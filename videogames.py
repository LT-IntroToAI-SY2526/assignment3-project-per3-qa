#database of popular videogames that were released from the years 1990-2020
from typing import List, Tuple

games_db: List[Tuple[str, str, int, List[str]]] = [
    (
    "super mario world",   # the videogame title
    "nintendo",            # the publisher
    1990,                  # the release year
    [                      # the list of developers
        "shigeru miyamoto",
        "katsuya eguchi hideki konno",
        "toshihiko nakago",
        "shigefumi hino",
        "koji kondo",
    ],
), 
(
    "mega man 3",   # the videogame title
    "capcom",            # the publisher
    1990,                  # the release year
    [                      # the list of developers
        "masayoshi kurokawa",
        "tokuro fujiwara",
        "masayoshi kurosawa",
        "yoshinori takenaka",
        "tadashi kuwana",
    ],
), 
(
    "mortal kombat ii",   # the videogame title
    "midway games",       # the publisher
    1993,                 # the release year
    [                     # the list of developers
        "ed boon",
        "john tobias",
    ],
),

(
    "donkey kong country 2",   # the videogame title
    "nintendo",                # the publisher
    1995,                      # the release year
    [                          # the list of developers
        "tim stamper",
        "chris stamper",
        "david wise",
        "steve mayles",
    ],
),

(
    "final fantasy vii",
    "square",
    1997,
    [
        "hironobu sakaguchi",
        "yoshinori kitase",
        "tetsuya nomura",
        "nobuo uematsu",
    ],
),

(
    "the sims",
    "electronic arts",
    2000,
    [
        "will wright",
        "lucy bradshaw",
        "rodi swanson",
    ],
),

(
    "call of duty",
    "activision",
    2003,
    [
        "infinity ward",
        "vince zampella",
        "grant collier",
    ],
),

(
    "shadow of the colossus",
    "sony computer entertainment",
    2005,
    [
        "fumito ueda",
        "kenji kaido",
        "kow otani",
    ],
),

(
    "portal",
    "valve",
    2007,
    [
        "kim swift",
        "erik wolpaw",
        "chet faliszek",
        "gabe newell",
    ],
),

(
    "red dead redemption",
    "rockstar games",
    2010,
    [
        "dan houser",
        "sam houser",
        "josh bass",
        "rob nelson",
    ],
),

(
    "the last of us",
    "sony computer entertainment",
    2013,
    [
        "neil druckmann",
        "bruce straley",
        "gustavo santaolalla",
    ],
),

(
    "the witcher 3: wild hunt",
    "cd projekt red",
    2015,
    [
        "konrad tomaszkiewicz",
        "mateusz kanik",
        "marcin blacha",
        "mikolaj stachowiak",
    ],
),

(
    "the legend of zelda: breath of the wild",
    "nintendo",
    2017,
    [
        "hidemaro fujibayashi",
        "eiji aonuma",
        "takuhiro dohta",
        "hajime wakai",
    ],
),

(
    "cyberpunk 2077"
    "cd projekt red",
    2020,
    [
        "adam badowski",
        "konrad tomaszkiewicz",
        "gabriel amatangelo",
    ]
 )
]