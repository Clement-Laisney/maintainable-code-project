from typing import Union


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
                f"\t\tArme 1: {choices[value]['weapon1']['name']}; "
                f"{choices[value]['weapon1']['desc']}\n"
            )
            print(
                f"\t\tArme 2: {choices[value]['weapon2']['name']}; "
                f"{choices[value]['weapon2']['desc']}\n"
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

    def prompt_difficulty(self):
        choice = int(
            input("\nChoisissez un niveau de difficulté entre 1 et 10 (defaut: 1): ")
            or 1
        )
        return choice
