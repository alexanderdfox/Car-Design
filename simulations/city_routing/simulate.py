#!/usr/bin/env python3
"""
Simulate 200 electric Formic-1 agents on a city grid (ant mode vs forbidden bee mode).

Ant mode: local pheromone read/write, probabilistic edges, 5% evaporation per minute.
Bee mode: central server assigns shortest path each tick (labeled baseline — rejected design).
"""

from __future__ import annotations

import heapq
import math
import random
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from formic_stack.agent import Agent, AgentConfig
from formic_stack.pheromone_map import PheromoneMap

Cell = Tuple[int, int]
Edge = Tuple[Cell, Cell]

GRID = 20
N_AGENTS = 200
TICK_S = 5
STEPS = 120  # 10 min sim
EVAP_PER_MIN = 0.95
EPSILON = 0.1


def grid_neighbors(c: Cell) -> List[Cell]:
    x, y = c
    out = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID and 0 <= ny < GRID:
            out.append((nx, ny))
    return out


def manhattan(a: Cell, b: Cell) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dijkstra(start: Cell, goal: Cell, blocked: Dict[Cell, bool]) -> List[Cell]:
    """Central optimal path — bee mode only."""
    pq: List[Tuple[float, Cell]] = [(0.0, start)]
    dist = {start: 0.0}
    prev: Dict[Cell, Cell] = {}
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            path = [u]
            while u in prev:
                u = prev[u]
                path.append(u)
            return list(reversed(path))
        if d > dist.get(u, math.inf):
            continue
        for v in grid_neighbors(u):
            if blocked.get(v, False):
                continue
            nd = d + 1.0
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return [start]


@dataclass
class Metrics:
    deliveries: int = 0
    total_latency: float = 0.0
    total_kwh: float = 0.0
    total_km: float = 0.0
    congestion_sum: float = 0.0


@dataclass
class DeliveryAgent:
    agent: Agent
    goal: Cell
    path: List[Cell] = field(default_factory=list)
    path_idx: int = 0
    assigned_at: int = 0
    delivered_at: int = -1

    @property
    def delivered(self) -> bool:
        return self.delivered_at >= 0


def run_ant_mode(seed: int = 42) -> Metrics:
    rng = random.Random(seed)
    pmap = PheromoneMap(evaporation_per_minute=EVAP_PER_MIN, deposit_delta=0.4)
    metrics = Metrics()
    agents: List[DeliveryAgent] = []
    for i in range(N_AGENTS):
        start = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        goal = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        while goal == start:
            goal = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        a = Agent(agent_id=f"M-{i:03d}", cell=start, soc=rng.uniform(0.5, 0.95))
        agents.append(DeliveryAgent(agent=a, goal=goal))

    for step in range(STEPS):
        pmap.evaporate(now=step * TICK_S / 60.0)
        for da in agents:
            if da.delivered:
                continue
            neighbors = grid_neighbors(da.agent.cell)
            before = da.agent.cell
            da.agent.step(pmap, neighbors, da.goal, rng)
            hop = manhattan(before, da.agent.cell) * 0.2
            metrics.total_km += hop
            metrics.total_kwh += da.agent.kwh_per_km * hop
            metrics.congestion_sum += pmap.congestion.get(before, 0.0)
            if da.agent.cell == da.goal:
                da.delivered_at = step
                metrics.deliveries += 1
                metrics.total_latency += step - da.assigned_at
                pmap.deposit_route(before, da.goal, success=True)

    return metrics


def run_bee_mode(seed: int = 42) -> Metrics:
    """Forbidden baseline: one server re-plans globally optimal path each tick."""
    rng = random.Random(seed)
    pmap = PheromoneMap()
    metrics = Metrics()
    agents: List[DeliveryAgent] = []
    for i in range(N_AGENTS):
        start = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        goal = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        while goal == start:
            goal = (rng.randint(0, GRID - 1), rng.randint(0, GRID - 1))
        a = Agent(agent_id=f"B-{i:03d}", cell=start, soc=rng.uniform(0.5, 0.95))
        agents.append(DeliveryAgent(agent=a, goal=goal))

    for step in range(STEPS):
        for da in agents:
            if da.delivered:
                continue
            # Central planner — bee mode
            path = dijkstra(da.agent.cell, da.goal, pmap.hazard)
            if len(path) < 2:
                continue
            nxt = path[1]
            before = da.agent.cell
            da.agent.cell = nxt
            da.agent.soc = max(0.0, da.agent.soc - da.agent.kwh_per_km * 0.2 / 75.0)
            hop = manhattan(before, nxt) * 0.2
            metrics.total_km += hop
            metrics.total_kwh += da.agent.kwh_per_km * hop
            if da.agent.cell == da.goal:
                da.delivered_at = step
                metrics.deliveries += 1
                metrics.total_latency += step
    return metrics


def main() -> None:
    print("Formic-1 city routing simulation")
    print(f"  Agents: {N_AGENTS}, grid: {GRID}x{GRID}, steps: {STEPS} (@ {TICK_S}s)\n")

    ant = run_ant_mode()
    bee = run_bee_mode()

    def report(label: str, m: Metrics) -> None:
        n = max(m.deliveries, 1)
        print(f"=== {label} ===")
        print(f"  Deliveries:     {m.deliveries} / {N_AGENTS}")
        print(f"  Mean latency:   {m.total_latency / n:.1f} ticks")
        print(f"  Total distance: {m.total_km:.1f} km")
        print(f"  Total energy:   {m.total_kwh:.2f} kWh")
        print(f"  kWh/km:         {m.total_kwh / max(m.total_km, 1e-6):.3f}")
        print(f"  Congestion Σ:   {m.congestion_sum:.1f}")
        print()

    report("ANT MODE (stigmergy, local rules)", ant)
    report("BEE MODE (rejected — central planner each tick)", bee)
    print("Bee mode is included only as a forbidden comparison baseline.")


if __name__ == "__main__":
    main()
