#!/usr/local/Cellar/python3
from GameObject import GameObject

import logging
import settings
#from util import console_color


log = logging.getLogger('game.Player')

reactionMap = {}

def cell_key(item):
    if item.game.playerInput[0] == "get":
        item.game.allObj[item._location].remove_object(item)
        item.game.player.give_object(item)
        return "you pick it up"

    return "ERROR: command passed to 'Item' dispite no matching command"

reactionMap["cell_key"] = cell_key

class Item(GameObject):

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        if "pick_up" in kwargs: self.pickup = kwargs["pick_up"]
        self._location = kwargs["location"]
        
        log.info("New Item Created: {}".format(kwargs["tag"]))

    def react(self): 
        log.info("{}.react()".format(self._tag))
        return reactionMap[self._tag](self)
    


