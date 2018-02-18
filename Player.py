#!python3
import GameObject
from GameObject import GameObject





class Player(GameObject):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        '''
        try:
            self.react = reactionMap[tag]
        except:
            print("""Created GameObject has no appropriate reaction function
                 , closing system""")
            sys.exit(1) #abort'''
        self._location = kwargs["location"]

    def _move(self, dir):
        print("Player::_move")
        if dir in self._location._connections:
            self._location = self._ObjDict["location"][self._location._connections[dir]]
            if self._location._visited: print(self._location._sDesc)
            else:
                self._location._visited = True
                print(self._location._lDesc)
            

    def react(self, command):
        print("Player::player_action")
        if command[0] == 'm' and len(command) == 2:
            self._move(command[1])

    _location = None
    _objDict = None
    
