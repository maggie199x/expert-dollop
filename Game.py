#!/usr/local/Cellar/python3
import argparse
import json
import platform
import logging

import settings
from util import clear_screen, console_color

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

        log.info(console_color("New Game Started", color="black", background="red"))

        # Mapping of input commands to functions
        self.reactionMap = {
            "quit": self._quit,
            "open": self._inclusive_action,
            "move": self._inclusive_action,
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

        # Initialize variables
        self.running = True
        self.player_input = None
        self.player = None
        self.locations = {}
        self.barriers = {}

        ## Initialize the Game (loading screen?)
        self._initialize_objects()
        #clear_screen()

    def run(self):
        while(self.running):
            self.command()

    def exit_game(self):
        self.running = False

    def command(self):
        input_text = input("@> ").lower().split()
        base_command = self.dealias_command(input_text[0])
        input_params = input_text[1:]
        self.player_input = [base_command] + input_params

        if base_command in self.reactionMap:
            log.info(console_color("Performing action {}".format(self.player_input), color="blue"))
            self.reactionMap[base_command]()

    def dealias_command(self, command):
        # If the command is not in the alias list, returns the command
        return self.aliasMap.get(command, command)

    ##############
    ## Accessors... we probably don't need any of this?
    ##############

    def player(self):
        # return player
        return self.player

    def running(self):
        # return running
        return self.running

    def test(self):
        print("test is successful")

    ##############
    ## Initialization Functions
    ##############

    def _connect_barrier(self, barrier):
        location = barrier._location
        for direction in barrier._connections:
            location = self.locations[location].give_barrier(barrier, direction)

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

    ##############
    ## Actions
    ##############

    def _inclusive_action(self):
        command = self.player_input
        if len(command) < 2:
            print("That action must have a target.")
            return False
        foundObj = self._search(command[1])
        if foundObj:
            return foundObj.react(self.player, self.command)
        else:
            print("Object {} not found.".format(command[1]))

    def _player_action(self):
        return self.player.react(self.player_input)

    def _search(self, tag):
        # Search player then location for tag
        if tag in self.player._inventory:
            return self.player._inventory[tag]
        elif tag in self.player._location._inventory:
            return self.player._location._inventory[tag]
        else:
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
