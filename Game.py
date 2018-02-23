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
            with open("GameObjects.json", 'r') as f:
                allObj = json.load(f)
                #print(allObj)
                for location in allObj["locations"]:
                    tag = location
                    #print(allObj["locations"][tag])
                    self._locations[tag] = Location(allObj["locations"][tag])

                #for player in allObj["locations"]: pass
                    #self._player = Player(player)
                '''
                self._locations = allObj["locations"]
                self._player = Player(allObj["player"][""])
                self._player = allObj["player"]["player"]
                self._player._objectDict = allObj'''
        except Exception, e:
            print "Error parsing GameObjects.json: %s" % e
            self._running = False
        

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

