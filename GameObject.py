#!/usr/local/Cellar/python3
import sys, traceback

class GameObject(object):
    def __init__(self, **kwargs): 
        
        self._tag = kwargs["tag"]
        if "alias_list" in kwargs: self.aliasList = kwargs["alias_list"]
        self._lDesc = kwargs["long_description"]
        self._sDesc = kwargs["short_description"]
        if "inventory" in kwargs: self.tagInventory = kwargs["inventory"]
        self.inventory = {}

    
    '''def give_item(self, tag):
        self._inventory.append(tag)

    def take_item(self, tag):
        self._inventory.remove(tag)'''
    
