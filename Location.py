#!/usr/local/Cellar/python3
import json
import logging

import settings
from util import console_color

import GameObject
from GameObject import GameObject
from Barrier import Barrier

log = logging.getLogger('game.Location')

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

        log.info(console_color("green","New Location Created: {}".format(kwargs["tag"])))

        self._connections = kwargs["connections"]
        self._barriers = {}
        self._visited = False
         
    def __str__(self):
        return json.dumps(self.__dict__)

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