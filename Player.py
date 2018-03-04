#!/usr/local/Cellar/python3
import json
import logging
import settings
from util import console_color

from GameObject import GameObject

log = logging.getLogger('game.Player')






class Player(GameObject):

    def __init__(self, objDict, **kwargs):
        super(Player, self).__init__(**kwargs)
        log.info(console_color("New Player Created: {}".format(objDict), color="red"))
        self._objDict = objDict
        self._location = self._objDict[kwargs["location"]]

    def __str__(self):
        return json.dumps(self.__dict__)

    def _move(self, direction):
        if direction in self._location._barriers:
            if self._location._barriers[direction]._open: 
                self._location = self._objDict[self._location._connections[direction]] #give player new location
                return self._location.react(self, ["move", direction])

            else: return self._location._barriers[direction]._sDesc


            #return self._barriers[direction].react(player, ["m", direction])

            #return reactionMap[self._tag](player, self, direction)

        return "theres nothing that way for you"
        #return self._location.player_move(self, direction)
            

    def react(self, command):
        if command[0] == 'move':
            if len(command) == 2:
                return self._move(command[1])
            return "Move where?"
        else: return "ERROR: command passed to 'Player' dispite no matching command"
    
