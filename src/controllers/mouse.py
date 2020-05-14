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
        for i, setence in enumerate(self.stream):
            if i == 0:
                self.controller.position = (int(pos) for pos in setence.metadata.split(','))
                continue

            sleep(setence.pause)

            if setence.action == 'mv':
                current_position = self.controller.position
                position = [int(pos) for pos in setence.metadata.split(',')]
                
                self.controller.move(
                    position[0] - current_position[0],
                    position[1] - current_position[1]
                )

            elif setence.action == 'sc':
                scroll = (int(delta) for delta in setence.metadata.split(','))
                self.controller.scroll(scroll[0], scroll[1])

            else:
                button = mouse.Button[setence.metadata]
                if setence.action == 'ps':
                    self.controller.press(button)
                else:
                    self.controller.release(button)


