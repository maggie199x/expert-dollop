import logging
import os

log = logging.getLogger('game.util')

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def console_color(message, **kwargs):
    color = kwargs.get("color", "white")
    background = kwargs.get("background", "black")
    
    colors = {
        "end": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "orange": "\033[33m",
        "blue": "\033[34m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "lightgrey": "\033[37m",
        "darkgrey": "\033[90m",
        "lightred": "\033[91m",
        "lightgreen": "\033[92m",
        "yellow": "\033[93m",
        "lightblue": "\033[94m",
        "pink": "\033[95m",
        "lightcyan": "\033[96m"
    }

    background_colors = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "orange": "\033[43m",
        "blue": "\033[44m",
        "purple": "\033[45m",
        "cyan": "\033[46m",
        "lightgrey": "\033[47m"
    }

    return "".join([colors[color], background_colors[background], message, colors["end"]])