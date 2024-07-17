class View:
    def prompt_for_player_name(self):
        name = input("tapez le nom du joueur: ")
        if not name:
            return None
        return name

    def prompt_for_character(self, player_name: str, choices: dict) -> dict:
        indexed_choices = {}

        print("\nVous pouvez choisir les personnages suivants:\n\n")
        for index, value in enumerate(choices):
            print(f"\t{index}: {value}\n")
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
            indexed_choices[index] = value

        choice = int(
            input(f"\nChoisissez le personnage qui sera joué par {player_name}: ")
        )

        return choices[indexed_choices[choice]]

    # def display_players(self, players):
    #     print("Voici le nom des joueurs:\n\n")
    #     for players
