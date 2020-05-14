from typing import List
from interpreters.setence import Setence
from time import sleep
from pynput import keyboard

class KeyboardController:
    '''Will reproduce everything on mirror file.'''

    def __init__(self, stream: List[Setence]):
        self.controller = keyboard.Controller()
        self.stream = stream

    def start(self):
        for setence in self.stream:
            key = keyboard.Key[setence.metadata]
            sleep(setence.pause)
            if setence.action == 'ps':
                self.controller.press(key)
            else:
                self.controller.release(key)

    

