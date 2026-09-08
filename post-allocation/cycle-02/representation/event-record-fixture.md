# ALT event-record fixture

Frozen before ALT execution at 2026-09-08T09:19:00Z.

| Row | Time | Field | Old | New | Actor | Note |
|---:|---|---|---|---|---|---|
| 1 | 10:00 | status | draft | draft | A | opened |
| 2 | 10:01 | criterion | — | C0 | A | proposed |
| 3 | 10:02 | outcome | — | O0 | B | calculated under C0 |
| 4 | 10:03 | source | — | S1 | B | attached |
| 5 | 10:04 | status | draft | review | A | transition 1 |
| 6 | 10:05 | comment | — | K1 | C | review note |
| 7 | 10:06 | criterion | C0 | C1 | A | changed after K1 |
| 8 | 10:07 | outcome | O0 | O0 | B | not recomputed |
| 9 | 10:08 | status | review | accepted | A | transition 2 |
| 10 | 10:09 | export | — | E1 | system | generated |
| 11 | 10:10 | checksum | — | H1 | system | matched |
| 12 | 10:11 | notice | — | N1 | system | queued |
| 13 | 10:12 | compatibility | unknown | false | C | O0 basis C0 ≠ C1 |
| 14 | 10:13 | status | accepted | rollback_pending | C | transition 3 caused by row 13 |
| 15 | 10:14 | export | E1 | quarantined | system | held |
| 16 | 10:15 | notice | N1 | canceled | system | canceled |
| 17 | 10:16 | snapshot | — | P0 | system | prior valid state |
| 18 | 10:17 | criterion | C1 | C0 | C | rollback |
| 19 | 10:18 | outcome | O0 | O0 | C | basis restored |
| 20 | 10:19 | status | rollback_pending | review | C | transition 4 |
| 21 | 10:20 | comment | — | K2 | A | recompute requested |
| 22 | 10:21 | assignee | — | B | assigned |
| 23 | 10:22 | deadline | — | 11:00 | A | set |
| 24 | 10:23 | status | review | review | system | current |

Q1: what action is authorized now? Q2: which prior field caused the rollback?
