#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

class Item(GameObject):

    def __init__(self, tag, lDesc, sDesc, pickup):
        super().__init__(tag, lDesc, sDesc)
        self._pickup = pickup
    


