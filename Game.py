#!/usr/local/Cellar/python3
import json
import platform

import Player, Location
from Player import Player
from Location import Location
from Barrier import Barrier

class Game(object):
    def __init__(self):
        self._Player_action_queue = ["m"]
        self._reactionMap = {
            "exit" : self._quit,
            "quit" : self._quit
        }
        objDict = {}
        try:
            with open("GameObjects.json", 'r') as f:
                allObj = json.load(f)
                for location in allObj["locations"]:
                    #print(location)
                    self._locations[location] = Location(**(allObj["locations"][location]))

                for barrier in allObj["barriers"]:
                    self._barriers[barrier] = Barrier(**(allObj["barriers"][barrier]))
                    #self._barriers[barrier].connect()


                self._player = Player( self._locations, **(allObj["player"]["player"]))
                for barrier in self._barriers:
                    #print(barrier)
                    self._connect_barrier(self._barriers[barrier])
        except Exception as e:
            print("Error parsing GameObjects.json: %s" % e)
            self._running = False
        

    def command(self):
        self._command = input("@> ").lower().split()
        #print(self._command)
        if self._command[0] in self._Player_action_queue: self._player_action()
        if self._command[0] in self._reactionMap:
            self._reactionMap[self._command[0]]()

    def _connect_barrier(self, barrier):
        #print(barrier._connections)
        #print(barrier._location)
        #print(barrier._connectionNum)
        location = barrier._location
        for direction in barrier._connections:
            #print(i)
            location = self._locations[location].give_barrier(barrier, direction)

        #test print
        for location in self._locations: 
            print(location)
            print(self._locations[location]._barriers)

    def run(self):
        while(self._running):
            self.command()

    def _player_action(self):
        #print("Game::player_action")
        return self._player.react(self._command)

    def _inclusive_action(self): 
        pass
        #print("Game::inclusive_action")


    def exit_game(self):
        self._running = False

    def player(): #return player
        return
    def running(): #return running
        return
    def test(self):
        print("test is successful")
        return

    def _quit(self):
        self._running = False
        print("quitting")


    #members
    _reactionMap = {}
    _command = None 
    _running = True
    _player = None
    _parser = None

    _locations = {}
    _barriers = {}
    #need to figure out reactionMap
    _moveAlias = ["go", "move"]

def main():
        print(platform.python_version())
        game = Game()
        game.run()

main()

