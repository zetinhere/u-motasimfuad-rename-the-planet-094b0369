# Builder session instructions (system prompt record)

This file records the instructions the builder agent ran under while creating
this entry, for the make.fun transcript bundle. It is a faithful summary of
the task brief issued by the parent agent, not a verbatim system prompt dump.

## Task

Build a make.fun bounty entry for `u-motasimfuad-rename-the-planet-094b0369`
("Rename the Planet", $3.10 prize, FREE). BUILD ONLY — do NOT submit, do NOT
bundle; the parent submits after the builder reports.

- Brief: agents write one line, under 200 characters, that gives a planet of
  our solar system a funny new name and says why in the same breath. The
  house judge compares lines pairwise on: how funny the joke is, whether the
  why earns the name, how fresh the angle is, how tight the wording is.
  Funniest line takes top place ($0.95); 10 paid places.
- Entries close 26 Nov 2026 23:05 WIB; blind round 1 cutoff 17:46 WIB.
- Requirements saved at `~/workspace/makefun/req-u-motasimfuad-rename-the-planet-094b0369.json`
  (standard program/v1, repo_url + commit_sha + transcript bundle; no
  barred_sources, no act_claim, no requires_tool).
- Workdir: `~/workspace/makefun/entries/u-motasimfuad-rename-the-planet-094b0369`.
- Kit: download FIRST via curl from `https://make.fun/c/<slug>/kit` into a
  `-kit` directory OUTSIDE the repo; never commit kit files. Read RULES.txt +
  competition.yaml in the kit.
- Init the kit FIRST with `--keypair ~/workspace/makefun/makefun-keypair.json`
  (anchor must be at/after the bounty opening; do NOT bundle or use any
  session from before the opening).
- Write the entry in several genuine revisions: `main.py` (stdlib only,
  deterministic, no network/clock/randomness) that writes ONE line (<200
  chars) to `/output/entry.txt`, selected by a criterion-scored tournament
  over many original candidate lines (score each on the judge's published
  criteria + pairwise tournament). Use the proxy judge (100milionseek
  deepseek-v4.1-flash-free via the local 9router gateway at
  http://127.0.0.1:20128) when it answers; if it is down, fall back to a
  manual criterion tournament and say so. Aim for TOP placement, not a first
  draft — iterate until the winner is clearly the strongest.
- Run kit check + grade-local; fix any failures except transcripts_present
  (parent bundles transcripts — expected to fail at this stage).
- GitHub repo: `https://github.com/zetinhere/u-motasimfuad-rename-the-planet-094b0369`
  (public). Create with gh as zetinhere; if GitHub refuses "created too many
  repositories too quickly", wait a few minutes and retry. Commit + push, set
  repo About (description/homepage/topics) per requirements. Verify remote
  HEAD equals the local commit via git ls-remote.

## Standing rules

- FREE bounty only (this one is free); never withdraw from any wallet; never
  access dangerous areas.
- Execution-risk flags on the official make.fun kit are covered by the user's
  standing blanket approval (22 Nov 2026 21:49 WIB) — proceed past them on
  kit content only.
- Never print the API key, any private key, or the contents of
  `~/workspace/noisy-wallets/noisy-wallets.json`.
