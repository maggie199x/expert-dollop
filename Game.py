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
from Item import Item
from Parser import Parser

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
            "help": self.help,
            "quit": self.quit,
            "open": self.inclusive_action,
            "get" : self.inclusive_action,
            "move": self.player_action,
        }
        
        self.searchMap = {
            "open": self.inclusive_search,
        }

        # Mapping of possible inputs to commands
        

        # Initialize variables
        self.parser = Parser()

        self.running = True
        self.playerInput = []
        self.player = None
        self.locations = {}
        self.barriers = {}
        self.items = {}
        self.allObj = {}
        #self.initialize_objects()

    def command(self):

        inputText = ""
        while len(inputText) < 1:
            inputText = input("@> ")
        
        inputList = self.parser.parse_command(inputText)
        self.playerInput = inputList
        verb = inputList[0]
        if verb in self.reactionMap: 
            log.info(console_color("performing action {}".format(self.playerInput), color="blue"))
            print(self.reactionMap[verb]())
        else: 
            print('The Architect will be happy to help you. If you need assistance, say "help"')


    def inclusive_search(self, searchTerm):
        #searches for any item viewable by the player in the room
        # search room for matching objects
        result = []
        inventory = self.player._location.inventory
        #print(inventory)

        if searchTerm in inventory:
            for i in inventory[searchTerm]:

                result.append(i)

        return result

    def run(self):
        while(self.running):
            self.command()

    #is this still used?
    def player_action(self):
        return self.player.react(self.playerInput) 


    def exit_game(self):
        self._running = False

    def inclusive_action(self): 

        command = self.playerInput
        #print(command)
        if len(command) < 2:
            return command[0] + " what?"

        foundObjects = self.inclusive_search(command[1])
        if len(foundObjects) == 1:
            return self.allObj[foundObjects[0]].react(self.player, self.playerInput)
        elif len(foundObjects) > 1: return "Which '" + command[1] + "'?" 
        else: return "What is a '" + ' '.join(command[1]) + "'?"

    def quit(self):
        self.running = False
        return "quitting"

    def help(self):
        return "Welcome to the Tower, founded in D7A by The Architect. Current verbs: 'open, move'"

    ''' initializes all objects from GameObjects.json '''
    def initialize_objects(self):
        objects = json.load(open("GameObjects.json"))
        for location in objects["locations"]:
            self.locations[location] = Location(**(objects["locations"][location]))
            self.allObj[location] = self.locations[location]
        for barrier in objects["barriers"]:
            self.barriers[barrier] = Barrier(**(objects["barriers"][barrier]))
            #self.connect_barrier(self.barriers[barrier])
            self.allObj[barrier] = self.barriers[barrier]
        for item in objects["items"]:
            self.items[item] = Item(**(objects["items"][item]))
            self.allObj[item] = self.items[item]
        self.player = Player(self.locations, **(objects["player"]["player"]))

        self.assemble_barriers(self.barriers)
        self.assemble_inventories(self.items)
        return True

    ''' ASSEMBLERS MUST BE CALLED BEFORE GAME CAN COMMENCE '''
    def assemble_barriers(self, barDict): #first step
        for key in barDict:
            barrier = barDict[key]
            location = barrier._location
            for direction in barrier._connections:
                location = self.locations[location].give_barrier(barrier, direction) 

    def assemble_inventories(self, objDict): #second step
        for key in objDict:
            obj = objDict[key]
            self.allObj[obj._location].give_object(obj)
        '''
        for key in objDict:
            #inventory = self.allObj[key].inventory
            for tag in self.allObj[key].tagInventory:
                objDict[key].give_object(self.allObj[tag])
        '''

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

    print("-------------WELCOME HOME-------------")
    game = Game()
    game.initialize_objects()
    game.run()

main()

