#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

reactionMap = {}

def cell_key(item, player, command):
	if command[0] == "get":
		player.give_object(item)
	return "cell_key reaction"

reactionMap["cell_key"] = cell_key

class Item(GameObject):

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        if "pick_up" in kwargs: self.pickup = kwargs["pick_up"]
        self._location = kwargs["location"]
        #self.react = reactionMap[kwargs["tag"]]

    def react(self, player, command):
    	return reactionMap[self._tag](self, player, command)
    


