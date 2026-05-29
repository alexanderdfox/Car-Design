"""Shared environmental map layers with TTL (stigmergy). No fleet command topic."""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

Cell = Tuple[int, int]
Edge = Tuple[Cell, Cell]


def _norm_edge(a: Cell, b: Cell) -> Edge:
    return (a, b) if a <= b else (b, a)


@dataclass
class ChargerClaim:
    reserved_until: float = 0.0
    price_kw: float = 0.12
    swap_ready: bool = True
    v2g_enabled: bool = False


@dataclass
class PheromoneMap:
    """Grid map: route pheromone on edges, hazards and charger claims on cells."""

    evaporation_per_minute: float = 0.95
    deposit_delta: float = 0.5
    route_pheromone: Dict[Edge, float] = field(default_factory=dict)
    hazard: Dict[Cell, bool] = field(default_factory=dict)
    charger_claim: Dict[Cell, ChargerClaim] = field(default_factory=dict)
    congestion: Dict[Cell, float] = field(default_factory=dict)
    _last_evap: float = 0.0  # minutes (simulation clock or wall clock)

    def evaporate(self, now: Optional[float] = None) -> None:
        now = now if now is not None else time.time() / 60.0
        elapsed_min = max(0.0, now - self._last_evap)
        if elapsed_min <= 0:
            return
        factor = self.evaporation_per_minute**elapsed_min
        for edge in list(self.route_pheromone):
            self.route_pheromone[edge] *= factor
            if self.route_pheromone[edge] < 1e-4:
                del self.route_pheromone[edge]
        for cell in list(self.congestion):
            self.congestion[cell] *= factor
            if self.congestion[cell] < 1e-4:
                del self.congestion[cell]
        for cell, claim in self.charger_claim.items():
            if claim.reserved_until > 0 and now > claim.reserved_until:
                claim.reserved_until = 0.0
        self._last_evap = now

    def deposit_route(self, a: Cell, b: Cell, success: bool) -> None:
        if not success:
            return
        e = _norm_edge(a, b)
        self.route_pheromone[e] = self.route_pheromone.get(e, 0.0) + self.deposit_delta

    def read_route(self, a: Cell, b: Cell) -> float:
        return self.route_pheromone.get(_norm_edge(a, b), 0.0)

    def set_hazard(self, cell: Cell, active: bool) -> None:
        if active:
            self.hazard[cell] = True
        elif cell in self.hazard:
            del self.hazard[cell]

    def reserve_charger(
        self, cell: Cell, hold_seconds: float = 720.0, now: Optional[float] = None
    ) -> bool:
        now = now if now is not None else time.time()
        claim = self.charger_claim.setdefault(cell, ChargerClaim())
        if claim.reserved_until > now:
            return False
        claim.reserved_until = now + hold_seconds
        return True

    def stall_cost(self, cell: Cell, distance_km: float, now: Optional[float] = None) -> float:
        now = now if now is not None else time.time()
        claim = self.charger_claim.get(cell)
        if claim is None:
            return distance_km + 1.0
        if claim.reserved_until > now:
            return math.inf
        if not claim.swap_ready:
            return math.inf
        return distance_km + claim.price_kw * 10.0
