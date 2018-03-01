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

#set up logging
log = logging.getLogger('game.Game')

class Game:
    """
        The Game.
    """
    def __init__(self):
       
        log.info(console_color("new Game Started", color='black', background='red'))

        # Mapping of input commands to functions
        self.reactionMap = {
            "quit": self.quit,
            "open": self.inclusive_action,
            "move": self.player_action,
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
        self.player_input = True
        self.player = None
        self.locations = {"test" : "test2"}
        self.barriers = {}
        #self.initialize_objects()


    def connect_barrier(self, barrier):
        location = barrier._location
        for direction in barrier._connections:
            location = self.locations[location].give_barrier(barrier, direction) 

        ## Initialize the Game (loading screen?)
        #self._initialize_objects()
        #clear_screen()

    def run(self):
        while(self.running):
            self.command()

    #is this still used?
    def player_action(self):
        return self.player.react(self.player_input) 


    def exit_game(self):
        self._running = False

    #is this still used?
    def inclusive_action(self): 
        command = self.player_input
        if len(command) < 2:
            return command[0] + " what?"

        foundObj = self.searchMap[command[0]](command[1:])
        if foundObj: return foundObj.react(self.player, self.player_input)
        else: return "What is a " + command[1:]

    def command(self):
        input_text = input("@> ").lower().split()
        base_command = self.dealias_command(input_text[0])
        input_params = input_text[1:]
        self.player_input = [base_command] + input_params

        if base_command in self.reactionMap: 
            log.info(console_color("performing action {}".format(self.player_input), color="blue"))
            print(self.reactionMap[base_command]())

        else: 
            print("not sure what you mean fam")

        #elif base_command in self.reactionMap: print(self._reactionMap[self._command[0]]())

    def dealias_command(self, command):
        # If the command is not in the alias list, returns the command
        return self.aliasMap.get(command, command)

    def search(self, tag):
        if (tag in self._player._inventory) or (tag in self._player._location._inventory):
            return self._allObj[tag]
        return None

    def quit(self):
        self._running = False
        return "quitting"

    def initialize_objects(self):
        #try:
        objects = json.load(open("GameObjects.json"))
        for location in objects["locations"]:
            self.locations[location] = Location(**(objects["locations"][location]))
        for barrier in objects["barriers"]:
            self.barriers[barrier] = Barrier(**(objects["barriers"][barrier]))
            self.connect_barrier(self.barriers[barrier])
        #except Exception as e:
            #log.error("Parsing Error: {}".format(e))
            #raise SyntaxError("Error parsing GameObjects.json")
        #try: 
        self.player = Player(self.locations, **(objects["player"]["player"]))
        #except Exception as e:
        #   log.error("Error loading GameObjects: {}".format(e))
        #  raise SyntaxError("Error loading objects from GameObjects.json")
        return True

    #members
    """
    _reactionMap = {}
    _command = None 
    _running = True
    _parser = None

    _allObj = {}
    _locations = {}
    _barriers = {}
    #need to figure out reactionMap
    _moveAlias = ["go", "move"] """

def main():
        print(platform.python_version())
        game = Game()
        game.initialize_objects()
        game.run()

main()

"""
def command(self):
self._command = input("@> ").lower().split()

if self._command[0] in self._Player_action_queue: print(self._player_action())
elif self._command[0] in self._reactionMap: print(self._reactionMap[self._command[0]]())
else: print("not sure what you mean fam")"""

"""
self._Player_action_queue = ["m"]
self._reactionMap = {
"exit" : self._quit,
"quit" : self._quit,
"open" : self._inclusive_action
}
objDict = {}
with open("GameObjects.json", 'r') as f:
allObj = json.load(f)
for location in allObj["locations"]:
#print(location)
self._locations[location] = Location(**(allObj["locations"][location]))
self._allObj[location] = self._locations[location]

for barrier in allObj["barriers"]:
self._barriers[barrier] = Barrier(**(allObj["barriers"][barrier]))
self._allObj[barrier] = self._barriers[barrier] """


"""
self._player = Player( self._locations, **(allObj["player"]["player"]))
for barrier in self._barriers:
self._connect_barrier(self._barriers[barrier]) """

'''
for location in objects["locations"]:
self.locations[location] = Location(**(objects["locations"][location]))
for barrier in objects["barriers"]:
self.barriers[barrier] = Barrier(**(objects["barriers"][barrier]))
for barrier in self.barriers:
self._connect_barrier(self.barriers[barrier])'''

