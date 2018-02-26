#!/usr/local/Cellar/python3
from pprint import pprint

import GameObject
from GameObject import GameObject
from Barrier import Barrier

class Location(GameObject):

    def __init__(self, **kwargs): 
        #print(kwargs)
        super(Location, self).__init__(**kwargs)
        self._connections = kwargs["connections"]
        #print(bars)
        self._barriers = {}
         

    def give_barrier(self, barrier, direction):
        '''for barrier in kwargs:
            direction = kwargs[barrier]["connections"][index]
            self._barriers[direction] = Barrier(**(kwargs[barrier]))
            return self._connections[direction]
        '''
        #print(barrier)
        #print(direction)
        self._barriers[direction] = barrier
        return self._connections[direction]

    _connections = None
    _barriers = None
    _visited = False

