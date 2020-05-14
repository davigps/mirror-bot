from typing import List
from interpreters.setence import Setence
from time import sleep
from pynput import mouse

class MouseController:
    '''Will reproduce everything on mirror file.'''

    def __init__(self, stream: List[Setence]):
        self.controller = mouse.Controller()
        self.stream = stream

    def start(self):
        for setence in self.stream:
            if setence.action == 'mv':
                position = (int(pos) for pos in setence.metadata.split(','))
                self.controller.position = position
            elif setence.action == 'sc':
                scroll = (int(delta) for delta in setence.metadata.split(','))
                self.controller.scroll(scroll[0], scroll[1])
