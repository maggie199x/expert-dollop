#!/usr/local/Cellar/python3
import argparse
import json
import platform
import logging

import settings
from util import clear_screen

class Parser:
    def __init__(self):
        self.aliasMap = {
            "exit": "quit",
            "go":   "move",
            "m":    "move",
            "o":    "open",
            "i":    "inventory",
            "inv":  "inventory",
            "north": "n",
            "south": "s",
            "east": "e",
            "west": "w"
        }
        self.verb = "" 
        self.subject = ""

    def parse_command(self, inputText):
        splitText = inputText.lower().split()
        splitText = self.dealias(splitText)
        result = []
        self.verb = splitText[0]#self.extract_verb(splitText)
        self.subject = self.extract_subject(splitText)
        if self.verb: result.append(self.verb)
        if self.subject: result.append(self.subject)
        return result


    def extract_verb(self, splitText):
        # If the command is not in the alias list, returns the command
        alias = splitText[0]
        return self.aliasMap.get(alias, alias)

    def extract_subject(self, splitText):
        i = 1
        indexToDelete = []
        while(i < len(splitText) - 1):
            if splitText[i] == "the":
                indexToDelete = [i] + indexToDelete #adding to beggning of list if element is 'the'
            i += 2

        for element in indexToDelete:
            splitText.pop(element)
        return ' '.join(splitText[1:])

    def dealias(self, splitText):
        for i in range(0, len(splitText)):
            word = splitText[i]
            splitText[i] = self.aliasMap.get(word, word)
        return splitText


def main():
    print("running")
    parser = Parser()
    print(parser.parse_command("open the old door"))
    print(parser.verb)
    print(parser.subject)




