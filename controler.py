from random import choices, choice, shuffle, randint
from model import Character, Monster, Weapon
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
        """Retrieve the player name and ask the player to choose his character."""

        while len(self.characters) < MAX_PLAYERS:
            player = self.view.prompt_for_player_name()
            if not player:
                return None

            # prompt_for_character returns a dictionnary with character properties
            character_properties = self.view.prompt_for_character(
                player,
                self.playable_characters,
            )
            if not character_properties:
                return None

            character = Character(**character_properties)
            self.characters.append(character)

            # delete the character from the list of available characters
            del self.playable_characters[character.name]

            # map the name of the character to the player name
            self.players[character.name] = player

    def get_pnjs(self) -> None:
        while len(self.characters) + len(self.pnjs) < MAX_PLAYERS:
            # attribute a number to a pnj (ie: first = 1 etc...)
            pnj_number = len(self.pnjs) + 1

            # prompt_for_character returns a dictionnary with properties
            character_properties = self.view.prompt_for_character(
                f"bot #{pnj_number}",
                self.playable_characters,
            )
            if not character_properties:
                return None

            character = Character(**character_properties)
            self.pnjs.append(character)

            # delete the character from the list of available characters
            del self.playable_characters[character.name]

            # map the name of the character to the bot name
            self.players[character.name] = f"bot #{pnj_number}"

    def get_difficulty(self) -> None:
        """Retrieve the difficulty of the dungeon"""
        self.dungeon_difficulty = self.view.prompt_difficulty()

    def select_monsters(self) -> None:
        """Choose and Create monster objects"""
        # Adapt the number of monsters with the number of players
        monster_number = min(len(self.players) + 1, MAX_MONSTERS)

        # Retrieve monsters with appropriate difficulty level
        available_monsters = [
            monster
            for monster in MONSTERS
            if (MONSTERS[monster]["difficulty"] <= self.dungeon_difficulty)
        ]

        choosed_monsters = choices(available_monsters, k=monster_number)

        # Create monster instances
        for monster_name in choosed_monsters:
            monster_properties = MONSTERS[monster_name]
            monster = Monster(**monster_properties)
            self.monsters.append(monster)

    def roll_initiative(self) -> None:
        """Draws the combat order"""
        self.queue = self.characters + self.pnjs + self.monsters
        shuffle(self.queue)

    def start_dungeon(self) -> None:
        """Start the round per round combat while monsters or players/pnjs not dead"""
        is_running = True
        while is_running:
            for character in self.queue:
                # If at least 1 monster and 1 player/pnj
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

                            # If dead remove it from the list of alive monsters/players/pnj
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

    def choose_target(self, available_target: list["Character"]) -> "Character":
        """Draws a Monster or Player/PNJ to target

        Args:
            available_target (list[Character]): A list of possible objects to target

        Returns:
            Character: A Character object
        """
        target = choice(available_target)
        return target

    def choose_weapon(self, weapons: list["Weapon"]) -> "Weapon":
        """Draws a weapon to attack with

        Args:
            weapons (list[Weapon]): A list of possible weapons objects to choose

        Returns:
            Weapon: A Weapon object
        """
        weapon = choice(weapons)
        return weapon

    def roll_attack(self, target: "Character") -> bool:
        """Rolls a 20-faced dice and compare it to the armor class of the target

        Args:
            target (Character): The Character object of the target

        Returns:
            bool: True if the dice result > target armor class
        """
        armor = target.armor
        dice = randint(1, 21)
        return dice > armor

    def winner(self, heroes: list["Character"], monsters: list["Character"]) -> str:
        """Get the winner

        Args:
            heroes (list[Character]): The list of Players and PNJ Character objects alive
            monsters (list[Character]): The list of Monster objects alive

        Returns:
            str: "Monsters or "Heroes"
        """
        if len(heroes) == 0:
            return "Monsters"
        elif len(monsters) == 0:
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
