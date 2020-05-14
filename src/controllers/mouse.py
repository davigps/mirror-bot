from _io import TextIOWrapper
from time import time, sleep
from pynput import keyboard


class MouseController:
    '''Will reproduce everything on mirror file.'''

    def __init__(self, file: TextIOWrapper):
        self.file = file
  
    def start(self):
        pass

