# Electric Ant-Car — How to Design

A complete industrial-design brief for a **single agent** (one urban logistics BEV) in a decentralized fleet. Coordination is environmental (stigmergy); this document defines **hardware, layout, and local behavior**—not a central fleet brain.

**Design constraint (carry into every drawing and spec):**

> Electric vehicle; decentralized ant-colony coordination via environmental traces and local rules only—no central hive controller, no queen node, no broadcast hive-mind.

**Related:** [electric-ant-cars-prompt-guide.md](./electric-ant-cars-prompt-guide.md) (prompt cookbook).

---

## 1. What you are designing

| Term | Meaning for this vehicle |
|------|---------------------------|
| **Agent** | This car alone—identical logic to every sibling unit |
| **Nest** | Depot/charging yard (infrastructure you drive toward, not a commander) |
| **Trail** | Digital route pheromone on shared maps—your planner reads/writes, not a server assigning your path |
| **Stigmergy** | You leave traces (charger reservation, hazard flag, congestion cell); others read and adapt |

You are **not** designing: a lead “queen” truck, a glowing unified core “brain,” hex-honeycomb hive branding, or a convoy that only moves when one unit broadcasts orders.

---

## 2. Design philosophy (form follows colony rules)

### 2.1 Ant morphology → road function (not insect cosplay)

Borrow **function**, not literal bugs:

| Ant trait | Vehicle translation |
|-----------|---------------------|
| Low, segmented body | Low roof (~1.85 m), **modular skid + cabin** on a common platform rail |
| Mandibles / carry | **Front load zone** + side roller doors; no decorative pincers |
| Antennae | **Wide front sensor arc** (LiDAR + cameras + UWB) on stalks or faired pillars—not whiskers |
| Colony member, not queen | **No “command module”** variant; every unit has the same compute and sensors |
| Trail following | **Local map + pheromone layer** in software; body has **V2X / mesh radio**, not a fleet-only mast |
| Nest return | **Standardized rear charge port + optional underbody pantograph** at nest only |

### 2.2 Electric-first

- BEV only; **150–300 km useful range** (urban logistics, not long-haul).
- **Swap battery tray** (slide-under pack) for &lt;5 min depot turnover; **CCS fast charge** when swapping unavailable.
- **Regen** biased to stop-and-go blocks; **SOC bands** drive when the unit seeks a nest (see §8).
- Thermal: pack cooling ducts along sills; **derate motor kW** when pack &gt; 45 °C.

### 2.3 Decentralized coupling (optional, never commanded)

Two units may **briefly dock** to pass a battery module or transfer a pallet—only after **local negotiation** (UWB range, mutual consent flags on a short-range link). No “follow the leader” convoy mode.

---

## 3. How to design — step-by-step workflow

Use this order so mechanical, electrical, and software stay aligned.

### Step A — Define the mission envelope

1. **Payload:** 400–600 kg cargo or 4 m³ (pick one primary; document the other as secondary).
2. **Footprint:** Max length 4.2 m, width 1.8 m (EU urban lane + parking); wheelbase 2.6–2.8 m.
3. **Ground clearance:** 160 mm minimum (speed humps, curb cuts).
4. **Turning:** 10.5 m curb-to-curb or tighter with rear-axle steer option.

### Step B — Lock the platform architecture

1. **Skid:** Flat aluminum/steel composite tray with **ISO-like rail slots** for cabin and battery cassette.
2. **Battery cassette:** One sliding unit (~400–600 kg), 60–90 kWh usable, handles at sides for robot or human swap.
3. **Drivetrain:** Dual-motor RWD or single motor + e-axle; peak 80–120 kW, continuous 40 kW.
4. **Cabin:** Bolt-on module; same width as skid; forward control (cab-over) for visibility.

### Step C — Package the volume (see §5)

1. Cargo cube aft of cab bulkhead.
2. Thermal path: cabin HVAC does **not** share pack coolant loop except at nest preconditioning.
3. Crash: front deformable zone **outside** sensor arc mounts so repairs don’t recalibrate primary LiDAR.

