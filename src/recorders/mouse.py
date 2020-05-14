from _io import TextIOWrapper
from threading import Thread
from time import time, sleep
from pynput import mouse


def close_if_needed(function):
    def wrapper(self, *args):
        if not self.is_alive():
            self.file.close()
            return False
        function(self, *args)
    
    return wrapper

class MouseRecorder:
    '''Will record everything pressed on mouse.'''

    def __init__(self, file: TextIOWrapper, k_is_alive: Thread.is_alive):
        self.file = file
        self.is_alive = k_is_alive
        self.last_event: float = None
  
    def start(self):
        '''Start process and set recorder's initial time.'''
        self.last_event = time()
        with mouse.Listener(
            on_click=self.on_click, 
            on_move=self.on_move,
            on_scroll=self.on_scroll) as listener:
            listener.join()

    @close_if_needed
    def on_click(self, x, y, button, pressed):
        if pressed:
            delta = time() - self.last_event
            self.last_event = time()

            metadata = str(button).replace('Button.', '')
            data = f'{delta}&ps&{metadata};'
            self.file.write(data)
        else:
            delta = time() - self.last_event
            self.last_event = time()

            metadata = str(button).replace('Button.', '')
            data = f'{delta}&rs&{metadata};'
            self.file.write(data)
    
    @close_if_needed
    def on_move(self, x, y):
        delta = time() - self.last_event
        self.last_event = time()

        data = f'{delta}&mv&{x},{y};'
        self.file.write(data)

    @close_if_needed
    def on_scroll(self, x, y, dx, dy):
        delta = time() - self.last_event
        self.last_event = time()

        data = f'{delta}&sc&{dx},{dy};'
        self.file.write(data)