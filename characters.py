from model import Weapon
from weapons import WEAPONS

CHARACTERS = {
    "Ilona": {
        "name": "Ilona",
        "hit_points": 10,
        "armor": 14,
        "desc": "Barde, Demi-elfe",
        "weapon1": Weapon(**WEAPONS["Dague"]),
        "weapon2": Weapon(**WEAPONS["Murmures Dissonants"]),
    },
    "Urmora": {
        "name": "Urmora",
        "hit_points": 14,
        "armor": 18,
        "desc": "Guerrière, Naine",
        "weapon1": Weapon(**WEAPONS["Marteau léger"]),
        "weapon2": Weapon(**WEAPONS["Arbalète"]),
    },
    "Karad": {
        "name": "Karad",
        "hit_points": 9,
        "armor": 16,
        "desc": "Moine, Humain",
        "weapon1": Weapon(**WEAPONS["Marteau léger"]),
        "weapon2": Weapon(**WEAPONS["Marteau de guerre"]),
    },
    "Peren": {
        "name": "Peren",
        "hit_points": 8,
        "armor": 13,
        "desc": "Occultiste, Elf",
        "weapon1": Weapon(**WEAPONS["Dague"]),
        "weapon2": Weapon(**WEAPONS["Décharge Occulte"]),
    },
    "Aloïs": {
        "name": "Aloïs",
        "hit_points": 9,
        "armor": 14,
        "desc": "Roublard, Humain",
        "weapon1": Weapon(**WEAPONS["Dague"]),
        "weapon2": Weapon(**WEAPONS["Rapière"]),
    },
    "Hommet": {
        "name": "Hommet",
        "hit_points": 9,
        "armor": 12,
        "desc": "Magicien, Humain",
        "weapon1": Weapon(**WEAPONS["Dague"]),
        "weapon2": Weapon(**WEAPONS["Contact Glacial"]),
    },
}
