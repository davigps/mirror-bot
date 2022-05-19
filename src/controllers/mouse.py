from time import sleep
from typing import List

from pynput.mouse import Button, Controller

from interpreters.setence import Setence


def read_setence(controller: Controller, setence: Setence):
    """Read the keyboard setence and press or release its key."""
    sleep(setence.pause)

    if setence.action == "mv":
        current_position = controller.position
        position = [int(pos) for pos in setence.metadata.split(",")]

        controller.position = tuple(position)

    elif setence.action == "sc":
        scroll = (int(delta) for delta in setence.metadata.split(","))
        controller.scroll(scroll[0], scroll[1])

    else:
        button = Button[setence.metadata]
        if setence.action == "ps":
            controller.press(button)
        else:
            controller.release(button)
