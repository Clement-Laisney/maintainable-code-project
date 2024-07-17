from model import Weapon, Character, Monster
from view import View
from characters import CHARACTERS

MAX_PLAYERS = 4
MAX_MONSTERS = 5


class Controller:
    def __init__(self, view) -> None:
        # model
        self.characters: list = []
        self.players: dict = {}
        self.pnjs: list = []
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
                CHARACTERS,
            )
            if not character_abilities:
                return None
            self.characters.append(Character(**character_abilities))

    # def get_pnjs(self) -> None:
    #     while (len(self.characters) + len(self.pnjs)) < MAX_PLAYERS:
    #         pnj: dict = self.view.prompt_for_pnjs()
    #         if not pnj:
    #             return None
    #         self.pnjs.append(Character(**pnjs))

    # def get_monsters(self):
    #     while len(self.monsters) < MAX_MONSTERS:
    #         monster: dict = self.view.prompt_for_monsters()
    #         if not monster:
    #             return None
    #         self.monsters.append(Monster(**monster))

    # def start_game(self):
    #     self.queue = self.characters + self.pnjs + self.monsters
    #     for player in self.queue:
    #         player.action()

    def run(self) -> None:
        self.get_players()

        # self.view.display_players(self.characters)

        # self.get_pnjs()

        # self.get_monsters()

        # self.start_game()
        # for player in self.queue:
        #     self.view.show_actions()
