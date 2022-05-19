from threading import Thread
from time import sleep, time

from _io import TextIOWrapper
from pynput import mouse


def close_if_needed(function):
    def wrapper(self, *args):
        if not self.is_alive():
            self.file.close()
            return False
        function(self, *args)

    return wrapper


class MouseRecorder:
    """Will record everything pressed on mouse."""

    def __init__(
        self, file: TextIOWrapper, delay_information, k_is_alive: Thread.is_alive
    ):
        self.file = file
        self.is_alive = k_is_alive
        self.last_event = delay_information

    def start(self):
        """Start process and set recorder's initial time."""

        with mouse.Listener(
            on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll
        ) as listener:
            listener.join()

    @close_if_needed
    def on_click(self, x, y, button, pressed):
        if pressed:
            delta = time() - self.last_event[0]
            self.last_event[0] = time()

            self.append_data(delta, "ps", str(button))
        else:
            delta = time() - self.last_event[0]
            self.last_event[0] = time()

            self.append_data(delta, "rs", str(button))

    @close_if_needed
    def on_move(self, x, y):
        delta = time() - self.last_event[0]
        self.last_event[0] = time()

        self.append_data(delta, "mv", f"{x},{y}")

    @close_if_needed
    def on_scroll(self, x, y, dx, dy):
        delta = time() - self.last_event[0]
        self.last_event[0] = time()

        self.append_data(delta, "sc", f"{dx},{dy}")

    def append_data(self, delta: float, action: str, metadata: str):
        if "Button" in metadata:
            metadata = metadata.replace("Button.", "")
        data = f"m|&|{delta}|&|{action}|&|{metadata}-;-"
        self.file.write(data)