### Step D — Place the “antennae” sensor arc (see §6)

1. 270°–300° horizontal FOV at bumper height + 1.2 m pillar cameras.
2. Redundancy: if front LiDAR fails, unit becomes **scout-only** (lower speed, higher ε)—does not halt the fleet.

### Step E — Specify dock / swap geometry (see §7)

1. Rear alignment cones + UWB anchors for nest stalls.
2. Side **coupling face** for agent-to-agent pack handoff (mechanical + electrical interlock).

### Step F — Skin and brand (see §9)

1. Matte utility panels, high-visibility edges, **no** hex hive graphics or “swarm mind” LED ring.

### Step G — Validate against checklist (§12)

---

## 4. Vehicle summary — “Formic-1” reference design

Working name: **Formic-1** (Latin for ant—use only in docs, not hive-themed marketing).

| Parameter | Target |
|-----------|--------|
| Type | BEV urban logistics van |
| GVW | ~3,200 kg |
| Curb weight (empty, with pack) | ~2,100 kg |
| Payload | 500 kg / 4.2 m³ |
| Pack (cassette) | 75 kWh usable, 400 V, liquid-cooled |
| Useful range | 220 km (mixed city, 50% load, climate on) |
| Depot charge | 150 kW DC on cassette port; 0–80% ~25 min |
| Swap time | Target 4 min (automated slide-lift at nest) |
| Top speed | 90 km/h (software cap for class) |
| Local compute | Edge box: 2× camera ISP, LiDAR driver, V2X; **no role as fleet server** |

---

## 5. Package layout

### 5.1 Side view (ASCII — use for sketches / image prompts)

```
                    ANTENNA ARC (sensors on faired pillars)
                   .---.   .---.   .---.
                  /     \ /     \ /     \
    [Cab]  ______/_______X_______X_______\________________ Cargo door
          |      |                               |  roller |
          | steer|   battery cassette (under)    |  door   |
    o-----+------+===============================+---------+-----o  <- wheels
          |<-- 2.7 m wheelbase -->|              |<- 1.8 m cargo ->|

    Front: deformable zone + short overhang
    Rear: charge port + optional pantograph pocket (nest only)
```

### 5.2 Plan view (top-down zones)

```
+------------------------------------------------------------------+
| F: Deformable + sensor arc (300 mm deep)                          |
+----------+-----------+---------------------------+----------------+
| Cab L    | Cab R     | CARGO (4.2 m³)            | Coupling face  |
| driver   | ingress     | tie-down rails, rollers | (optional)     |
+----------+-----------+---------------------------+----------------+
|          | BATTERY CASSETTE (full width, under cargo floor)       |
+------------------------------------------------------------------+
| R: Charge + nest alignment + camera rear                         |
+------------------------------------------------------------------+
```

### 5.3 Mass and CG

- Pack as low as possible (cassette between frame rails).
- Cargo floor 650 mm from ground; max load height 1,400 mm.
- Keep **60% mass** between axles loaded; software uses axle estimate for regen blend only—no fleet telematics required.

### 5.4 Module breakdown (build variants without a “queen”)

| Module | Swappable at depot | Notes |
|--------|-------------------|--------|
| Cabin | Yes (same rails) | Left- or right-hand drive |
| Battery cassette | Yes | Standard interface only |
| Rear axle / motor | Rare | Common across fleet |
| Sensor mast set | Yes | Calibrated per VIN |

Every module variant uses the **same** local agent firmware image.

---

## 6. Sensor and compute placement

### 6.1 Front “antennae” arc

| Sensor | Location | FOV / role |
|--------|----------|------------|
| Spinning or solid-state LiDAR | Center bumper, 400 mm height | 300° H, obstacle + curb |
| Wide camera pair | Pillar mounts, 1.35 m | Stereo depth, signs |
| Narrow camera | Roof front | Long-range lights |
| UWB | Bumper corners | Nest stall alignment, peer dock |
| Radar (optional) | Behind bumper skin | Rain/fog fill-in |

