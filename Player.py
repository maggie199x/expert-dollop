#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject




class Player(GameObject):
    def __init__(self, objDict, **kwargs):
        super(Player, self).__init__(**kwargs)
        self._objDict = objDict
        self._location = self._objDict[kwargs["location"]]

    def _move(self, direction):
        return self._location.player_move(self, direction)
            

    def react(self, command):
        if command[0] == 'm' and len(command) == 2:
            return self._move(command[1])

    _location = None
    _objDict = None
    
