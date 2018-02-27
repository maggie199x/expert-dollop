#!/usr/local/Cellar/python3
import json
import logging

import settings
from util import console_color

from GameObject import GameObject

log = logging.getLogger('game.Barrier')

reactionMap = {}

def old_door(barrier, player, action):
    #print("old_door::reaction")
    #print(action)
    if action[0] == "m":
        if barrier._open:
            player._location = barrier._connections[action[1]]
            if player._location._visited: return player._location._sDesc
            else:
                player._location._sDesc
                return player._location._lDesc

        return barrier._lDesc
    
    if action[0] == "open":
        return barrier.open()


reactionMap["old_door"] = old_door

class Barrier(GameObject):
    def __init__(self, **kwargs): 

        log.info(console_color("purple","New Barrier Created: {}".format(kwargs["tag"])))
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
        self._open = True
        return "you open it"

    _open = False
    _connections = []
    _location = str
    _connectionNum = int