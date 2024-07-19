from model import Weapon
from weapons import WEAPONS

MONSTERS = {
    "Dragonnet de cuivre": {
        "name": "Dragonnet de cuivre",
        "hit_points": 22,
        "armor": 12,
        "weapon1": Weapon(**WEAPONS["Morsure de dragon"]),
        "weapon2": Weapon(**WEAPONS["Souffle d'acide"]),
        "difficulty": 1,
        "desc": "OUUH le mignon petit dragon !",
    },
    "Ours brun": {
        "name": "Ours brun",
        "hit_points": 34,
        "armor": 7,
        "weapon1": Weapon(**WEAPONS["Griffe de bête sauvage"]),
        "weapon2": Weapon(**WEAPONS["Morsure de bête sauvage"]),
        "difficulty": 1,
        "desc": "Oh mais tiens voilà quelqu'un ! Petit ours brun...",
    },
    "Loup sanguinaire": {
        "name": "Loup sanguinaire",
        "hit_points": 37,
        "armor": 10,
        "weapon1": Weapon(**WEAPONS["Morsure de bête sauvage"]),
        "weapon2": Weapon(**WEAPONS["Morsure de bête sauvage"]),
        "difficulty": 1,
        "desc": "AHOUUUUUUUH !",
    },
    "Goule": {
        "name": "Goule",
        "hit_points": 22,
        "armor": 8,
        "weapon1": Weapon(**WEAPONS["Griffe de goule"]),
        "weapon2": Weapon(**WEAPONS["Morsure de goule"]),
        "difficulty": 1,
        "desc": "De la chaire humaine fraiche !!!",
    },
    "Spectre": {
        "name": "Spectre",
        "hit_points": 22,
        "armor": 8,
        "weapon1": Weapon(**WEAPONS["Absorbtion de vie"]),
        "weapon2": Weapon(**WEAPONS["Absorbtion de vie"]),
        "difficulty": 1,
        "desc": "BoUuhOUuhH",
    },
    "Ankheg": {
        "name": "Ankheg",
        "hit_points": 39,
        "armor": 10,
        "weapon1": Weapon(**WEAPONS["Morsure de bête sauvage"]),
        "weapon2": Weapon(**WEAPONS["Vaporisation d'acide"]),
        "difficulty": 2,
        "desc": "Pourquoi acheter un marteau piqueur quand on a un Ankheg ?",
    },
    "Griffon": {
        "name": "Griffon",
        "hit_points": 59,
        "armor": 8,
        "weapon1": Weapon(**WEAPONS["Coup de bec"]),
        "weapon2": Weapon(**WEAPONS["Griffe de bête sauvage"]),
        "difficulty": 2,
        "desc": "Buck !",
    },
    "Mimique": {
        "name": "Mimique",
        "hit_points": 58,
        "armor": 8,
        "weapon1": Weapon(**WEAPONS["Morsure de mimique"]),
        "weapon2": Weapon(**WEAPONS["Pseudopode"]),
        "difficulty": 2,
        "desc": "Je ne vois pas ce qui vous fais dire que je suis un monstre !",
    },
    "Merrow": {
        "name": "Merrow",
        "hit_points": 45,
        "armor": 9,
        "weapon1": Weapon(**WEAPONS["Morsure de merrow"]),
        "weapon2": Weapon(**WEAPONS["Harpon"]),
        "difficulty": 2,
        "desc": "Elle à morphlé la Petite sirène !",
    },
    "Doppelganger": {
        "name": "Doppelganger",
        "hit_points": 52,
        "armor": 10,
        "weapon1": Weapon(**WEAPONS["Coup"]),
        "weapon2": Weapon(**WEAPONS["Attaque surprise"]),
        "difficulty": 3,
        "desc": "Je suis un humain ! (enfin je crois ?!)",
    },
    "Basilic": {
        "name": "Basilic",
        "hit_points": 52,
        "armor": 11,
        "weapon1": Weapon(**WEAPONS["Morsure de basilic"]),
        "weapon2": Weapon(**WEAPONS["Morsure de basilic"]),
        "difficulty": 3,
        "desc": "1, 2, 3, Soleil !",
    },
    "Vétéran": {
        "name": "Vétéran",
        "hit_points": 58,
        "armor": 13,
        "weapon1": Weapon(**WEAPONS["Epée longue"]),
        "weapon2": Weapon(**WEAPONS["Arbalète lourde"]),
        "difficulty": 3,
        "desc": "My name is Bond... James bond !",
    },
}
