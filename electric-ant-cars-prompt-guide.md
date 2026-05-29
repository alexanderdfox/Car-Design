# Electric Ant Cars — Prompt Usage Guide

Use these prompts to generate, design, or simulate **electric vehicles that behave like an ant colony**—not a bee hive mind. Each unit is simple, local, and reactive; order emerges from **stigmergy** (shared traces in the environment), not from a central commander.

---

## Core idea (ants vs bees)

| Ant colony (use this) | Bee hive mind (avoid this) |
|----------------------|----------------------------|
| No single “queen” controller | One central brain broadcasts orders |
| Decisions from **local sensing + pheromone-like signals** | Ranked hierarchy: drone → worker → queen |
| Robust when individuals fail | Fragile if the hub fails |
| Paths **reinforced by use**, fade when unused | Fixed roles assigned top-down |
| **Electric**: quiet, modular, swappable packs, grid/cell “nests” | Treat fleet as one organism with a soul |

**One-line constraint for every prompt:**

> Electric vehicles; decentralized ant-colony coordination via environmental traces and local rules only—no central hive controller, no queen node, no broadcast hive-mind.

---

## Vocabulary to reuse in prompts

- **Agent** — one car (or one delivery pod), not “the fleet brain”
- **Stigmergy** — leave/read traces: heat maps, occupancy grids, charge-slot reservations, route pheromone decay
- **Nest** — depot, hub, or charging yard (a *place*, not a commander)
- **Trail** — preferred corridor strengthened by traffic, weakened over time
- **Scout** — explores low-confidence areas; **forager** — exploits known good routes
- **Evaporation** — old data expires so the system adapts (traffic, outages, full chargers)
- **Electric constraints** — SOC bands, kW limits, regenerative braking, V2G optional, thermal derating

---

## Master system prompt (copy as prefix)

```text
You are designing/describing a fleet of electric road vehicles that coordinate like ants, not bees.

Rules:
1. No central AI that assigns every move. No "queen", "hive mind", or single orchestrator.
2. Each vehicle runs identical local logic: sense → score options → act → deposit a trace.
3. Coordination is environmental: digital pheromones (route cost, charger occupancy, hazard flags) that decay.
4. Failure tolerance: losing any vehicle or any edge node must not collapse the fleet.
5. Electric-first: battery state, charging curves, grid load, and range anxiety shape utility scores.
6. Explain behavior with simple rules (IF/weight tables), not opaque global optimization unless labeled as offline planning only.

When describing behavior, show what each car senses locally and what trace it writes. Do not anthropomorphize a collective consciousness.
```

---

## Task-specific prompt templates

### 1. Vehicle industrial design (electric + ant-like *form*)

```text
Design an electric urban logistics vehicle inspired by ant morphology (low profile, modular segments, optional coupling) but styled for roads—not insects cosmetically, but functionally: good ground clearance, swap battery tray, front sensor arc like antennae.

Constraints: BEV, 150–300 km useful range, fast depot charge, no autonomous "queen truck" leading a convoy by command—coupling is opt-in via local negotiation only.

Deliver: side view, package layout, sensor placement, how two units might briefly dock to pass a pack. Avoid futuristic hive aesthetic (hex honeycomb branding, unified glowing core "brain").
```

### 2. Traffic / routing (stigmergy, not central dispatch)

```text
Simulate 200 electric delivery ant-cars in a city grid. Each car every 5 s:
- Reads local traffic + pheromone map (edge weights increase with successful transits, decay 5%/min).
- Picks next edge via probabilistic choice (exploit high pheromone, explore with ε=0.1).
- Writes delivery success/failure at destination cell.

No central router. Compare to a forbidden baseline: one server assigns globally optimal paths each tick (label that "bee mode" and reject it).

Output: pseudocode for local agent, update rules for pheromone, metrics (latency, kWh/km, congestion).
```

### 3. Charging yard (nest as infrastructure)

```text
Design a charging "nest" for 40 electric ant-cars. Allocation rule: cars sense stall pheromone (reserved-until-time); reserve by writing timestamp; no dispatcher API.

Include: SOC thresholds for seeking nest, queue spillback to street traces, load balancing via price pheromone on stalls (cheap stalls attract), night V2G optional with per-car opt-in only.

Forbidden: central scheduler that sorts the entire queue each second.
```

### 4. Story / UX / game narrative

```text
Write a short scene where electric courier cars reorganize after a bridge closure. Show 3 cars making local decisions from stale vs fresh traces—older paths fade, scouts find detours, foragers reinforce the new corridor.

Tone: grounded sci-fi. No telepathy, no hive voice chorus. Optional: one human operator adjusts nest capacity only, not individual routes.
```

### 5. Code / robotics stack

```text
Implement a ROS2-style multi-agent stack for electric differential-drive pods:
- Node per vehicle: local planner + pheromone publisher/subscriber on grid topic.
- Shared map layer with TTL fields (route_pheromone, hazard, charger_claim).
- No /fleet/command topic; ban single master planner node.

Language: [Python/C++]. Include unit tests for evaporation and for recovery when 30% of agents drop offline.
```

---

## Negative prompts (append to avoid hive mind)

```text
Do NOT: central fleet brain, queen vehicle, synchronized swarm thinking, shared consciousness, bee hierarchy, waggle-dance metaphor as command protocol, all cars receiving identical orders each tick, hex-hive branding as the main aesthetic, diesel or ICE powertrains unless explicitly for contrast only.
```

---

## Parameter cheat sheet (tune in prompts)

| Knob | Ant-like meaning | Typical range |
|------|------------------|---------------|
| Pheromone deposit Δ | reward a used edge/cell | 0.1–1.0 per success |
| Evaporation λ | forget outdated info | 0.95–0.99 per minute |
| Exploration ε | scout probability | 0.05–0.15 |
| SOC_min | seek nest | 15–25% |
| kW_cap per nest | grid constraint | nameplate × diversity factor |
| Local horizon | how far each car plans | 3–8 hops / 30–120 s |

---

## Quality checklist (before you accept output)

- [ ] Can you remove any one car without explaining a fleet-wide crash?
- [ ] Is every coordination mechanism readable on a map/trace/topic?
- [ ] Is power (kWh, SOC, charge rate) part of the utility function?
- [ ] Did the model sneak in a “master controller”? If yes, rewrite with nest-as-infrastructure only.
- [ ] Are bees/hive/queen metaphors absent or only in a “do not use” contrast?

---

## Minimal one-shot example

```text
Describe how 12 electric ant-cars clear a stadium exit after an event using stigmergy only. Each car senses bumper density within 50 m, deposits congestion pheromone on its cell, and chooses the exit lane with lowest effective cost (distance + congestion − route pheromone). Trails to the north parking lot strengthen; east lot pheromone evaporates after 20 min. No central traffic AI. 200 words, bullet rules first.
```

---

## File purpose

This document is a **prompt cookbook** for image models, LLMs, simulators, and code assistants. Keep the ant/electric/decentralized triangle explicit in every request so outputs stay away from electric “hive” clichés and toward **colony intelligence without a king**.
