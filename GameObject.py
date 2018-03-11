#!/usr/local/Cellar/python3
import sys, traceback, logging
from util import clear_screen#, console_color

log = logging.getLogger('game.Game')

class GameObject(object):
    def __init__(self, **kwargs): 
        self.game = kwargs["GAME"]
        
        self._tag = kwargs["tag"]
        self._lDesc = kwargs["long_description"]
        self._sDesc = kwargs["short_description"]
        if "alias_list" in kwargs: self.aliasList = kwargs["alias_list"]

        self.tagInventory = []
        self.inventory = {}

        log.info("New GameObject Constructed: {}".format(self._tag))

    def give_object(self, obj):
        '''gives obj to self.inventory'''
        log.info("{}.give_object({})".format(self._tag, obj._tag))
        self.tagInventory.append(obj._tag)
        for alias in obj.aliasList:
            if alias in self.inventory: self.inventory[alias].append(tag)
            else: self.inventory[alias] = [obj._tag]

    def remove_object(self, obj): #TODO: The key is still in the inventory even though the value is an empty list
        '''takes object from self.inventory'''
        log.info("{}.remove_object({})".format(self._tag, obj._tag ))
        self.tagInventory.remove(obj._tag)
        for alias in obj.aliasList:
            self.inventory[alias].remove(obj._tag)
            if len(self.inventory[alias]) == 0: self.inventory.pop(alias, None)
