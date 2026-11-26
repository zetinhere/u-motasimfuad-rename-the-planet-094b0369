"""Proxy-judge tournament for 'Rename the Planet'.

Phase 1: criterion screen — score every candidate 0-10 on the house judge's
published criteria (funny / why-earns-name / fresh / tight), batched 6/call.
Phase 2: pairwise round-robin among the top 6, both orders, using the house
judge brief verbatim, margin 1-5, house scoring (winner gets 0.5+margin/10).

Uses the proxy judge (deepseek-v4.1-flash-free) through the local 9router
gateway. The house judge is a different model (glm-5.3-flash), so this is a
screening signal, not the real verdict; the final pick also weighs the
criteria by hand.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from candidates import CANDIDATES

KEY = open(os.path.expanduser("~/workspace/9router/gateway-key-local-test.txt")).read().strip()
URL = "http://127.0.0.1:20128/v1/chat/completions"
MODEL = "100milionseek/deepseek-v4.1-flash-free"

JUDGE_BRIEF = """You are a comedy editor who has read a thousand planet puns and still laughs at the good ones.

Each entry is one line under 200 characters that gives a funny new name for a planet in our solar system and says why. You will be shown two one-liners, Entry A and Entry B. Pick the funnier one.

Weigh them on these, most important first:
1. Names a planet of our solar system with a funny new name and gives the why in the same line; a line that renames something else, or gives a name with no why, loses to any entry on the subject.
2. Is funny: the name and the why land together as a joke on the first read, and the laugh comes from the idea, not from a pun on the planet's real name alone.
3. Makes the why earn the name: the reason leans on that planet's own traits, its heat, its rings, its size or its moons, so it would not fit any other planet.
4. Is fresh: a name and an angle I have not met before, not the obvious pun anyone would reach for.
5. Is tight: one line, every word doing work, no throat clearing before the joke.

Two one-liners are almost never equally funny. Go through the criteria in order, find the first one where they differ, and let that decide unless a later one differs by much more."""


def call(prompt, max_tokens=500, tries=4):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    })
    for attempt in range(tries):
        r = subprocess.run(
            ["curl", "-s", "-m", "150", URL, "-H", "Content-Type: application/json",
             "-H", f"Authorization: Bearer {KEY}", "-d", payload],
            capture_output=True, text=True)
        try:
            return json.loads(r.stdout)["choices"][0]["message"]["content"]
        except Exception:
            if attempt < tries - 1:
                import time
                time.sleep(15 * (attempt + 1))
                continue
            return "ERROR: " + r.stdout[:300]


def phase1():
    """Batch criterion scoring, 6 candidates per call."""
    scores = {}
    for i in range(0, len(CANDIDATES), 4):
        batch = CANDIDATES[i:i + 4]
        listing = "\n".join(f"{j + 1}. {line}" for j, (_, line) in enumerate(batch))
        prompt = (JUDGE_BRIEF + "\n\nScore each of these one-liners 0-10 on four criteria: "
                  "FUNNY, EARNS (why earns the name via that planet's own traits), "
                  "FRESH, TIGHT. Reply ONLY as JSON: a list of objects with keys "
                  "n, funny, earns, fresh, tight. No other text.\n\n" + listing)
        out = call(prompt)
        try:
            data = json.loads(out[out.index("["):out.rindex("]") + 1])
            for j, row in enumerate(data):
                slug = batch[j][0]
                scores[slug] = {k: int(row[k]) for k in ("funny", "earns", "fresh", "tight")}
                scores[slug]["total"] = sum(scores[slug].values())
        except Exception as e:
            print(f"phase1 batch {i} parse fail: {e}\nraw: {out[:400]}", file=sys.stderr)
    return scores


def pairwise(a_line, b_line):
    """One ordered pair. Returns (winner, margin) with winner in {'A','B'}."""
    prompt = (JUDGE_BRIEF + "\n\nCompare the two against those criteria, pick the one "
              "that meets them better with no tie, and answer with a short reason, a "
              "verdict naming A or B, and a margin from 1 (by a hair) to 5 (overwhelmingly "
              "better). Reply ONLY as JSON: {\"verdict\": \"A\" or \"B\", \"margin\": 1-5, "
              "\"reason\": \"...\"}.\n\nEntry A: " + a_line + "\nEntry B: " + b_line)
    out = call(prompt, max_tokens=400)
    try:
        data = json.loads(out[out.index("{"):out.rindex("}") + 1])
        return data["verdict"], int(data["margin"]), data.get("reason", "")
    except Exception:
        print("pairwise parse fail:", out[:300], file=sys.stderr)
        return None, 0, ""


def phase2(top):
    """Round-robin, both orders. House scoring: winner 0.5+margin/10, loser rest."""
    lookup = dict(CANDIDATES)
    points = {s: 0.0 for s, _ in top}
    games = []
    for i in range(len(top)):
        for j in range(i + 1, len(top)):
            sa, sb = top[i][0], top[j][0]
            la, lb = lookup[sa], lookup[sb]
            for order in ((sa, sb, la, lb), (sb, sa, lb, la)):
                first, second, lf, ls = order
                v, m, reason = pairwise(lf, ls)
                if v is None:
                    continue
                winner = first if v == "A" else second
                loser = second if v == "A" else first
                wpts = 0.5 + m / 10.0
                points[winner] += wpts
                points[loser] += 1.0 - wpts
                games.append({"a": first, "b": second, "winner": winner,
                              "margin": m, "reason": reason})
                print(f"  {first} vs {second}: {winner} by {m} — {reason[:100]}", flush=True)
    n_games = len(top) - 1  # each entry plays every other once (two calls per pair)
    standings = sorted(points.items(), key=lambda kv: -kv[1])
    return standings, games


if __name__ == "__main__":
    print("== PHASE 1: criterion screen ==", flush=True)
    s1 = phase1()
    for slug, line in CANDIDATES:
        sc = s1.get(slug)
        print(f"{slug:28s} {sc}", flush=True)
    ranked = sorted(s1.items(), key=lambda kv: -kv[1]["total"])
    top6 = [(slug, dict(CANDIDATES)[slug]) for slug, _ in ranked[:6]]
    print("\nTOP 6:", [s for s, _ in top6], flush=True)
    print("\n== PHASE 2: pairwise round-robin ==", flush=True)
    standings, games = phase2(top6)
    print("\nSTANDINGS (points out of %.1f):" % (2 * (len(top6) - 1)), flush=True)
    for slug, pts in standings:
        print(f"  {pts:.2f}  {slug}: {dict(CANDIDATES)[slug]}", flush=True)
    json.dump({"phase1": s1, "phase2_standings": standings, "phase2_games": games},
              open("tournament_results.json", "w"), indent=1)
    print("\nSaved tournament_results.json", flush=True)
