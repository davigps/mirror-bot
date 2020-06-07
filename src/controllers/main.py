from typing import List
from interpreters.setence import Setence
from time import sleep
import pynput

from controllers import keyboard, mouse


class Controller:
    '''
        Class responsable for read every setence and
        execute by calling the controller of its type.
    '''

    def __init__(self, stream: List[Setence]):
        self.keyboardController = pynput.keyboard.Controller()
        self.mouseController = pynput.mouse.Controller()
        self.stream = stream

    def start(self):
        '''Start the main Controller to read and execute every setence.'''
        for i, setence in enumerate(self.stream):
            if i == 0:
                self.mouseController.position = (int(pos) for pos in setence.metadata.split(','))
                continue

            if setence.type == 'k':
                keyboard.read_setence(self.keyboardController, setence)
            else:
                mouse.read_setence(self.mouseController, setence)