Fairings: **rounded rectangular pods**, matte black—not insect legs.

### 6.2 Sides and rear

| Sensor | Location | Role |
|--------|----------|------|
| Side cameras | Mid cargo, recessed | Parking, lane change |
| Ultrasonics | Corners | Low-speed gaps |
| Rear camera + LiDAR | Above charge door | Reverse, nest docking |
| IMU + wheel ticks | Chassis | Odometry for local grid |

### 6.3 Connectivity (traces, not commands)

- **V2X / 5G / mesh:** publish-subscribe to **map topics** (route_pheromone, hazard, charger_claim)—TTL fields evaporate on server edge or RSU; vehicle never subscribes to `/fleet/command`.
- **Onboard:** Store last 8 hops of local cost map; no requirement for cloud path.

---

## 7. Battery swap and peer dock (two agents)

### 7.1 Design goals

- Enable **nest** swap as default; **peer** swap only for emergency or remote recovery.
- No third vehicle acting as coordinator—only pairwise handshake.

### 7.2 Nest swap (infrastructure)

1. Agent reads **stall pheromone** (reserved-until timestamp) on local display / API to map layer.
2. Agent writes reservation; drives into stall using UWB + rear camera.
3. Floor lift supports cassette; slides pack out/in on rails shared with all Formic-1 units.
4. Pantograph optional for top-up while loading next cassette.

### 7.3 Peer dock (two Formic-1 units) — side view

```
  Agent A (donor)              Agent B (receiver)
  cargo side                         cargo side
      |                                   |
      |  [==== COUPLING FACE ====]        |
      |  align pins + data link           |
      v                                   v
  cassette partially ejected ------> receiver rail guides
```

**Sequence (local rules only):**

1. Both parked; UWB range &lt; 3 m; speed 0.
2. Exchange `DOCK_OFFER` / `DOCK_ACCEPT` over peer link (timeouts 30 s).
3. Mechanical interlock: shared side coupling face opens; **donor** ejects cassette 30%.
4. **Receiver** pulls cassette on motorized rails (receiver powered).
5. Donor retracts empty rail; faces disengage; each writes `pack_id` to its log and **charger_claim** trace at nest if heading in.

Forbidden: a third “supervisor” car or cloud script that triggers swap for the pair.

---

## 8. Onboard behavior (what each car runs)

Identical on every unit—shown so industrial design supports software needs.

### 8.1 Sense → score → act → deposit

Every 1–5 s (configurable):

1. **Sense:** SOC, local traffic, pheromone map slice (3–8 hops), stall prices, hazards.
2. **Score:** utility = distance + congestion − route_pheromone + energy_cost(SOC, kWh/km).
3. **Act:** next edge / lane / nest seek if SOC &lt; SOC_min (15–25%).
4. **Deposit:** success/failure at cell, congestion, optional delivery outcome Δ.

### 8.2 Scout vs forager (modes, not roles assigned by HQ)

| Mode | When | Behavior |
|------|------|----------|
| **Forager** | High pheromone confidence on route | Low ε (0.05), exploit trails |
| **Scout** | Stale map, closure, or sensor derate | ε = 0.10–0.15, explore |

### 8.3 Electric utility (always in score)

```
energy_cost = α * (1/SOC_remaining) + β * predicted_kWh_next_hop
If SOC < SOC_min → add large penalty unless edge leads toward nest with free stall pheromone
```

Thermal: if pack temp high, reduce α (prefer gentler routes with regen).

---

## 9. Styling and materials

### Do

- **Matte** white or light gray body; safety orange on bumpers and door edges.
- Flat panels, visible **segment line** between cab module and cargo (modularity honest in form).
- Small **agent ID** barcode / QR on rear door (for humans at nest—not fleet soul).
- LED status strip on rear: charge state only (amber/green)—not synchronized swarm patterns.

