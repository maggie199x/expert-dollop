#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject




class Player(GameObject):
    def __init__(self, objDict, **kwargs):
        super(Player, self).__init__(**kwargs)
        self._objDict = objDict
        self._location = self._objDict[kwargs["location"]]

    def _move(self, direction):
        if direction in self._location._barriers:
            if self._location._barriers[direction]._open: 
                self._location = self._objDict[self._location._connections[direction]] #give player new location
                return self._location.react(self, ["visit"])

            else: return self._location._barriers[direction]._sDesc


            #return self._barriers[direction].react(player, ["m", direction])

            #return reactionMap[self._tag](player, self, direction)

        return "theres nothing that way for you"
        #return self._location.player_move(self, direction)
            

    def react(self, command):
        if command[0] == 'm' and len(command) == 2:
            return self._move(command[1])

    _location = None
    _objDict = None
    
