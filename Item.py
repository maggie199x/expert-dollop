#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

reactionMap = {}

def cell_key(item):
	if item.game.playerInput[0] == "get":
		item.game.allObj[item._location].remove_object(item)
		item.game.player.give_object(item)
		return "you pick it up"

	return "cell_key reaction"

reactionMap["cell_key"] = cell_key

class Item(GameObject):

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        if "pick_up" in kwargs: self.pickup = kwargs["pick_up"]
        self._location = kwargs["location"]
        #self.react = reactionMap[kwargs["tag"]]

    def react(self, player, command):
    	return reactionMap[self._tag](self)
    


