#!/usr/local/Cellar/python3
import GameObject
from GameObject import GameObject



''' The barrier object class are objects which prevent player movement, or trigger events which happen when a player passes through
They are not in charge of the player moving to a new location. If a barrier is open, the player WILL be able to move into a new location
The barrier object simply decides if a reaction happens when the player enters the new location
IE. the player moves into a new room, and the door shuts behind him. '''


reactionMap = {}

def old_door(barrier, player, command):
    #print("old_door::reaction")
    #print(action)
    ''' Not sure that this is necessary anymore 
    if action[0] == "m":
        if barrier._open:
            player._location = barrier._connections[action[1]]
            if player._location._visited: return player._location._sDesc
            else:
                player._location._sDesc
                return player._location._lDesc

        return barrier._lDesc
    '''
    if command[0] == "open":
        return barrier.open()


reactionMap["old_door"] = old_door

class Barrier(GameObject):
    def __init__(self, **kwargs): 
        #pass
        #print(kwargs)
        self._connections = kwargs["connections"]
        self._location = kwargs["location"]
        self._connectionNum = kwargs["connection_num"]
        if "open" in kwargs: self._open = kwargs["open"]

        super(Barrier, self).__init__(**kwargs)

    def react(self, player, action):
        #print("react::" + self._tag)
        return reactionMap[self._tag](self, player, action)


    def open(self):
        #print("barrier::open")
        self._open = True
        return "you open it"

    _open = False
    _connections = []
    _location = str
    _connectionNum = int