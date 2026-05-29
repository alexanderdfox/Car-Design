# Formic-1 — How the Car Should Look (Ant-Inspired Appearance Prompt)

Use this as a **single copy-paste prompt** for image models, industrial designers, or CAD assistants. It describes **look and form only**—not fleet software. Every unit is an ordinary colony member; there is no queen trim, hive branding, or insect costume.

**Constraint:**

> Electric urban logistics vehicle; ant-inspired **function**, not bug cosplay; matte utility aesthetic; decentralized colony member (identical to all siblings).

---

## Master appearance prompt (copy all)

```text
Design the exterior and proportions of the Formic-1, an electric urban delivery vehicle whose FORM is inspired by ant biology translated to road hardware—not a literal insect, not a bee hive product.

ANT → VEHICLE TRANSLATION (visible in the design):
- Segmented body: read as three honest modules on one low flat skid—cab module, cargo box, underbody battery cassette—separated by subtle panel gaps and rail lines, not a single melted blob.
- Low, wide stance: cab-over forward control, overall height about 1.85 m, length 4.2 m, width 1.8 m; ground clearance for real streets (~160 mm); wide track, stable center of gravity.
- Antennae: a wide front sensor arc—two faired rectangular pillars (matte black) flanking the windshield with LiDAR/camera housings; reads as sensing "antennae," never as whiskers, legs, or mandibles.
- Carrying: large side roller cargo door, flat load floor visible in cutaway; front deformable zone clearly ahead of sensors for repair without recalibrating perception.
- Colony member: every vehicle identical—no "command" variant, no gold leader accents, no larger executive cab, no crown or central glowing core on the roof.
- Nest return: rear CCS charge port, optional underbody pantograph pocket suggested only at rear; orange safety accents on bumpers and door edges, not on a fake stinger.

ELECTRIC (must read as BEV):
- No exhaust, no grille pretending to cool ICE; clean flat front under sensors; underbody battery cassette visible in side cutaway or transparent floor graphic; quiet utility van proportions.
- Matte white or light gray body panels; flat industrial surfaces; small agent ID QR on rear door; rear LED strip for charge state only (amber/green), not synchronized swarm light shows.

MATERIALS AND LIGHT:
- Photoreal or studio product render; soft overhead light; optional 3/4 rear inset; urban ground line or neutral gray floor.
- Surfaces: matte paint, black sensor fairings, orange bumper highlights (#f97316 range), zinc-gray cassette and skid hints.

OPTIONAL DETAIL (peer dock, do not dominate):
- Midship coupling face on one cargo side—flush panel, alignment pins—suggests two units can briefly dock; no convoy leader truck in frame.

MOOD: grounded near-future logistics, European urban scale, trustworthy utility—NOT sci-fi hive cathedral, NOT cute insect face, NOT hex honeycomb grille or honey-yellow branding.
```

---

## Negative prompt (append always)

```text
Do NOT: literal ant or beetle face on grille, six legs, exoskeleton spines, giant mandibles, wings, stinger tail, hex honeycomb hive grille, glowing brain dome, queen limousine variant, gold leader paint, synchronized LED ring implying one mind, diesel exhaust pipes, monster truck insect, bee yellow-black stripes, waggle-dance branding, "swarm intelligence" marketing graphics, formation-flying convoy with a lead vehicle.
```

---

## Short one-shot (tight budgets)

```text
Side view, Formic-1 electric delivery van: low cab-over white matte body, orange bumpers, modular cab + cargo + underbody swap battery, twin black sensor pods on front pillars like antennae, rear CCS port, 4.2 m urban van, studio lighting. Ant-inspired segmentation and sensing, NOT insect cosplay, NOT hex hive aesthetic, NOT queen leader truck.
```

---

## What “ant-like” means here (designer cheat sheet)

| Ant idea | What viewers should see on the car |
|----------|-----------------------------------|
| Segment | Cab / cargo / pack are visually distinct modules on one skid |
| Low profile | Cab-over, low roof, wide wheelbase |
| Antennae | Front sensor pillars + arc, black fairings |
| Worker | Same body as every other unit—no royal trim |
| Carry load | Cargo box dominates aft of cab |
| Return to nest | Rear charging interface, depot-scale not heroic |

| Ant idea | What to avoid |
|----------|----------------|
| Queen | Larger cab, gold trim, "command" mast |
| Hive | Hex patterns, unified glowing core |
| Swarm mind | Matching LED pulses on many vans in one image |
| Bug cosplay | Eyes, legs, mandibles, chitin texture |

---

## Reference dimensions (keep proportions credible)

| Dimension | Target |
|-----------|--------|
| Overall length | 4,200 mm |
| Width | 1,800 mm |
| Height (unloaded) | 1,850 mm |
| Wheelbase | 2,700 mm |
| Cargo volume | ~4.2 m³ |
| Sensor pillar height | ~1.35 m camera band; bumper LiDAR ~400 mm |

---

## SVG assets (from this prompt)

| Prompt element | SVG |
|----------------|-----|
| Key (show vs avoid) | [appearance-00-key.svg](../assets/appearance/appearance-00-key.svg) |
| Master side studio | [appearance-01-side-studio.svg](../assets/appearance/appearance-01-side-studio.svg) |
| Segmented modules | [appearance-02-segmented-modules.svg](../assets/appearance/appearance-02-segmented-modules.svg) |
| Front antenna arc | [appearance-03-antenna-arc-front.svg](../assets/appearance/appearance-03-antenna-arc-front.svg) |
| 3/4 rear studio | [appearance-04-three-quarter.svg](../assets/appearance/appearance-04-three-quarter.svg) |
| BEV + cargo carry | [appearance-05-bev-front-carry.svg](../assets/appearance/appearance-05-bev-front-carry.svg) |
| Colony members | [appearance-06-colony-member.svg](../assets/appearance/appearance-06-colony-member.svg) |
| Rear nest interface | [appearance-07-rear-nest.svg](../assets/appearance/appearance-07-rear-nest.svg) |
| Materials / mood | [appearance-08-materials-mood.svg](../assets/appearance/appearance-08-materials-mood.svg) |

Full matrix: [assets/appearance/README.md](../assets/appearance/README.md)

```bash
open assets/appearance/appearance-01-side-studio.svg
```

## Related assets and docs

- Engineering layouts: [electric-ant-car-design-guide.md](../electric-ant-car-design-guide.md)
- Side render schematic: [assets/render-01-side-view.svg](../assets/render-01-side-view.svg)
- Package diagram: [assets/render-02-package-layout.svg](../assets/render-02-package-layout.svg)
- Prompt cookbook: [electric-ant-cars-prompt-guide.md](../electric-ant-cars-prompt-guide.md)
