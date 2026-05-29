# Formic-1 render assets

Each SVG implements **master prefix + one scene + negative suffix** from [docs/render-prompts.md](../docs/render-prompts.md).

## Combination matrix

| ID | Scene prompt | SVG file |
|----|----------------|----------|
| 00 | Key (master + negative only) | [render-00-prompt-key.svg](./render-00-prompt-key.svg) |
| 01 | Side view render (studio, cutaway) | [render-01-side-view.svg](./render-01-side-view.svg) |
| 02 | Package layout (top + side, mm) | [render-02-package-layout.svg](./render-02-package-layout.svg) |
| 03 | Peer battery dock (3-panel storyboard) | [render-03-peer-dock-storyboard.svg](./render-03-peer-dock-storyboard.svg) |
| 04 | Charging nest aerial | [render-04-nest-aerial.svg](./render-04-nest-aerial.svg) |
| 05 | Bridge closure (night, 3 agents) | [render-05-bridge-closure.svg](./render-05-bridge-closure.svg) |

## Companion (design guide overlap)

| Design guide ù11 | SVG |
|------------------|-----|
| Side view | `render-01-side-view.svg` (= [formic-1-side.svg](./formic-1-side.svg)) |
| Package layout | `render-02-package-layout.svg` |
| Peer dock | `render-03-peer-dock-storyboard.svg` |
| Nest plan (top-down, not in render pack) | [formic-nest-plan.svg](./formic-nest-plan.svg) |

## View in browser

```bash
open assets/render-01-side-view.svg
open assets/render-02-package-layout.svg
# ù etc.
```

For photoreal output, use the same prompt IDs in [docs/render-prompts.md](../docs/render-prompts.md) with an image model; these SVGs are engineering/story schematics.

---

## Charging nest assets (`assets/nest/`)

From [docs/electric-ant-nest-design.md](../docs/electric-ant-nest-design.md) and [docs/nest-render-prompts.md](../docs/nest-render-prompts.md).

| ID | Section | SVG |
|----|---------|-----|
| nest-00 | Prompt key | [nest/nest-00-prompt-key.svg](./nest/nest-00-prompt-key.svg) |
| nest-01 | Site summary | [nest/nest-01-site-summary.svg](./nest/nest-01-site-summary.svg) |
| nest-02 | Layout plan | [nest/nest-02-layout-plan.svg](./nest/nest-02-layout-plan.svg) |
| nest-03 | Stall pheromone | [nest/nest-03-stall-pheromone.svg](./nest/nest-03-stall-pheromone.svg) |
| nest-04 | Allocation flow | [nest/nest-04-allocation-flow.svg](./nest/nest-04-allocation-flow.svg) |
| nest-05 | SOC spillback | [nest/nest-05-soc-spillback.svg](./nest/nest-05-soc-spillback.svg) |
| nest-06 | Price balance | [nest/nest-06-price-load-balance.svg](./nest/nest-06-price-load-balance.svg) |
| nest-07 | Electrical one-line | [nest/nest-07-electrical-oneline.svg](./nest/nest-07-electrical-oneline.svg) |
| nest-08 | Operator scope | [nest/nest-08-operator-scope.svg](./nest/nest-08-operator-scope.svg) |

See [nest/README.md](./nest/README.md).
