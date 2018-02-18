#!python3
import json

import Player, Location
from Player import Player
from Location import Location

class Game(object):
    def __init__(self):
        self._Player_action_queue = ["m"]
        self._reactionMap = {
            "exit" : self._quit,
            "quit" : self._quit
        }

	try:
            self._locations = json.loads(open('locations.json'))
        except Exception, e:
            print 'Error parsing locations.json'

        self._player = Player("player", self._locations, self._locations["first_room"])

    def command(self):
        self._command = raw_input("@> ").lower().split()
        print(self._command)
        if self._command[0] in self._Player_action_queue: self._player_action()
        if self._command[0] in self._reactionMap:
            self._reactionMap[self._command[0]]()

    def run(self):
        while(self._running):
            self.command()

    def _player_action(self):
        print("Game::player_action")
        return self._player.react(self._command)

    def _inclusive_action(self):
        print("Game::inclusive_action")


    def exit_game(self):
        self._running = False

    def player(): #return player
        return
    def running(): #return running
        return
    def test(self):
        print("test is successful")
        return

    def _quit(self):
        self._running = False
        print("quitting")


    #members
    _reactionMap = {}
    _command = None 
    _running = True
    _player = None
    _parser = None

    _locations = {}
    #need to figure out reactionMap
    _moveAlias = ["go", "move"]

def main():
        game = Game()
        game.run()

main()

