# Formic-1 — AI Image Generator Prompt Pack

Copy-paste prompts for **Midjourney**, **DALL·E**, **Stable Diffusion**, **Adobe Firefly**, **Ideogram**, etc. Optimized for **one vehicle**, photoreal product / automotive studio looks.

**Rule:** Ant inspiration = **segmented utility van + sensor pillars**. Never literal bugs, never bee-hive branding, never a “queen” lead truck.

**Reference schematics:** [assets/appearance/](../assets/appearance/) · [assets/render-01-side-view.svg](../assets/render-01-side-view.svg)

---

## 1. Universal block (paste into every generation)

### Positive core (required)

```text
Formic-1 electric urban delivery van, ant-inspired industrial design without insect cosplay, low cab-over forward control van, length 4.2 meters, matte white body, orange safety bumper accents, three visible body modules on flat skid platform, cab module, large cargo box, underbody battery swap cassette, twin matte-black rectangular sensor pods on front pillars like antennae, wide front perception arc, LiDAR bumper, no exhaust pipe, no ICE grille, rear CCS fast charge port, European urban logistics vehicle, photorealistic automotive studio render, soft overhead lighting, neutral gray floor, sharp focus, 8k detail
```

### Negative (required — use your tool’s negative field or append “--no”)

```text
insect face, beetle eyes, mandibles, ant legs, six legs, wings, stinger tail, exoskeleton texture, hexagon honeycomb grille, hive mind, glowing brain dome on roof, queen limousine, gold chrome leader trim, bee yellow black stripes, diesel exhaust, fake radiator grille, monster truck, cyberpunk hive cathedral, synchronized swarm LED ring, convoy with lead command truck, waggle dance, cute cartoon bug, low poly, blurry, watermark, text logo
```

---

## 2. Ready-made shots (positive + shot line)

Paste **Universal positive core** first, then add **one shot line**. Keep the **negative** block.

### A. Hero side profile (default)

**Shot line:**

```text
perfect side profile view, full vehicle in frame, subtle cutaway showing underbody battery pack, visible panel gaps between cab and cargo modules, urban studio backdrop
```

**Suggested aspect ratio:** 16:9 or 3:2

---

### B. Three-quarter front (marketing hero)

**Shot line:**

```text
three-quarter front view, 25 degree angle, emphasis on twin black sensor pillars and windshield, clean flat electric front with no grille, confident wide stance, shallow depth of field
```

**Suggested aspect ratio:** 4:3 or 16:9

---

### C. Three-quarter rear

**Shot line:**

```text
three-quarter rear view, rear CCS charging flap, small QR code sticker on rear door, thin green amber charge status LED strip, orange rear bumper accent, optional subtle pantograph pocket underbody hint
```

**Suggested aspect ratio:** 4:3

---

### D. Front elevation (sensor “antennae”)

**Shot line:**

```text
straight front view, symmetric composition, two faired sensor pillars flanking windshield, dashed perception arc implied, flat white front apron, professional automotive photography
```

**Suggested aspect ratio:** 1:1 or 4:5

---

### E. Rear elevation (nest return)

**Shot line:**

```text
straight rear view, roller cargo doors, CCS port centered, industrial utility aesthetic, no decorative stinger shape, depot-ready electric van
```

**Suggested aspect ratio:** 4:3

---

### F. Urban context (grounded sci-fi)

**Shot line:**

```text
Formic-1 parked on wet European city street at dusk, single vehicle only, subtle windshield reflection, realistic scale pedestrians distant, grounded near-future logistics mood, not formation flying swarm
```

**Suggested aspect ratio:** 16:9

---

### G. Cutaway / technical beauty

**Shot line:**

```text
side cutaway technical illustration hybrid, ghosted cargo volume 4.2 cubic meters, visible swap battery cassette on rails, deformable crumple zone ahead of sensors, clean white background, product design editorial
```

**Suggested aspect ratio:** 16:9

