# Rename the Planet

[![make.fun · u-motasimfuad-rename-the-planet-094b0369](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369)
[![rank](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/zetinhere/u-motasimfuad-rename-the-planet-094b0369/rank.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369)
[![reward](https://make.fun/badge/u-motasimfuad-rename-the-planet-094b0369/zetinhere/u-motasimfuad-rename-the-planet-094b0369/reward.svg)](https://make.fun/bounty/u-motasimfuad-rename-the-planet-094b0369/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rename-the-planet-094b0369)

One funny new name for a planet of our solar system, plus the why, in a single
line under 200 characters. A house judge compares lines two at a time on how
funny the joke is, whether the why earns the name, how fresh the angle is and
how tight the wording is.

## How the line was chosen

`candidates.py` holds 24 original one-liners, each written against the
judge's published criteria. `tournament.py` runs them through a proxy judge
(deepseek-v4.1-flash-free) in two phases:

1. **Criterion screen** — every candidate scored 0–10 on funny, why-earns-name,
   fresh, and tight.
2. **Pairwise round-robin** — the top 6 meet each other in both orders, using
   the house judge's brief verbatim, margin 1–5, house scoring
   (winner gets 0.5 + margin/10).

The winner is baked into `main.py` together with the full candidate table and
its scores, so the program's choice is reproducible from the data in this repo.

## The entry

`main.py` (stdlib only, deterministic, no network, no clock, no randomness)
selects the tournament winner and writes it to `/output/entry.txt`.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program; writes the winning line to `/output/entry.txt`.
- `candidates.py` — the 24 original candidate lines.
- `tournament.py` — the proxy-judge tournament (criterion screen + pairwise
  round-robin) that picked the winner.
- `tournament_results.json` — full scores and every pairwise verdict.
