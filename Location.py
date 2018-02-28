#!/usr/local/Cellar/python3
from pprint import pprint

import GameObject
from GameObject import GameObject
from Barrier import Barrier

reactionMap = {}



def second_room(location, player, command):
    print(command)
    result = ""
    if command[0] in location.baseMap: 
        if command[0] == "m":
            if command[0] == "n":
                location._barriers["s"]._open = False
                result = "The door slams shut behind you."
                print("yas")
        print(location.baseMap[command[0]](location) + result)
    else: return "error"

def first_room(location, player, command):
    if command[0] in location.baseMap: return location.baseMap[command[0]](location)

reactionMap["second_room"] = second_room
reactionMap["first_room"] = first_room

class Location(GameObject):

    def __init__(self, **kwargs): 
        super(Location, self).__init__(**kwargs)
        #baseMap = { "visit" : self.visit}

        self._connections = kwargs["connections"]
        self._barriers = {}
        self._react = reactionMap[kwargs["tag"]]
    
    def react(self, player, command): 
        return reactionMap[self._tag](self, player, command)


    def visit(self):
        if self._visited: return self._sDesc
        else: 
            self._visited = True
            return self._lDesc

    def give_barrier(self, barrier, direction):
        self._inventory.append(barrier._tag)
        self._barriers[direction] = barrier
        return self._connections[direction]

    def player_move(self, player, direction):
        '''
        if direction in self._connections:
            if direction in self._barriers:
                return self._barriers[direction].react(player, ["m", direction])

            return reactionMap[self._tag](player, self, direction)
        return "there's nothing but death that way" '''

    baseMap = { "m" : visit }
    _connections = None
    _barriers = None
    _visited = False

