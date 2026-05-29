# Formic-1 Charging Nest — Infrastructure Design

A **nest** is a place (depot + charging yard), not a commander. Forty **Formic-1** agents allocate stalls by reading and writing **stall pheromone** on a shared map layer—no central scheduler API.

**Constraint:** Electric vehicles; decentralized ant-colony coordination via environmental traces and local rules only—no central hive controller, no queen node, no broadcast hive-mind.

**Related:** [electric-ant-car-design-guide.md](../electric-ant-car-design-guide.md) · [electric-ant-cars-prompt-guide.md](../electric-ant-cars-prompt-guide.md)

---

## 1. Site summary

| Parameter | Value |
|-----------|--------|
| Capacity | 40 stalls (swap + charge) |
| Footprint | 120 m × 80 m (industrial parcel) |
| Grid feed | 2.4 MVA nameplate; diversity factor 0.65 → **1.56 MVA** planning cap |
| Per-stall peak | 150 kW DC + 12 kW swap robotics |
| Swap rails | Shared Formic-1 cassette geometry (1,800 × 1,400 × 220 mm) |
| V2G | Optional night export; **per-agent opt-in only** |

---

## 2. Layout (plan)

```
                    STREET (queue spillback writes street_pheromone)
    ═══════════════════════════════════════════════════════════════
         ingress UWB        ingress UWB
              |                  |
    ┌─────────┴──────────────────┴─────────┐
    │  BUFFER LANE (slow pass, no stops)   │
    ├──────┬──────┬──────┬──────┬──── ... ─┤
    │ S01  │ S02  │ S03  │ S04  │   ...    │  Row A — swap lifts
    ├──────┼──────┼──────┼──────┼──────────┤
    │ S11  │ S12  │ ...                   │  Row B
    ├──────┴──────┴───────────────────────┤
    │  CCS overflow pads (slow charge)     │
    ├─────────────────────────────────────┤
    │  Cassette storage (charged / empty)  │
    └─────────────────────────────────────┘
              │                  │
         egress UWB        egress UWB
    ═══════════════════════════════════════════════════════════════
                    STREET
```

- **Stalls S01–S40:** guided rails, floor lift, rear alignment cones + UWB anchor per stall.
- **No dispatcher office logic**—only human operator panel for **nest capacity** (open/close rows, fire stop), not per-vehicle routes.

---

## 3. Stall pheromone (allocation rules)

Each stall cell on the map exposes a TTL field:

| Field | Type | Meaning |
|-------|------|---------|
| `reserved_until` | UTC timestamp | Hold stall; others treat as infinite cost until evaporation |
| `price_kw` | float | Dynamic $/kWh equivalent for load balancing |
| `swap_ready` | bool | Lift idle, cassette stock present |
| `v2g_enabled` | bool | Stall hardware allows export |

### 3.1 Local agent algorithm (every car, identical)

```
ON seeking_nest (SOC < SOC_min OR scheduled swap):
  READ stalls within radio horizon H (default 2 km map tile)
  FOR each stall s:
    cost[s] = wait_estimate(s) + price_kw[s] * expected_kWh + distance
    IF now < s.reserved_until: cost[s] = INF
  PICK stall s* with softmax(-cost)  // no global sort of all 40 queues
  IF random() < commit_threshold:
    WRITE s*.reserved_until = now + T_hold  (T_hold = 12 min default)
  DRIVE using UWB + rear camera into s*
  ON arrival: WRITE swap_ready consumption; CLEAR reservation when exit
```

**Forbidden:** service that re-sorts all 40 queues every second and pushes slot IDs to cars.

### 3.2 Evaporation

- Unclaimed reservation older than `T_hold` auto-clears (λ ≈ 0.99/min on stale claims).
- `price_kw` decays toward base rate when stall idle &gt; 10 min.

---

## 4. SOC thresholds and queue spillback

| Band | SOC | Behavior |
|------|-----|----------|
| Normal | &gt; 40% | Deliveries only; pass nest without write |
| Lean | 25–40% | Bias route toward nests with low `price_kw` |
| Seek nest | 15–25% (`SOC_min`) | Must acquire stall pheromone or raise hazard trace |
| Critical | &lt; 15% | Deposits **low_soc_spill** on street graph; peers reroute |

**Spillback:** if all nearby `reserved_until` block agents, cars write **street_queue_pheromone** on ingress edges. Others read increased edge cost—trails redirect to alternate nests or CCS overflow pads without a central router.

---

## 5. Load balancing via price pheromone

```
price_kw[stall] = base_rate * (1 + 0.6 * utilization_15min) - solar_offset
```

- High utilization → higher price → agents prefer cheaper stalls (distributed choice, not one optimizer).
- Night **V2G:** only if agent sets `v2g_opt_in=true` locally; stall writes export tariff trace; no fleet-wide discharge command.

---

## 6. Electrical one-line (conceptual)

- 2 × 1.2 MVA transformers → bus A / bus B.
- Stalls odd on A, even on B for phase balance.
- **kW_cap enforcement:** stall controller lowers `swap_ready` and raises `price_kw` when bus &gt; 90% cap—agents read traces, not a broadcast throttle message.

---

## 7. Human operator scope (allowed)

| Allowed | Forbidden |
|---------|-----------|
| Close row for maintenance | Assign car 17 to stall 4 |
| Fire emergency stop | Push global route table |
| Adjust base `price_kw` floor | “Queen console” convoy launch |

---

## 8. Quality checklist

- [x] Remove any stall controller—others still pick among remaining stalls.
- [x] Coordination = `reserved_until`, `price_kw`, street spillback on map.
- [x] SOC and kWh in agent utility (see design guide §8).
- [x] No master scheduler.
- [x] No hive/queen product language.

---

## 9. Integration with code

Map fields are implemented in `formic_stack/pheromone_map.py` as `charger_claim` TTL cells. Run agents against a 40-stall fixture in tests.
