from random import choices
from model import Character, Monster
from characters import CHARACTERS
from monsters import MONSTERS

MAX_PLAYERS = 4
MAX_MONSTERS = 5


class Controller:
    def __init__(self, view) -> None:
        # model
        self.playable_characters = CHARACTERS
        self.characters: list = []
        self.pnjs: list = []
        self.players: dict = {}

        self.dungeon_difficulty = 1
        self.monsters: list = []
        self.queue: list = []

        self.view = view

    def get_players(self) -> None:
        while len(self.characters) < MAX_PLAYERS:
            player = self.view.prompt_for_player_name()
            if not player:
                return None
            character_abilities = self.view.prompt_for_character(
                player,
                self.playable_characters,
            )
            if not character_abilities:
                return None
            character = Character(**character_abilities)
            self.characters.append(character)
            del self.playable_characters[character.name]
            self.players[character.name] = player

    def get_pnjs(self) -> None:
        while len(self.characters) + len(self.pnjs) < MAX_PLAYERS:
            pnj_number = len(self.pnjs) + 1
            character_abilities = self.view.prompt_for_character(
                f"bot{pnj_number}",
                self.playable_characters,
            )
            if not character_abilities:
                return None
            character = Character(**character_abilities)
            self.pnjs.append(character)
            del self.playable_characters[character.name]
            self.players[character.name] = f"bot{pnj_number}"

    def get_difficulty(self) -> None:
        self.dungeon_difficulty = self.view.prompt_difficulty()

    def select_monsters(self) -> None:
        monster_number = min(len(self.players) + 1, MAX_MONSTERS)
        available_monsters = [
            monster
            for monster in MONSTERS
            if (MONSTERS[monster]["difficulty"] <= self.dungeon_difficulty)
        ]
        choosed_monsters = choices(available_monsters, k=monster_number)

        for monster_name in choosed_monsters:
            monster_abilities = MONSTERS[monster_name]
            monster = Monster(**monster_abilities)
            self.monsters.append(monster)

    # def start_game(self):
    #     self.queue = self.characters + self.pnjs + self.monsters
    #     for player in self.queue:
    #         player.action()

    def run(self) -> None:
        self.get_players()

        self.get_pnjs()

        self.view.display_players(self.players)

        self.get_difficulty()

        self.select_monsters()

        self.view.display_monsters(self.monsters)

        # self.start_game()
        # for player in self.queue:
        #     self.view.show_actions()
