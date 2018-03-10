#!/usr/local/Cellar/python3
import json
import logging
import settings
from util import console_color


from GameObject import GameObject
from Barrier import Barrier

log = logging.getLogger('game.Location')

reactionMap = {}



def second_room(location):
    return location.base_react(location.game.playerInput)

def first_room(location):
    return location.base_react(location.game.playerInput)
    

reactionMap["second_room"] = second_room
reactionMap["first_room"] = first_room

class Location(GameObject):

    def __init__(self, **kwargs): 
        super(Location, self).__init__(**kwargs)
        log.info(console_color("New Location Created: {}".format(kwargs["tag"]), color="green"))

        self.baseMap = { "move" : self.visit }

        self._connections = kwargs["connections"]
        self._barriers = {}
        self._react = reactionMap[kwargs["tag"]]
        self._visited = False


    def __str__(self):
        return json.dumps(self.__dict__)

    def base_react(self, command):
        if command[0] in self.baseMap: return self.baseMap[command[0]]()
    
    def react(self): 
        return reactionMap[self._tag](self)


    def visit(self):
        self.game.player._location = self._tag
        print(self.game.player._location)
        if self._visited: return self._sDesc
        else: 
            self._visited = True
            return self._lDesc

    def give_barrier(self, barrier, direction):
        self.give_object(barrier)
        self._barriers[direction] = barrier
        return self._connections[direction]

    def player_move(self, player, direction):
        '''
        if direction in self._connections:
            if direction in self._barriers:
                return self._barriers[direction].react(player, ["m", direction])

            return reactionMap[self._tag](player, self, direction)
        return "there's nothing but death that way" '''

    

