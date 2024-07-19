from random import choices, choice, shuffle, randint
from model import Character, Monster
from characters import CHARACTERS
from monsters import MONSTERS

MAX_PLAYERS = 4
MAX_MONSTERS = 5


class Controller:
    def __init__(self, view) -> None:
        self.playable_characters = CHARACTERS
        self.players: dict = {}

        self.characters: list = []
        self.pnjs: list = []
        self.monsters: list = []

        self.dungeon_difficulty = 1
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

    def roll_initiative(self) -> None:
        self.queue = self.characters + self.pnjs + self.monsters
        shuffle(self.queue)

    def start_dungeon(self):
        is_running = True
        while is_running:
            for character in self.queue:
                if (len(self.characters) + len(self.pnjs) > 0) and len(
                    self.monsters
                ) > 0:
                    if character.is_alive:
                        self.view.display_hit_points(character)
                        if character in self.characters:
                            target = self.view.prompt_target(self.monsters)
                            weapon = self.view.prompt_weapon(
                                [character.weapon1, character.weapon2]
                            )

                        elif character in self.pnjs:
                            target = self.choose_target(self.monsters)
                            weapon = self.choose_weapon(
                                [character.weapon1, character.weapon2]
                            )

                        else:
                            target = self.choose_target(self.characters + self.pnjs)
                            weapon = self.choose_weapon(
                                [character.weapon1, character.weapon2]
                            )

                        self.view.display_attack(character, target, weapon)
                        is_hit = self.roll_attack(target)
                        if is_hit:
                            damages = character.attack(target, weapon)
                            self.view.display_damages(character, target, damages)
                            is_still_alive = target.is_alive
                            if not is_still_alive:
                                if target in self.characters:
                                    self.characters.remove(target)
                                elif target in self.pnjs:
                                    self.pnjs.remove(target)
                                else:
                                    self.monsters.remove(target)
                                self.view.display_death(target)
                        else:
                            self.view.display_hit_failled()
                else:
                    is_running = False

    def choose_target(self, available_target):
        target = choice(available_target)
        return target

    def choose_weapon(self, weapons):
        weapon = choice(weapons)
        return weapon

    def roll_attack(self, target):
        armor = target.armor
        dice = randint(1, 21)
        return dice > armor

    def winner(self, heroes, monsters):
        if len(heroes) == 0:
            return "Monsters"
        else:
            return "Heroes"

    def run(self) -> None:
        self.get_players()

        self.get_pnjs()

        self.view.display_players(self.players)

        self.get_difficulty()

        self.select_monsters()

        self.view.display_monsters(self.monsters)

        self.roll_initiative()

        self.view.display_initiative_order(self.queue)

        self.start_dungeon()

        winner = self.winner(self.characters + self.pnjs, self.monsters)
        self.view.display_winner(winner)
