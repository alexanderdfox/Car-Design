# City routing — local agent pseudocode

From prompt cookbook §2. **No central router.**

## Pheromone update (shared map, TTL)

```
every minute OR each tick with factor λ:
  for each edge e in route_pheromone:
    route_pheromone[e] *= λ    // λ = 0.95 typical (5% loss per minute)

on successful transit (agent at cell A → B):
  route_pheromone[edge(A,B)] += Δ    // Δ = 0.1–1.0

on congestion sense:
  congestion[cell] += bump
  congestion[cell] *= λ over time
```

## Local agent (every 5 s)

```
function AGENT_TICK(agent, map, goal):
  map.evaporate()
  neighbors = grid_neighbors(agent.cell)
  ε = scout_epsilon if low_pheromone_confidence else forager_epsilon

  if random() < ε:
    next = random_choice(neighbors)
  else:
    costs = []
    for n in neighbors:
      if map.hazard[n]: costs.append(INF)
      else:
        costs.append(
          distance(agent.cell, n)
          + congestion[n]
          - route_pheromone[edge(agent.cell, n)]
          + energy_cost(agent.soc, kWh_per_km)
        )
    next = softmax_pick(neighbors, -costs)

  success = (next == goal)
  map.deposit_route(agent.cell, next, success)
  agent.cell = next
  agent.soc -= kWh_per_km * hop_km / pack_kWh
```

## Energy utility

```
energy_cost = α * (1 / max(SOC, 0.05)) + β * kWh_per_km * hop_km
if SOC < SOC_min: cost += nest_seek_penalty unless edge toward free stall trace
```

## Metrics

- Delivery latency (ticks to goal)
- kWh/km fleet aggregate
- Congestion integral on cells
- Compare to **bee mode**: `dijkstra(agent.cell, goal)` every tick — rejected design

Run: `python3 simulations/city_routing/simulate.py`
