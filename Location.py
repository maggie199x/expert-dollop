#!python3
import GameObject
from GameObject import GameObject

class Location(GameObject):

	def __init__(self, tag, connect, lDesc, sDesc):
		super(Location, self).__init__(tag, lDesc, sDesc)
		self._connections = connect

	_connections = None
	_visited = False

