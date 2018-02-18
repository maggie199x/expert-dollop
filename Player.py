#!python3
import GameObject
from GameObject import GameObject





class Player(GameObject):
	def __init__(self, tag, loc_dict, loc, inv):
		super(Player, self).__init__(tag, "ldesc of player", "sdesc of player", inv)
		'''
		try:
			self.react = reactionMap[tag]
		except:
			print("""Created GameObject has no appropriate reaction function
				 , closing system""")
			sys.exit(1) #abort'''
		self._location = loc
		self._map = loc_dict

	def _move(self, dir):
		print("Player::_move")
		if dir in self._location._connections:
			self._location = self._map[self._location._connections[dir]]
			if self._location._visited: print(self._location._sDesc)
			else:
		 		self._location._visited = True
		 		print(self._location._lDesc)
			

	def react(self, command):
		print("Player::player_action")
		if command[0] == 'm' and len(command) == 2:
			self._move(command[1])

	_location = None
	_map = None
	
