import numpy as np


class Character:
    def __init__(
        self,
        name: str,
        hit_points: int,
        armor: int,
        weapon1: "Weapon",
        weapon2: "Weapon",
        desc: str,
    ) -> None:
        self.name = name
        self.hit_points = hit_points
        self.armor = armor
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.desc = desc

        self.is_alive = True

    def __str__(self) -> str:
        return (
            f"\n{self.name}:\n"
            f"{self.desc}\n\n"
            f"\t- Armor Class (AC): {self.armor}\n"
            f"\t- Hit Points (HP): {self.hit_points}\n"
            f"\t- weapon 1: {self.weapon1.name}\n"
            f"\t- weapon 2: {self.weapon2.name}\n"
        )

    def __repr__(self) -> str:
        return f"<Character: {self.name}>"

    def attack(self, other, weapon):
        damage_dice = weapon.damage
        damages = self.roll_damage(damage_dice)
        other.damage(damages)
        return damages

    def roll_damage(self, damage_dice):
        number_of_dice, value_of_dice = damage_dice.split("d")
        rolls = np.random.randint(
            1,
            int(value_of_dice) + 1,
            int(number_of_dice),
        )
        total_damage = np.sum(rolls)
        return total_damage

    def damage(self, damages):
        if self.hit_points > damages:
            self.hit_points -= damages
            return None
        self.hit_points = 0
        self.is_alive = False


class Weapon:
    def __init__(
        self,
        name: str,
        damage: str,
        category: str,
        desc: str,
    ) -> None:
        self.name = name
        self.damage = damage
        self.category = category
        self.desc = desc

    def __str__(self) -> str:
        return f"{self.name}: {self.damage} damage.\n{self.desc}\n"

    def __repr__(self) -> str:
        return f"<weapon: {self.name}>"


class Monster(Character):
    def __init__(
        self,
        name: str,
        hit_points: int,
        armor: int,
        weapon1: Weapon,
        weapon2: Weapon,
        difficulty: int,
        desc: str,
    ) -> None:
        super().__init__(name, hit_points, armor, weapon1, weapon2, desc)
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return f"<Monster: {self.name}>"