### Do not

- Hex honeycomb grille, “hive core” glowing center console.
- Unified glass dome implying one consciousness.
- “Queen edition” trim package or gold accent leader vehicle.
- Diesel/ICE cues (exhaust, grille mesh for cooling fiction).

---

## 10. Dimensions table (for CAD)

| Dimension | mm |
|-----------|-----|
| Overall length | 4,200 |
| Overall width | 1,800 |
| Overall height (unloaded) | 1,850 |
| Wheelbase | 2,700 |
| Front track / rear track | 1,530 / 1,530 |
| Ground clearance | 160 |
| Cargo L × W × H | 2,200 × 1,650 × 1,400 |
| Cassette L × W × H | 1,800 × 1,400 × 220 |
| Coupling face width | 1,200 (centered on cargo side) |

---

## 11. Prompts for image models and CAD assistants

Copy the **master prefix** from the prompt cookbook, then append one of:

### Side view render

```text
Side view of an electric urban delivery van, low profile cab-over design, modular cab on flat skid, matte white utility vehicle, orange bumper accents. Wide front sensor pods on two faired pillars like antennae—not insect legs. Underbody battery cassette visible in cutaway. Rear charge port. Ground clearance for city streets. No hexagon hive patterns, no glowing brain core, no insect cosplay. Photorealistic studio lighting, 3/4 rear secondary inset optional.
```

### Package layout diagram

```text
Technical diagram top view and side view of modular electric logistics van: cab forward, cargo box aft, battery cassette under cargo floor, sensor arc at front, coupling face on driver side midship. Labels for LiDAR, cameras, cargo volume, swap rails. Clean line art, engineering style, not futuristic hive aesthetic.
```

### Peer dock sequence

```text
Three-panel storyboard: two identical small electric delivery vans side by side in a parking lane, coupling face aligned, battery cassette transferring on rails. Urban setting. No lead truck, no drone overseer. Instructional technical illustration.
```

**Negative prompt (always append):**

```text
Do NOT: central fleet brain, queen vehicle, synchronized swarm thinking, hex-hive branding, diesel exhaust, insect monster truck, waggle-dance metaphor, glowing hive mind core.
```

---

## 12. Quality checklist (this design)

- [x] **Remove one car** — fleet continues; no single unit holds exclusive map or pack type.
- [x] **Coordination on traces** — stall reservation, route pheromone, hazards are environmental/TTL fields.
- [x] **Power in utility** — SOC, kWh/km, thermal derate in §8.
- [x] **No master controller** — peer dock is pairwise; nest is infrastructure only.
- [x] **Bee/hive absent** — contrast only in cookbook, not in product language.

---

## 13. Produced artifacts (repo)

| Output | Location |
|--------|----------|
| Charging nest layout | [docs/electric-ant-nest-design.md](./docs/electric-ant-nest-design.md) |
| Render / CAD prompts | [docs/render-prompts.md](./docs/render-prompts.md) |
| Vehicle schematic SVG | [assets/formic-1-side.svg](./assets/formic-1-side.svg) |
| Nest plan SVG | [assets/formic-nest-plan.svg](./assets/formic-nest-plan.svg) |
| City routing simulation | [simulations/city_routing/](./simulations/city_routing/) |
| Agent stack + tests | [formic_stack/](./formic_stack/) · [tests/](./tests/) |
| Narrative scene | [docs/narrative-bridge-closure.md](./docs/narrative-bridge-closure.md) |
| Project index | [README.md](./README.md) |
| 3D CAD / STEP | Export manually from §5–§7, §10 dimensions |

---

## 14. File purpose

This file is the **how-to-design** companion for a single **Formic-1** electric ant-car agent: philosophy, workflow, layout, sensors, swap geometry, styling rules, and generation prompts. Fleet behavior stays decentralized; hardware supports **local sense, trace, and act** only.
