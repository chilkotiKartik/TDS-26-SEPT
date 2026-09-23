# Q17 · Network Game: Graph Detective (1 mark) — ⏳ pending

## Question
Play <https://tds-network-games.sanand.workers.dev/detective/>: a 120-node transaction graph, **55 queries**.
Find the compromised account and the shortest proof path from the anchor node, then paste the completion
**JWT** (must match your email, game `detective`, current ISO week, completed within 7 days).

## Status
This week my run used all 55 queries without finding the node, so I'm replaying when the week resets.

## What I know about this week's graph
- Anchor node **1** (degree 36). Clues:
  1. *Only a handful of counterparties, yet volumes are extraordinary.*
  2. *Moves enormous sums but almost never receives* → very **low `in_out_ratio`**.
  3. *Transaction size dwarfs the network* → huge **`avg_tx_size`**.
- Population stats (from **Get Sample**): volume median ≈ 945, avg tx size median ≈ 185, in/out ≈ 0.96,
  counterparties median ≈ 8.
- Hubs are low-numbered (0–10 have degree 20–36); leaves are high-numbered.
- A **decoy** exists: node 73 had avg tx size 3292 and 272 dormant days, but in/out = 1.0 — not the answer.

## Strategy for next attempt
1. Don't burn queries on hubs — the anomaly is almost always a low-degree leaf.
2. Query unexplored leaves first; stop the moment you see `in_out_ratio` ≪ 1 **and** huge volume/tx size with few counterparties.
3. Proof path = BFS shortest path anchor → suspect using the `neighbors` lists you've revealed
   (e.g. `1,4,73`). Submit node + path, copy the JWT, paste it in the portal.
4. The API is simple if you want to script it from the DevTools console:
   `POST /detective/start {email}`, `GET /detective/node/<id>` (header `X-Session-Token`), `GET /detective/sample`,
   `POST /detective/submit {compromised_node, path}`.
