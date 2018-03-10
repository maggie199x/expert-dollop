#!/usr/local/Cellar/python3
import sys, traceback

class GameObject(object):
    def __init__(self, **kwargs): 
        self.game = kwargs["GAME"]
        
        self._tag = kwargs["tag"]
        self._lDesc = kwargs["long_description"]
        self._sDesc = kwargs["short_description"]

        self.tagInventory = []
        if "alias_list" in kwargs: self.aliasList = kwargs["alias_list"]
        self.inventory = {}

    def give_object(self, obj):
        '''gives obj to self.inventory'''
        self.tagInventory.append(obj._tag)
        for alias in obj.aliasList:
            if alias in self.inventory: self.inventory[alias].append(tag)
            else: self.inventory[alias] = [obj._tag]

    def remove_object(self, obj): #TODO: The key is still in the inventory even though the value is an empty list
        '''takes object from self.inventory'''
        self.tagInventory.remove(obj._tag)
        for alias in obj.aliasList:
            self.inventory[alias].remove(obj._tag)
