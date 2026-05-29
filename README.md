# Electric Ant Cars (Formic-1)

Decentralized **electric urban logistics vehicles** that coordinate like an ant colony—stigmergy on shared map traces, not a central hive controller.

## Repository map

| Path | Contents |
|------|----------|
| [electric-ant-cars-prompt-guide.md](./electric-ant-cars-prompt-guide.md) | Prompt cookbook |
| [electric-ant-car-design-guide.md](./electric-ant-car-design-guide.md) | Formic-1 vehicle design brief |
| [docs/formic-ant-appearance-prompt.md](./docs/formic-ant-appearance-prompt.md) | Ant-inspired **look** prompt (image/CAD) |
| [docs/ai-image-car-design-prompt.md](./docs/ai-image-car-design-prompt.md) | **AI image generator** copy-paste prompts |
| [assets/appearance/](./assets/appearance/) | Appearance SVGs `appearance-00` .. `appearance-08` |
| [docs/electric-ant-nest-design.md](./docs/electric-ant-nest-design.md) | 40-stall charging nest (infrastructure only) |
| [docs/nest-render-prompts.md](./docs/nest-render-prompts.md) | Nest image/CAD prompt pack |
| [assets/nest/](./assets/nest/) | Nest SVGs nest-00 .. nest-08 (all doc sections) |
| [docs/narrative-bridge-closure.md](./docs/narrative-bridge-closure.md) | Story: bridge closure, 3 agents |
| [docs/render-prompts.md](./docs/render-prompts.md) | Image/CAD prompt pack |
| [assets/README.md](./assets/README.md) | Render prompt → SVG matrix (00–05) |
| [assets/render-01-side-view.svg](./assets/render-01-side-view.svg) … `render-05` | All [render-prompts](./docs/render-prompts.md) scenes |
| [assets/formic-1-side.svg](./assets/formic-1-side.svg) | Legacy alias → see `render-01` |
| [assets/formic-nest-plan.svg](./assets/formic-nest-plan.svg) | Nest top-down plan (companion to `render-04`) |
| [formic_stack/](./formic_stack/) | Python agent stack (ROS2-style topics, no `/fleet/command`) |
| [simulations/city_routing/](./simulations/city_routing/) | 200-agent grid sim + pseudocode |
| [tests/](./tests/) | Evaporation + offline recovery tests |

## Quick start

```bash
cd /Users/alexanderfox/Desktop/Ants
python3 -m unittest discover -s tests -v
python3 simulations/city_routing/simulate.py
```

## Design constraint

> Electric vehicles; decentralized ant-colony coordination via environmental traces and local rules only—no central hive controller, no queen node, no broadcast hive-mind.

## Formic-1 snapshot

- BEV urban van, 4.2 × 1.8 m, 75 kWh swap cassette, ~220 km useful range
- Front sensor “antenna arc”; side coupling face for peer pack transfer
- Local behavior: sense → score → act → deposit pheromone

## What is intentionally not included

- **3D CAD / STEP** — export from Fusion/Onshape using dimension table in the design guide; use [render-prompts](./docs/render-prompts.md) for AI-assisted modeling
- **Bee mode in production** — only in simulation as a rejected baseline
- **`/fleet/command`** — banned in `formic_stack/topics.py`

## Quality checklist

- [x] Any one car can fail without fleet-wide crash
- [x] Coordination on map traces (pheromone, hazard, charger_claim)
- [x] SOC / kWh in routing utility
- [x] No master planner in ant stack
- [x] No hive/queen product language
