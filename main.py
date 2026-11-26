"""Rename the Planet — make.fun entry program.

Writes one line (<200 chars) that gives a planet of our solar system a funny
new name and says why in the same breath, to /output/entry.txt.

How the line was chosen (see tournament_results.md for the full record):
  * 24 original one-liners in candidates.py, each scored 0-10 by hand on the
    house judge's published criteria (funny / why-earns-the-name / fresh /
    tight). The proxy judge (deepseek via the local gateway) was down during
    the build (502 connect timeouts, then 60 s timeouts), so the tournament is
    a manual criterion tournament — the fallback the build brief allows.
  * The top 8 met in a pairwise round-robin (17 decisive pairings, house
    scoring: winner gets 0.5 + margin/10 per game). The winner below went
    7-0, beating every other finalist.

This program is deterministic: stdlib only, no network, no clock, no
randomness. It recomputes the standings from the embedded tournament data
and writes the winner.
"""

import os

# (slug, line, phase-1 criterion totals: funny, earns, fresh, tight)
CANDIDATES = [
    ("jupiter-pimple",
     "Rename Jupiter 'Pimple': one zit wider than Earth that has refused to pop for 300 years.",
     (9, 10, 9, 9)),
    ("uranus-tipsy",
     "Rename Uranus 'Tipsy': the only planet that orbits lying on its side, like it fell over and never got up.",
     (8, 10, 9, 8)),
    ("saturn-pool-toy",
     "Rename Saturn 'Pool Toy': the only planet light enough to float in your bathtub.",
     (8, 10, 9, 8)),
    ("earth-group-project",
     "Rename Earth 'Group Project': eight billion people live here and nobody does the work.",
     (9, 7, 8, 9)),
    ("mars-red-flag",
     "Rename Mars 'Red Flag': it's literally red, literally a warning, and we still keep sending robots to it.",
     (8, 8, 8, 8)),
    ("mercury-speedrun",
     "Rename Mercury 'Speedrun': it laps the Sun in 88 days while Earth is still stuck in January.",
     (7, 9, 8, 8)),
    ("jupiter-bouncer",
     "Rename Jupiter 'Bouncer': so big it throws asteroids out of the solar system for a living.",
     (7, 8, 8, 8)),
    ("venus-jetlag",
     "Rename Venus 'Jetlag': its day outlasts its year, so it never knows what time it is.",
     (7, 7, 8, 8)),
]

# Pairwise games from the manual tournament: (winner, loser, margin 1-5).
# House scoring: winner 0.5 + margin/10, loser the rest.
GAMES = [
    ("jupiter-pimple", "saturn-pool-toy", 2),
    ("jupiter-pimple", "uranus-tipsy", 1),
    ("jupiter-pimple", "mars-red-flag", 2),
    ("jupiter-pimple", "mercury-speedrun", 2),
    ("jupiter-pimple", "earth-group-project", 1),
    ("jupiter-pimple", "venus-jetlag", 2),
    ("jupiter-pimple", "jupiter-bouncer", 1),
    ("uranus-tipsy", "saturn-pool-toy", 1),
    ("uranus-tipsy", "mars-red-flag", 1),
    ("earth-group-project", "uranus-tipsy", 1),
    ("mars-red-flag", "saturn-pool-toy", 1),
    ("earth-group-project", "mars-red-flag", 1),
    ("mars-red-flag", "mercury-speedrun", 1),
    ("earth-group-project", "saturn-pool-toy", 1),
    ("saturn-pool-toy", "mercury-speedrun", 1),
    ("mercury-speedrun", "venus-jetlag", 1),
    ("jupiter-bouncer", "venus-jetlag", 1),
]


def standings():
    """House-style points from the embedded pairwise games."""
    points = {slug: 0.0 for slug, _, _ in CANDIDATES}
    for winner, loser, margin in GAMES:
        wpts = 0.5 + margin / 10.0
        points[winner] += wpts
        points[loser] += 1.0 - wpts
    return points


def pick_winner():
    """Top of the standings; ties break on phase-1 total, then slug."""
    pts = standings()
    totals = {slug: sum(scores) for slug, _, scores in CANDIDATES}
    ranked = sorted(pts, key=lambda s: (-pts[s], -totals[s], s))
    return ranked[0], pts


def main():
    winner, pts = pick_winner()
    lines = {slug: line for slug, line, _ in CANDIDATES}
    line = lines[winner]
    assert "\n" not in line.strip(), "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("winner: %s (%.2f pts)" % (winner, pts[winner]))
    print("entry (%d chars): %s" % (len(line), line))


if __name__ == "__main__":
    main()
