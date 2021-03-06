#!/usr/local/Cellar/python3
from GameObject import GameObject

import logging
import settings
#from util import console_color


log = logging.getLogger(__name__)

file_handler = logging.FileHandler('_logs/Item.log')

log.addHandler(file_handler)

reactionMap = {}

def cell_key(item):
    #TODO: make a general function for actions like "get"
    log.info("{}: cell_key reaction".format(item._tag))
    if item.game.playerInput[0] == "get":
        item.game.allObj[item._location].remove_object(item)
        item.game.player.give_object(item)
        return "you pick it up"

    log.error("ERROR: command passed to 'Item' dispite no matching command")
    return "Nothing happens."

def door_key(item):
    #TODO: make a general function for actions like "get"
    log.info("{}: door_key reaction".format(item._tag))
    if item.game.playerInput[0] == "get":
        item.game.allObj[item._location].remove_object(item)
        item.game.player.give_object(item)
        return "you pick it up"

    log.error("ERROR: command passed to 'Item' dispite no matching command")
    return "Nothing happens."

reactionMap["cell_key"] = cell_key
reactionMap["door_key"] = door_key

class Item(GameObject):

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        if "pick_up" in kwargs: self.pickup = kwargs["pick_up"]
        self._location = kwargs["location"]
        
        log.info("New Item Created: {}".format(kwargs["tag"]))

    def react(self): 
        log.info("{}.react()".format(self._tag))
        return reactionMap[self._tag](self)
    


