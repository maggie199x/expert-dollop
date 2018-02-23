#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

class Location(GameObject):

    def __init__(self, **kwargs): 
    	#print(kwargs)
        super(Location, self).__init__(**kwargs)
        #self._connections = kwargs["connections"]

    _connections = None
    _visited = False

