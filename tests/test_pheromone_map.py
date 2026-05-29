"""Unit tests: evaporation and fleet recovery when agents go offline."""

import unittest

from formic_stack.agent import Agent
from formic_stack.pheromone_map import ChargerClaim, PheromoneMap
from formic_stack.topics import BANNED_TOPICS, MapNode


class TestEvaporation(unittest.TestCase):
    def test_route_pheromone_decays(self) -> None:
        pmap = PheromoneMap(evaporation_per_minute=0.95)
        pmap.deposit_route((0, 0), (1, 0), success=True)
        self.assertAlmostEqual(pmap.read_route((0, 0), (1, 0)), 0.5)
        pmap.evaporate(now=1.0)
        self.assertLess(pmap.read_route((0, 0), (1, 0)), 0.5)
        pmap.evaporate(now=100.0)
        self.assertLess(pmap.read_route((0, 0), (1, 0)), 0.01)

    def test_charger_reservation_expires(self) -> None:
        pmap = PheromoneMap()
        pmap.charger_claim[(5, 5)] = ChargerClaim(reserved_until=100.0)
        self.assertFalse(pmap.reserve_charger((5, 5), now=50.0))
        pmap.evaporate(now=101.0)
        self.assertTrue(pmap.reserve_charger((5, 5), now=101.0))


class TestOfflineRecovery(unittest.TestCase):
    def test_thirty_percent_offline_still_delivers_traces(self) -> None:
        pmap = PheromoneMap(evaporation_per_minute=0.95, deposit_delta=0.4)
        agents = [Agent(agent_id=f"A{i}", cell=(0, 0)) for i in range(10)]
        for i, a in enumerate(agents):
            if i % 3 == 0:
                a.online = False
        online = [a for a in agents if a.online]
        self.assertGreaterEqual(len(online), 6)
        for step in range(30):
            pmap.evaporate(now=float(step))
            for a in online:
                a.step(pmap, [(1, 0), (0, 1)], goal=(5, 5))
        self.assertGreater(len(pmap.route_pheromone), 0)


class TestBannedTopics(unittest.TestCase):
    def test_fleet_command_banned(self) -> None:
        node = MapNode()
        with self.assertRaises(ValueError):
            node.get_topic("/fleet/command")
        self.assertIn("/fleet/command", BANNED_TOPICS)


if __name__ == "__main__":
    unittest.main()
