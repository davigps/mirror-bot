from _io import TextIOWrapper
from time import time, sleep
from pynput import keyboard

class KeyboardRecorder:
    '''Will record everything pressed on keyboard.'''

    def __init__(self, file: TextIOWrapper):
        self.file = file
        self.last_event: float = None
  
    def start(self):
        '''Start record process.'''
        self.last_event = time()
        with keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release) as listener:
            listener.join()
    
    def on_press(self, key):
        delta = time() - self.last_event
        self.last_event = time()

        if key == keyboard.Key.esc:
            print('Record ended.')
            self.file.close()
            return False
        
        data = f'{delta}|&|ps|&|{key}|;|'
        self.file.write(data)


    def on_release(self, key: keyboard.Key):
        delta = time() - self.last_event
        self.last_event = time()

        data = f'{delta}|&|rs|&|{key}|;|'
        self.file.write(data)

