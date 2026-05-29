# Formic-1 — Image & CAD Prompt Pack

Copy **master prefix** + one scene + **negative suffix** into your image model or CAD assistant.

## Master prefix

```text
You are designing a fleet of electric road vehicles that coordinate like ants, not bees.
Rules: no central AI assigning every move; identical local logic per vehicle; coordination via digital pheromones that decay; failure tolerant; electric-first (SOC, charging, kWh); explain with simple rules not opaque global optimization.
Vehicle: Formic-1 urban BEV logistics van, 4.2m x 1.8m x 1.85m, matte white, orange bumper accents, modular cab on skid, battery cassette under cargo, front sensor pods on faired pillars (antenna arc), rear CCS port.
```

## Negative suffix (always append)

```text
Do NOT: central fleet brain, queen vehicle, synchronized swarm thinking, hex-hive branding, diesel exhaust, insect monster truck, waggle-dance metaphor, glowing hive mind core.
```

---

## 1. Side view render

```text
[MASTER PREFIX]
Side view of Formic-1 electric urban delivery van, low profile cab-over, modular cab on flat skid, matte white, orange bumper accents. Wide front sensor pods on two faired pillars—not insect legs. Cutaway showing underbody battery cassette. Rear charge port. City street ground line. Photorealistic studio lighting.
[NEGATIVE SUFFIX]
```

## 2. Package layout (engineering diagram)

```text
[MASTER PREFIX]
Technical line art: top view and side view labeled diagram. Zones: deformable front, cab L/R, 4.2 m³ cargo, coupling face driver side, battery cassette under floor, LiDAR and camera positions, swap rails. White background, dimension callouts in mm.
[NEGATIVE SUFFIX]
```

## 3. Peer battery dock (storyboard)

```text
[MASTER PREFIX]
Three-panel instructional storyboard: two identical Formic-1 vans side by side in urban parking lane, coupling faces aligned, battery cassette transferring on rails. No lead truck, no drone overseer.
[NEGATIVE SUFFIX]
```

## 4. Charging nest aerial

```text
[MASTER PREFIX]
Aerial architectural rendering of electric logistics depot: 40 charging/swap stalls in two rows, buffer lane, cassette storage, matte industrial aesthetic, orange safety markings. No hexagon hive architecture, no central control tower labeled queen.
[NEGATIVE SUFFIX]
```

## 5. Bridge closure scene (mood)

```text
[MASTER PREFIX]
Grounded sci-fi: three white electric delivery vans at night city intersection, road closed sign, subtle UI glow on windscreen only. Distributed individuality—vehicles not formation-flying. Wet asphalt reflections.
[NEGATIVE SUFFIX]
```

---

## CAD export checklist

- Use dimensions from [electric-ant-car-design-guide.md](../electric-ant-car-design-guide.md) §10
- Coupling face 1,200 mm wide, cassette 1,800 × 1,400 × 220 mm
- Export STEP from Onshape/Fusion after locking skid rail pattern
