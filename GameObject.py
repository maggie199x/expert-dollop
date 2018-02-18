#!python3
import sys, traceback

class GameObject(object):
    def __init__(self, **kwargs):
        for i in kwargs:

            self._tag = kwargs["tag"]
            self._lDesc = kwargs["long_description"]
            self._sDesc = kwargs["short_description"]
            self._inv = kwargs["inventory"]

    
    def give_item(self, tag):
        self._inv.append(tag)

    def take_item(self, tag):
        self._inv.remove(tag)
    
    #react = None
    _tag = None
    _sDesc = None
    _lDesc = None
    _inv = []
    _alias = []
