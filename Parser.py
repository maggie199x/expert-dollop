#!/usr/local/Cellar/python3
import argparse
import json
import platform
import logging

import settings
from util import clear_screen, console_color

class Parser:
    def __init__(self):
        self.aliasMap = {
            "exit": "quit",
            "go":   "move",
            "m":    "move",
            "o":    "open",
        }
        self.verb = "" 

    def extract_verb(self, inputText):
        # If the command is not in the alias list, returns the command
        alias = inputText[0]
        return self.aliasMap.get(alias, alias)

    def extract_subject(self, inputText):
        return ' '.join(inputText[1:])

    def parse_command(self, inputText):
        splitText = inputText.lower().split()
        result = []
        self.verb = self.extract_verb(splitText)
        self.subject = self.extract_subject(splitText)
        result.append(self.verb)
        result.append(self.subject)
        return result