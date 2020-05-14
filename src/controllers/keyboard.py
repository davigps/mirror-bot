from interpreters.setence import Setence
from time import sleep
from pynput.keyboard import Controller, Key

def read_setence(controller: Controller, setence: Setence):
    if len(setence.metadata) > 1:
        key = Key[setence.metadata]
    else:
        key = setence.metadata
    sleep(setence.pause)
    if setence.action == 'ps':
        controller.press(key)
    else:
        controller.release(key)
