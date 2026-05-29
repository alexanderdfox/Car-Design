# Formic-1 Charging Nest — Image & SVG Prompt Pack

Copy **nest master prefix** + one scene + **negative suffix** into image models or CAD tools. SVG schematics live in [assets/nest/](../assets/nest/).

## Nest master prefix

```text
You are designing charging nest INFRASTRUCTURE for Formic-1 electric logistics vans—not a fleet commander.
Rules: nest is a place (depot + swap yard); forty stalls; agents read/write stall pheromone on a shared map (reserved_until, price_kw, swap_ready, v2g_enabled); no central scheduler API; no dispatcher assigning slots per second.
Electric: 150 kW DC per stall, cassette swap rails 1800x1400x220 mm, 2.4 MVA site with diversity factor 0.65, optional per-vehicle V2G opt-in only.
Aesthetic: matte industrial yard, orange safety markings, no hex-hive architecture, no queen control tower.
```

## Negative suffix (always append)

```text
Do NOT: central queue dispatcher, queen control tower, hex honeycomb depot layout, hive mind operations center, fleet-wide V2G discharge command, assigning car N to stall M from HQ, waggle-dance metaphor, glowing hive core building.
```

---

## Scene prompts (match design doc sections)

### 1. Site summary

```text
[NEST MASTER PREFIX]
Site plan diagram: 120 m x 80 m industrial parcel, 40 swap/charge stalls, 2.4 MVA grid feed annotation, 1.56 MVA diversified cap callout, buffer lane, cassette storage zone. Clean engineering infographic.
[NEGATIVE SUFFIX]
```

### 2. Layout plan

```text
[NEST MASTER PREFIX]
Top-down nest layout: street ingress/egress with UWB anchors, buffer lane, Row A stalls S01-S20 swap lifts, Row B S21-S40, CCS overflow pads, cassette storage. Label stall IDs. Orthographic plan view.
[NEGATIVE SUFFIX]
```

### 3. Stall pheromone fields

```text
[NEST MASTER PREFIX]
Data diagram: each stall cell exposes TTL fields reserved_until, price_kw, swap_ready, v2g_enabled. Show read/write by agents, evaporation on stale reservations. No central database assigning all queues.
[NEGATIVE SUFFIX]
```

### 4. Local allocation flow

```text
[NEST MASTER PREFIX]
Flowchart: agent seeking_nest reads stalls within 2 km horizon, computes cost with INF if reserved, softmax pick, write reserved_until 12 min, drive UWB+dock, clear on exit. Forbidden side panel: global re-sort every second.
[NEGATIVE SUFFIX]
```

### 5. SOC thresholds and spillback

```text
[NEST MASTER PREFIX]
Diagram: SOC bands Normal >40%, Lean 25-40%, Seek nest 15-25%, Critical <15% with low_soc_spill on street graph; street_queue_pheromone on ingress when stalls blocked. Formic-1 vans as icons only.
[NEGATIVE SUFFIX]
```

### 6. Price load balancing

```text
[NEST MASTER PREFIX]
Chart: price_kw = base_rate * (1 + 0.6 * utilization) - solar_offset; stalls as bars; agents distributed toward cheaper stalls. Night V2G branch only if v2g_opt_in on vehicle.
[NEGATIVE SUFFIX]
```

### 7. Electrical one-line

```text
[NEST MASTER PREFIX]
Single-line electrical diagram: utility 2.4 MVA, two 1.2 MVA transformers, bus A odd stalls, bus B even stalls, 150 kW DC per stall, swap robotics 12 kW. kW_cap raises price_kw trace when bus >90%—not broadcast throttle.
[NEGATIVE SUFFIX]
```

### 8. Human operator scope

```text
[NEST MASTER PREFIX]
Split panel: ALLOWED (close row maintenance, fire E-stop, adjust price_kw floor) vs FORBIDDEN (assign car to stall, global route table, queen console). Minimal control room, no throne aesthetic.
[NEGATIVE SUFFIX]
```

---

## SVG assets (all combinations)

| Doc section | Prompt | SVG |
|-------------|--------|-----|
| Key | Master + negative | [nest-00-prompt-key.svg](../assets/nest/nest-00-prompt-key.svg) |
| 1. Site summary | Scene 1 | [nest-01-site-summary.svg](../assets/nest/nest-01-site-summary.svg) |
| 2. Layout plan | Scene 2 | [nest-02-layout-plan.svg](../assets/nest/nest-02-layout-plan.svg) |
| 3. Stall pheromone | Scene 3 | [nest-03-stall-pheromone.svg](../assets/nest/nest-03-stall-pheromone.svg) |
| 4. Allocation flow | Scene 4 | [nest-04-allocation-flow.svg](../assets/nest/nest-04-allocation-flow.svg) |
| 5. SOC spillback | Scene 5 | [nest-05-soc-spillback.svg](../assets/nest/nest-05-soc-spillback.svg) |
| 6. Price balancing | Scene 6 | [nest-06-price-load-balance.svg](../assets/nest/nest-06-price-load-balance.svg) |
| 7. Electrical one-line | Scene 7 | [nest-07-electrical-oneline.svg](../assets/nest/nest-07-electrical-oneline.svg) |
| 8. Operator scope | Scene 8 | [nest-08-operator-scope.svg](../assets/nest/nest-08-operator-scope.svg) |

Legacy alias: [formic-nest-plan.svg](../assets/formic-nest-plan.svg) points to layout plan (section 2).

Full matrix: [assets/nest/README.md](../assets/nest/README.md)
