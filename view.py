from typing import Union
from time import sleep


class View:
    def prompt_for_player_name(self):
        name = input("tapez le nom du joueur: ")
        if not name:
            return None
        return name

    def prompt_for_character(
        self, player_name: str, choices: dict
    ) -> Union[dict, None]:
        indexed_choices = {}

        print("\nVous pouvez choisir les personnages suivants:\n\n")
        for index, value in enumerate(choices):
            print(f"\t{index+1}: {value}\n")
            print(f"\t\tPV: {choices[value]['hit_points']}\n")
            print(f"\t\tArmure: {choices[value]['armor']}\n")
            print(f"\t\tCaractéristiques: {choices[value]['desc']}\n")
            print(
                f"\t\tArme 1: {choices[value]['weapon1'].name}; "
                f"{choices[value]['weapon1'].desc}\n"
            )
            print(
                f"\t\tArme 2: {choices[value]['weapon2'].name}; "
                f"{choices[value]['weapon2'].desc}\n"
            )
            indexed_choices[index + 1] = value

        choice = int(
            input(f"\nChoisissez le personnage qui sera joué par {player_name}: ") or 0
        )
        if choice == 0:
            return None

        return choices[indexed_choices[choice]]

    def display_players(self, players):
        print("\nVoici le nom des joueurs:\n\n")
        for player in players:
            print(f"\t- {players[player]} jouera {player}\n")
        sleep(3)

    def prompt_difficulty(self):
        choice = int(
            input("\nChoisissez un niveau de difficulté entre 1 et 3 (defaut: 1): ")
            or 1
        )
        return choice

    def display_monsters(self, monsters):
        print("\nVoici les monstres contre lesquels vous allez vous battre:\n\n")
        for monster in monsters:
            print(f"\t- {monster.name}, {monster.desc}\n")
        sleep(3)

    def display_initiative_order(self, queue):
        print("\nL'ordre est le suivant:\n\n")
        for index, character in enumerate(queue):
            print(f"\t{index+1} {character.name}\n")
        sleep(3)

    def prompt_target(self, available_target):
        print("\nVoici les cibles possibles:\n\n")
        for index, target in enumerate(available_target):
            print(f"\t{index+1} {target.name}: {target.hit_points} points de vie\n")
        choice = int(input("\nChoisissez une cible à attaquer: ") or 1)
        return available_target[choice - 1]

    def prompt_weapon(self, weapons):
        print("\nVoici les armes diponibles:\n\n")
        for index, weapon in enumerate(weapons):
            print(f"\t{index+1} {weapon.name} : {weapon.damage}, {weapon.desc}\n")
        choice = int(input("\nChoisissez une arme pour attaquer: ") or 1)
        return weapons[choice - 1]

    def display_damages(self, character, target, damages):
        print(f"\n{character.name} à infligé {damages} de dommages à {target.name}\n")
        sleep(3)

    def display_death(self, target):
        print(f"\n{target.name} est mort ! \n")
        sleep(3)

    def display_hit_failled(self):
        print("\nL'attaque n'à pas aboutie ...\n")
        sleep(3)

    def display_hit_points(self, character):
        print(f"\n{character.name} à {character.hit_points} points de vie.")
        sleep(3)

    def display_attack(self, character, target, weapon):
        print(f"\n{character.name} attaque {target.name} avec {weapon.name}")
        sleep(3)

    def display_winner(self, winner):
        if winner == "Monsters":
            print("\nLes monstres ont gagnés :( \n")
        else:
            print("\nVotre équipe à gagnée :) \n")
        sleep(3)
