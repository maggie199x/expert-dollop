#!/usr/local/Cellar/python3
import argparse
import json
import platform
import logging

import settings
from util import console_color

from Player import Player
from Location import Location
from Barrier import Barrier

# Set up logging
log = logging.getLogger('game.Game')

class Game:
    """
        The Game.
    """
    def __init__(self):

        log.info(console_color("New Game Started", color="blue", background="lightgrey"))

        # Mapping of input commands to functions
        self.reactionMap = {
            "quit": self._quit,
            "open": self._inclusive_action
        }

        # Mapping of possible inputs to commands
        self.aliasMap = {
            "e":    "quit",
            "exit": "quit",
            "q":    "quit",
            "go":   "move",
            "m":    "move",
            "o":    "open",
        }

        self._command = None
        self.running = True
        self.parser = None
        self.playerActionQueue = ["m"]

        self.player = None
        self.locations = {}
        self.barriers = {}
        self._initialize_objects()

    def command(self):
        input_text = input("@> ").lower().split()
        base_command = self.dealias_command(input_text[0])
        input_params = input_text[1:]
        self._command = [base_command] + input_params

        if self._command[0] in self.playerActionQueue:
            self._player_action()
        if self._command[0] in self.reactionMap:
            print(self.reactionMap[self._command[0]]())

    def dealias_command(self, command):
        # If the command is not in the alias list, returns the command
        return self.aliasMap.get(command, command)

    def exit_game(self):
        self.running = False

    def player(self):
        # return player
        return self.player

    def run(self):
        while(self.running):
            self.command()

    def running(self):
        # return running
        return self.running

    def test(self):
        print("test is successful")


    def _connect_barrier(self, barrier):
        location = barrier._location
        for direction in barrier._connections:
            location = self.locations[location].give_barrier(barrier, direction)



    def _inclusive_action(self):
        foundObj = self._search(self.command[1])
        if foundObj:
            return foundObj.react(self.player, self.command)

    def _initialize_objects(self):
        try:
            objects = json.load(open("GameObjects.json"))
        except Exception as e:
            log.error("Parsing Error: {}".format(e))
            raise SyntaxError("Error parsing GameObjects.json")
        try:
            for location in objects["locations"]:
                self.locations[location] = Location(**(objects["locations"][location]))
            for barrier in objects["barriers"]:
                self.barriers[barrier] = Barrier(**(objects["barriers"][barrier]))
            for barrier in self.barriers:
                self._connect_barrier(self.barriers[barrier])
            self.player = Player(self.locations, **(objects["player"]["player"]))
        except Exception as e:
            log.error("Error loading GameObjects: {}".format(e))
            raise SyntaxError("Error loading objects from GameObjects.json")

        return True

    def _player_action(self):
        return self.player.react(self.command)

    def _search(self, tag):
        if (tag in self.player._inventory) or (tag in self.player._location._inventory):
            return self._allObj[tag]
        return None

    def _quit(self):
        self.running = False
        print("quitting")


def main():
    # Set up logging for all modules
    logging.basicConfig(filename=settings.LOG_FILENAME,format=settings.LOG_FORMAT,level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console_log_formatter = logging.Formatter(settings.LOG_FORMAT)
    console.setFormatter(console_log_formatter)

    # Parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Enable Debug Mode")
    args = parser.parse_args()
    if args.debug:
        # Add console logging
        logging.getLogger('').addHandler(console)

    # Run the Game
    game = Game()
    game.run()


if __name__ == "__main__":
    # execute only if run as a script
    main()
