#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject

class Barrier(GameObject):
	def __init__(self, **kwargs): 
		#pass
		#print(kwargs)
		self._connections = kwargs["connections"]
		self._location = kwargs["location"]
		self._connectionNum = kwargs["connection_num"]

		super(Barrier, self).__init__(**kwargs)

	_connections = []
	_location = str
	_connectionNum = int