# After the Bridge — Scene

Grounded sci-fi. Three **Formic-1** agents, local traces only. One human adjusts nest row capacity—not routes.

---

The river bridge had been closed for eleven minutes when Unit **M-07** rolled to the intersection and stopped—not because anyone told the fleet to stop, but because the hazard cell on the shared grid still glowed amber from the first witness: a construction barrel knocked into lane two, confirmed by three passing agents before the flag hardened.

M-07’s cab display showed two corridors: west along Riverside, pheromone strength **0.82** from an hour of successful deliveries; east through the tunnel loop, strength **0.41** and fading. Evaporation had not yet killed the west trail. The bridge closure was newer than the map’s habit.

**Rule on M-07:** if `hazard[edge] == true`, effective cost = ∞. Scout mode: ε ← 0.12.

M-07 chose southbound—unfamiliar, low pheromone—and wrote a faint deposit on the edge it left: `route_pheromone += 0.15`, success unknown. No voice in its radio. No chorus.

---

Two blocks behind, **M-19** was a forager. Its last four hops had been high-confidence; ε at 0.05. It read M-07’s fresh southbound trace and the decaying west river trail. Stale west looked cheap until hazard subtraction. M-19’s utility table:

| Edge | Distance | Congestion | −Pheromone | Hazard | Score |
|------|----------|------------|------------|--------|-------|
| West (river) | 1.2 km | 0.3 | −0.79 | ∞ | blocked |
| East loop | 2.8 km | 0.1 | −0.38 | 0 | 2.52 |
| South (scout) | 1.0 km | 0.2 | −0.14 | 0 | 1.06 |

M-19 took the east loop—longer, but the only finite cost. At the destination cell it wrote `delivery_success`, deposit Δ = 0.7. The east loop’s pheromone would strengthen for the next hour unless evaporation and a better detour appeared.

---

**M-33** had been southbound before the closure, carrying a medical kit pallet. Its SOC read 22%—inside **seek nest** band. It did not call a dispatcher. It read stall traces within eight kilometers: four nests, twelve free stalls with `price_kw` spread. Nest **Gamma** on Canal Street had the lowest price trace and a `reserved_until` slot it could claim with a twelve-minute hold.

M-33 wrote `reserved_until` to Gamma stall 6, published nothing to siblings except the side effect of a occupied stall cell, and turned north on a corridor whose pheromone had evaporated to 0.09. An older path, forgotten. That was fine. Gamma’s charger did not care about the bridge.

---

At the operations desk, one human slid a maintenance toggle: **Nest Gamma, Row B → offline** for a tripped breaker. Not “send everyone to Delta.” Row capacity changed; the map updated. M-33’s reservation held on Row A. Other agents approaching Gamma would read higher `price_kw` on Row B stalls and scatter by local softmax—no hive mind, just math on shared ink.

By minute twenty, west river pheromone had fallen below 0.2. South and east trails braided through the grid. The bridge was still closed. The colony had not agreed on anything. The road had.

---

**Bullets (behavior rules shown in scene)**

- Hazard flags block edges locally; no central reroute broadcast.
- Scouts raise ε and deposit weak trails; foragers exploit reinforced corridors.
- Pheromone evaporates; stale west becomes a trap unless hazard logic intervenes.
- SOC triggers nest seek via stall `reserved_until` / `price_kw`, not HQ assignment.
- Human touches **infrastructure capacity** only.
