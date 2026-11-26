"""Candidate one-liners for 'Rename the Planet' (u-motasimfuad-rename-the-planet-094b0369).

Every line: names a planet of our solar system, gives it a funny new name,
and says why in the same breath. All under 200 characters. Written fresh
here; the obvious puns (Uranus cheap jokes, Mars bar, Lord of the Rings,
Pluto-is-not-a-planet) were deliberately avoided because the judge's brief
says the laugh must come from the IDEA, not a pun on the planet's real name,
and the why must lean on that planet's own traits.
"""

CANDIDATES = [
    ("jupiter-pimple",
     "Rename Jupiter 'Pimple': one zit wider than Earth that has refused to pop for 300 years."),
    ("saturn-pool-toy",
     "Rename Saturn 'Pool Toy': the only planet light enough to float in your bathtub."),
    ("venus-jetlag",
     "Rename Venus 'Jetlag': its day outlasts its year, so it never knows what time it is."),
    ("uranus-tipsy",
     "Rename Uranus 'Tipsy': the only planet that orbits lying on its side, like it fell over and never got up."),
    ("mars-red-flag",
     "Rename Mars 'Red Flag': it's literally red, literally a warning, and we still keep sending robots to it."),
    ("neptune-windbag",
     "Rename Neptune 'Windbag': home to the fastest winds in the solar system, and it never shuts up about it."),
    ("mercury-microwave",
     "Rename Mercury 'Microwave': scorching by day, frozen by night - it can't pick a temperature."),
    ("earth-group-project",
     "Rename Earth 'Group Project': eight billion people live here and nobody does the work."),
    ("jupiter-hoarder",
     "Rename Jupiter 'Hoarder': 95 moons and counting - it physically cannot stop collecting."),
    ("venus-pressure-cooker",
     "Rename Venus 'Pressure Cooker': the air crushes like the deep sea and the rain is battery acid."),
    ("saturn-hula-hoop",
     "Rename Saturn 'Hula Hoop': the only planet wearing a ring it can never take off."),
    ("mars-dust-bunny",
     "Rename Mars 'Dust Bunny': one storm and the whole planet vanishes under the furniture."),
    ("mercury-speedrun",
     "Rename Mercury 'Speedrun': it laps the Sun in 88 days while Earth is still stuck in January."),
    ("venus-rewind",
     "Rename Venus 'Rewind': the only planet that spins backwards, like it's trying to undo its day."),
    ("saturn-disappearing-act",
     "Rename Saturn 'Disappearing Act': its rings are raining into the planet and will vanish within 100 million years."),
    ("mercury-hot-and-cold",
     "Rename Mercury 'Hot and Cold': 430 degrees by day, minus 180 by night - the solar system's most dramatic ex."),
    ("venus-sauna",
     "Rename Venus 'Sauna': 465 degrees under a permanent cloud blanket - the hottest room in the solar system."),
    ("jupiter-bouncer",
     "Rename Jupiter 'Bouncer': so big it throws asteroids out of the solar system for a living."),
    ("neptune-long-distance",
     "Rename Neptune 'Long-Distance Relationship': sunlight takes four hours to reach it, so every conversation lags."),
    ("earth-comment-section",
     "Rename Earth 'Comment Section': the only planet where eight billion people argue about everything, all at once."),
    ("uranus-sideways",
     "Rename Uranus 'Sideways': it rolls around the Sun on its side because sitting up straight was too much effort."),
    ("mars-backup-plan",
     "Rename Mars 'The Backup Plan': a freezing desert with almost no air, and it's still humanity's Plan B."),
    ("jupiter-never-logs-off",
     "Rename Jupiter 'The Storm That Never Logs Off': its red spot has raged for 300 years without a single day off."),
    ("saturn-halo",
     "Rename Saturn 'Halo': it wears a ring of ice around its waist and acts like it's not showing off."),
]

if __name__ == "__main__":
    for slug, line in CANDIDATES:
        print(f"{len(line):3d}  {slug}: {line}")
    bad = [(s, l) for s, l in CANDIDATES if not (1 <= len(l) <= 199)]
    print("over-limit:", bad)
