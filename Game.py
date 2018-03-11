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

#TODO: Get Comments up to date




class Game:
    """
        The Game.
    """
    def __init__(self):
        #test
        log.info(console_color("new Game Constructed", color='black', background='red'))

        # Mapping of input commands to functions
        self.reactionMap = {
            "help": self.help,
            "quit": self.quit,
            "open": self.inclusive_action,
            "get" : self.inclusive_action,

            "move": self.player_action,
            "inventory": self.player_action
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

    def command(self):
        log.info(console_color("command()", color="green"))

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
        log.info(console_color("inclusive_search()", color="green"))
        result = []
        inventory = self.allObj[self.player._location].inventory
        if searchTerm in inventory:
            for i in inventory[searchTerm]:
                result.append(i)

        return result

    def run(self):
        log.info(console_color("run()", color="green"))
        while(self.running):
            self.command()

    def player_action(self):
        log.info(console_color("player_action()", color="green"))
        return self.player.react(self.playerInput) 


    def exit_game(self):
        log.info(console_color("exit_game()", color="green"))
        self._running = False

    def inclusive_action(self): 
        log.info(console_color("inclusive_action()", color="green"))
        command = self.playerInput
        if len(command) < 2:
            return command[0] + " what?"
        foundObjects = self.inclusive_search(command[1])
        if len(foundObjects) == 1:
            return self.allObj[foundObjects[0]].react(self.player, self.playerInput)
        elif len(foundObjects) > 1: return "Which '" + command[1] + "'?" 
        else: return "What is a '" + command[1] + "'?"

    def quit(self):
        log.info(console_color("quit()", color="green"))
        self.running = False
        return "quitting\n----------------------------------------------"

    def help(self):
        log.info(console_color("help()", color="green"))
        return "Welcome to the Tower, founded in D7A by The Architect. Current verbs: 'open, move, get'"

    ''' initializes all objects from GameObjects.json '''
    def initialize_objects(self):
        log.info(console_color("Game::initialize_objects()", color="green"))
        args = {"GAME" : self}
        objects = json.load(open("GameObjects.json"))
        for location in objects["locations"]:
            z = objects["locations"][location].copy()
            z.update(args)
            self.locations[location] = Location(**z)
            self.allObj[location] = self.locations[location]
        for barrier in objects["barriers"]:
            z = objects["barriers"][barrier].copy()
            z.update(args)
            self.barriers[barrier] = Barrier(**z)
            self.allObj[barrier] = self.barriers[barrier]
        for item in objects["items"]:
            z = objects["items"][item].copy()
            z.update(args)
            self.items[item] = Item(**z)
            self.allObj[item] = self.items[item]
        z = objects["player"]["player"]
        z.update(args)
        self.player = Player(**z) 

        self.assemble_barriers()
        self.assemble_inventories(self.items)
        return True

    ''' ASSEMBLERS MUST BE CALLED BEFORE GAME CAN COMMENCE '''
    def assemble_barriers(self): #first step
        log.info(console_color("assemble_barriers()", color="green"))
        for key in self.barriers:
            barrier = self.barriers[key]
            location = barrier._location
            for direction in barrier._connections:
                location = self.locations[location].give_barrier(barrier, direction) 
            

    def assemble_inventories(self, objDict): #second step
        log.info(console_color("assemble_inventories()", color="green"))
        for key in objDict:
            obj = objDict[key]
            self.allObj[obj._location].give_object(obj)

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

    print(intro_art2)
    game = Game()
    game.initialize_objects()
    game.run()

intro_art2 = """
----------------------------------------------
    ██████╗ ███████╗██╗   ██╗██╗██╗         
    ██╔══██╗██╔════╝██║   ██║██║██║         
    ██║  ██║█████╗  ██║   ██║██║██║         
    ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║         
    ██████╔╝███████╗ ╚████╔╝ ██║███████╗    
    ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝    
████████╗ ██████╗ ██╗    ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║    ██║██╔════╝██╔══██╗
   ██║   ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
   ██║   ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝╚███╔███╔╝███████╗██║  ██║
   ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
    ███████╗████████╗ █████╗ ██████╗        
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗       
    ███████╗   ██║   ███████║██████╔╝       
    ╚════██║   ██║   ██╔══██║██╔══██╗       
    ███████║   ██║   ██║  ██║██║  ██║       
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝       
            Pre-Alpha V0.0.1
----------------------------------------------"""

main()


