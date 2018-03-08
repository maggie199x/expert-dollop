#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

reactionMap = {}

def cell_key(item, player, command):
	print("cell_key reaction")

reactionMap["cell_key"] = cell_key

class Item(GameObject):

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        if "pick_up" in kwargs: self.pickup = kwargs["pick_up"]
    


