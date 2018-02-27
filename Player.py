#!/usr/local/Cellar/python3
import json
import logging

import GameObject
from GameObject import GameObject

log = logging.getLogger('game.Player')

class Player(GameObject):

    def __init__(self, objDict, **kwargs):
        super(Player, self).__init__(**kwargs)

        log.info("New Player Created: {}".format(objDict))

        self._objDict = objDict
        self._location = self._objDict[kwargs["location"]]

    def __str__(self):
        return json.dumps(self.__dict__)

    def _move(self, direction):
        return self._location.player_move(self, direction)

    def react(self, command):
        if command[0] == 'm' and len(command) == 2:
            return self._move(command[1])
