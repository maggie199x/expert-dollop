#!/usr/local/Cellar/python3
import json
import logging
import settings
from util import console_color

from GameObject import GameObject

log = logging.getLogger('game.Barrier')

#TODO: Make a base react so that each object is not required to have unique interactions.

''' The barrier object class are objects which prevent player movement, or trigger events which happen when a player passes through
They are not in charge of the player moving to a new location. If a barrier is open, the player WILL be able to move into a new location
The barrier object simply decides if a reaction happens when the player enters the new location
IE. the player moves into a new room, and the door shuts behind him. '''


reactionMap = {}

def oak_door(barrier, player, command):
    if command[0] == "open":
        return barrier.open()


reactionMap["oak_door"] = oak_door

class Barrier(GameObject):
    def __init__(self, **kwargs): 
        log.info(console_color("New Barrier Created : {}".format(kwargs["tag"]), color="purple"))
        #print(kwargs["tag"])
        self._connections = kwargs["connections"]
        self._location = kwargs["location"]
        self._connectionNum = kwargs["connection_num"]
        if "open" in kwargs: self._open = kwargs["open"]

        super(Barrier, self).__init__(**kwargs)

    def __str__(self):
        return json.dumps(self.__dict__)

    def react(self, player, action):
        #print("react::" + self._tag)
        return reactionMap[self._tag](self, player, action)


    def open(self):
        #print("barrier::open")
        if self._open:
            return "That's already open."
        else: 
            self._open = True
            return "You open it."

    _open = False
    _connections = []
    _location = str
    _connectionNum = int