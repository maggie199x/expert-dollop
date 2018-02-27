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
                self._allObj[barrier] = self._barriers[barrier]


            self._player = Player( self._locations, **(allObj["player"]["player"]))
            for barrier in self._barriers:
                self._connect_barrier(self._barriers[barrier])
        

    def command(self):
        self._command = input("@> ").lower().split()
        if self._command[0] in self._Player_action_queue: self._player_action()
        if self._command[0] in self._reactionMap:
            print(self._reactionMap[self._command[0]]())

    def _connect_barrier(self, barrier):
        location = barrier._location
        for direction in barrier._connections:
            location = self._locations[location].give_barrier(barrier, direction)

    def run(self):
        while(self._running):
            self.command()

    def _player_action(self):
        return self._player.react(self._command)

    def _inclusive_action(self): 
        foundObj = self._search(self._command[1])
        if foundObj: return foundObj.react(self._player, self._command)



    def _search(self, tag):
        if (tag in self._player._inventory) or (tag in self._player._location._inventory):
            return self._allObj[tag]
        return None


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

    _allObj = {}
    _locations = {}
    _barriers = {}
    #need to figure out reactionMap
    _moveAlias = ["go", "move"]

def main():
        print(platform.python_version())
        game = Game()
        game.run()

main()

