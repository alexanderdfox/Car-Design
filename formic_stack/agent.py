"""Local agent: sense → score → act → deposit. Identical logic per vehicle."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from formic_stack.pheromone_map import Cell, PheromoneMap

Edge = Tuple[Cell, Cell]


@dataclass
class AgentConfig:
    exploration_epsilon: float = 0.1
    soc_min: float = 0.20
    alpha_energy: float = 2.0
    beta_kwh: float = 0.3
    scout_epsilon: float = 0.12
    forager_epsilon: float = 0.05


@dataclass
class Agent:
    agent_id: str
    cell: Cell
    soc: float = 0.85
    pack_temp_c: float = 35.0
    config: AgentConfig = field(default_factory=AgentConfig)
    online: bool = True
    kwh_per_km: float = 0.22

    def effective_epsilon(self, pmap: PheromoneMap, goal: Cell) -> float:
        """Scout when pheromone confidence low or sensor derate (hot pack)."""
        neighbors = [n for _, n in self._neighbor_edges()]
        if not neighbors:
            return self.config.scout_epsilon
        avg_ph = sum(pmap.read_route(self.cell, n) for n in neighbors) / len(neighbors)
        if avg_ph < 0.15 or self.pack_temp_c > 45.0:
            return self.config.scout_epsilon
        return self.config.forager_epsilon

    def energy_cost(self, hop_km: float) -> float:
        soc = max(self.soc, 0.05)
        return self.config.alpha_energy * (1.0 / soc) + self.config.beta_kwh * self.kwh_per_km * hop_km

    def edge_cost(
        self,
        pmap: PheromoneMap,
        nxt: Cell,
        hop_km: float = 0.2,
        goal: Optional[Cell] = None,
    ) -> float:
        if pmap.hazard.get(nxt, False):
            return math.inf
        cong = pmap.congestion.get(nxt, 0.0)
        ph = pmap.read_route(self.cell, nxt)
        dist = hop_km
        if goal is not None:
            dist += 0.01 * (abs(nxt[0] - goal[0]) + abs(nxt[1] - goal[1]))
        cost = dist + cong - ph + self.energy_cost(hop_km)
        if self.soc < self.config.soc_min:
            cost += 5.0
        return cost

    def choose_next(
        self,
        pmap: PheromoneMap,
        neighbors: List[Cell],
        goal: Cell,
        rng: Optional[random.Random] = None,
    ) -> Cell:
        rng = rng or random.Random()
        if not neighbors:
            return self.cell
        eps = self.effective_epsilon(pmap, goal)
        costs = [self.edge_cost(pmap, n, goal=goal) for n in neighbors]
        if all(c == math.inf for c in costs):
            return rng.choice(neighbors)
        if rng.random() < eps:
            return rng.choice(neighbors)
        weights = []
        for c in costs:
            if c == math.inf:
                weights.append(0.0)
            else:
                weights.append(math.exp(-c))
        total = sum(weights)
        if total <= 0:
            return rng.choice(neighbors)
        r = rng.random() * total
        acc = 0.0
        for n, w in zip(neighbors, weights):
            acc += w
            if r <= acc:
                return n
        return neighbors[-1]

    def step(
        self,
        pmap: PheromoneMap,
        neighbors: List[Cell],
        goal: Cell,
        rng: Optional[random.Random] = None,
    ) -> Cell:
        if not self.online:
            return self.cell
        rng = rng or random.Random()
        nxt = self.choose_next(pmap, neighbors, goal, rng)
        # Deposit on successful transit; extra weight if hop completes delivery
        pmap.deposit_route(self.cell, nxt, success=True)
        if nxt == goal:
            pmap.deposit_route(self.cell, nxt, success=True)
        pmap.congestion[self.cell] = pmap.congestion.get(self.cell, 0.0) + 0.1
        self.soc = max(0.0, self.soc - self.kwh_per_km * 0.2 / 75.0)
        self.cell = nxt
        return nxt

    def _neighbor_edges(self) -> List[Edge]:
        x, y = self.cell
        return [((x, y), (x + 1, y)), ((x, y), (x, y + 1))]
