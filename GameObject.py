#!/usr/local/Cellar/python3
import sys, traceback

class GameObject(object):
    def __init__(self, **kwargs): 
        
        self._tag = kwargs["tag"]
        self._lDesc = kwargs["long_description"]
        self._sDesc = kwargs["short_description"]
        if "inventory" in kwargs: self._inventory = kwargs["inventory"] 

    
    def give_item(self, tag):
        self._inventory.append(tag)

    def take_item(self, tag):
        self._inventory.remove(tag)
    
    _tag = None
    _sDesc = None
    _lDesc = None
    _inventory = []
    _alias = []
