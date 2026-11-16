# tiny-chess-01-entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/chengyuanpeng/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/chengyuanpeng/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python 3.13: a fixed-node-budget alpha-beta search with piece-square-table evaluation, MVV-LVA capture ordering and a capture-only quiescence search, written and tuned by an AI coding agent. It plays the make.fun house gauntlet through the trial env, one deterministic move at a time — no clock, no randomness, no model calls.

## Run it

```sh
# Start a trial env from the bounty kit, then point the engine at it:
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=0m4vwbr3&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