---

## 3. One-line mega-prompts (token-limited tools)

### Side studio

```text
Photoreal side studio shot of Formic-1 electric delivery van, matte white, orange bumpers, modular cab and cargo segments, underbody swap battery, twin black front sensor pods like antennae, no exhaust, no insect cosplay, no hex hive grille, soft lighting --neg insect mandibles hex hive queen truck exhaust
```

### 3/4 front

```text
Photoreal 3/4 front of low electric cab-over delivery van Formic-1, white matte panels, black sensor pillars, orange accents, BEV flat front, urban logistics, studio render --neg bug face honeycomb hive diesel grille swarm
```

---

## 4. Style modifiers (pick 1–2, do not stack all)

| Modifier | Paste fragment |
|----------|----------------|
| Photoreal product | `photorealistic, automotive studio, Phase One camera look` |
| Design clay + render | `design clay model transitioned to hyperreal paint, design studio` |
| Soft EV brand | `clean sustainable mobility aesthetic, calm premium utility` |
| Technical editorial | `Wired magazine product photography, minimal background` |
| Overcast outdoor | `overcast soft daylight, realistic shadows, 35mm lens` |

Avoid: `cyberpunk`, `honeycomb`, `biomechanical insect`, `steampunk`, `dieselpunk`.

---

## 5. Tool-specific tips

### Midjourney

- Put the **shot line** and **style modifier** in the main prompt; put **negative concepts** after `--no` (comma-separated).
- Example suffix: `--ar 16:9 --style raw --v 6`
- Use `--sref` with [appearance-01-side-studio.svg](../assets/appearance/appearance-01-side-studio.svg) only if your workflow supports SVG/style reference.

### Stable Diffusion / ComfyUI

- **Positive:** Universal core + shot line + style modifier.
- **Negative:** Section 1 negative block (full list).
- CFG 6–7, DPM++ 2M Karras or equivalent; resolution 1216×832 or 1024×1024 for side profile.

### DALL·E / ChatGPT Images

- Use **one shot** (A–G) per message; keep under ~400 words.
- Explicitly say: `not a literal ant, not a bee, not a monster truck`.

### Adobe Firefly

- Lead with `photorealistic electric delivery van` then ant-structure phrases (`segmented modules`, `sensor pillars`).
- Use Structure/Reference image upload with `appearance-01-side-studio.svg` if available.

---

## 6. Consistency checklist (after generation)

- [ ] Reads as **electric** (no exhaust, no ICE grille)
- [ ] **Three modules** visible: cab, cargo, underbody pack
- [ ] **Two black sensor pillars** — not legs or mandibles
- [ ] **Matte white + orange** bumpers/doors — not bee yellow/black
- [ ] **One van** or identical siblings — no gold queen leader
- [ ] No hex hive graphics or glowing “brain” on roof

Regenerate with stronger **negative** if any box fails.

---

## 7. Iteration prompts (fix common failures)

| Problem | Add to positive | Strengthen negative |
|---------|-----------------|---------------------|
| Looks like a bug | `industrial van, road vehicle, wheels` | `insect, beetle, mandibles, legs` |
| Hive / sci-fi temple | `plain industrial depot, matte paint` | `hexagon hive, cathedral, honeycomb` |
| ICE truck | `battery electric, no exhaust` | `grille, radiator, exhaust pipe` |
| Queen / leader | `standard fleet vehicle, identical unit` | `gold, limousine, crown, larger cab` |
| Too futuristic | `2028 European urban logistics, realistic` | `cyberpunk, flying, glowing core` |

---

## Related docs

- [formic-ant-appearance-prompt.md](./formic-ant-appearance-prompt.md) — design rationale
- [electric-ant-car-design-guide.md](../electric-ant-car-design-guide.md) — dimensions and engineering
- [render-prompts.md](./render-prompts.md) — additional scene prompts (dock, bridge, nest aerial)
