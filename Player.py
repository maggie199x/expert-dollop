#!/usr/local/Cellar/python3
import json
import logging
import settings
#from util import console_color

from GameObject import GameObject

log = logging.getLogger('game.Player')






#TODO: make Player in charge of searching and "getting" instead of Game.py
#TODO: Change functions in reaction maps to take kwargs
class Player(GameObject):

    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        log.info("New Player Created: {}".format(kwargs["tag"]))
        self._location = kwargs["location"]
        self.reactionMap = {
            "move" : self.move,
            "inventory" : self.check_inventory
        }


    def __str__(self):
        return json.dumps(self.__dict__)

    def move(self, command):
        log.info("{}.move({})".format(self._tag, command))
        direction = command[1]
        if direction in self.game.allObj[self._location]._barriers:
            if self.game.allObj[self._location]._barriers[direction]._open: 
                self._location = self.game.allObj[self.game.allObj[self._location]._connections[direction]] #give player new location
                return self._location.react()

            else: return self.game.allObj[self._location]._barriers[direction]._sDesc

        return "theres nothing that way for you"


    def check_inventory(self, command):
        log.info("{}.check_inventory({})".format(self._tag, command))
        result = "You are holding: "
        for gameObjTag in self.tagInventory:
            result += self.game.allObj[gameObjTag]._sDesc
        return result

            

    def react(self, command):
        log.info("{}.react({})".format(self._tag, command))
        if command[0] in self.reactionMap: return self.reactionMap[command[0]](command)
        else: return "ERROR: command passed to 'Player' dispite no matching command"
    
