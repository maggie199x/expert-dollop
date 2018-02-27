#!/usr/local/Cellar/python3
from pprint import pprint

import GameObject
from GameObject import GameObject
from Barrier import Barrier

reactionMap = {}

def second_room(player, location, direction):
    location._barriers["s"].close()

def first_room(barriers):
    pass

reactionMap["second_room"] = second_room
reactionMap["first_room"] = first_room

class Location(GameObject):

    def __init__(self, **kwargs): 
        super(Location, self).__init__(**kwargs)
        self._connections = kwargs["connections"]
        self._barriers = {}
         

    def give_barrier(self, barrier, direction):
        self._inventory.append(barrier._tag)
        self._barriers[direction] = barrier
        return self._connections[direction]

    def player_move(self, player, direction):
        if direction in self._connections:
            if direction in self._barriers:
                return self._barriers[direction].react(player, ["m", direction])

            return reactionMap[self._tag](player, self, direction)
        return "there's nothing but death that way"

    _connections = None
    _barriers = None
    _visited = False

