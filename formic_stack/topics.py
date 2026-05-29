"""ROS2-style pub/sub without /fleet/command or master planner."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Set

# Explicitly banned topic names (documentation + runtime guard)
BANNED_TOPICS = frozenset({"/fleet/command", "/hive/orders", "/queen/plan"})


@dataclass
class Topic:
    name: str
    subscribers: List[Callable[[Any], None]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.name in BANNED_TOPICS:
            raise ValueError(f"Banned central command topic: {self.name}")

    def publish(self, msg: Any) -> None:
        for cb in self.subscribers:
            cb(msg)

    def subscribe(self, callback: Callable[[Any], None]) -> None:
        self.subscribers.append(callback)


class MapNode:
    """Shared map layer node — not a master planner."""

    def __init__(self) -> None:
        self._topics: Dict[str, Topic] = {}
        self._allowed: Set[str] = {
            "/map/route_pheromone",
            "/map/hazard",
            "/map/charger_claim",
            "/map/congestion",
            "/vehicle/telemetry",
        }

    def get_topic(self, name: str) -> Topic:
        if name in BANNED_TOPICS:
            raise ValueError(f"Banned topic: {name}")
        if name not in self._allowed and not name.startswith("/vehicle/"):
            raise ValueError(f"Topic not on allowlist: {name}")
        if name not in self._topics:
            self._topics[name] = Topic(name)
        return self._topics[name]


@dataclass
class VehicleNode:
    """One node per vehicle: local planner + pheromone pub/sub."""

    vehicle_id: str
    map_node: MapNode

    def publish_telemetry(self, payload: dict) -> None:
        self.map_node.get_topic(f"/vehicle/{self.vehicle_id}/telemetry").publish(payload)
