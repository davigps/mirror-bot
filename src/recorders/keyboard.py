from _io import TextIOWrapper
from time import time, sleep
from pynput import keyboard

class KeyboardRecorder:
    '''Will record everything pressed on keyboard.'''

    def __init__(self, file: TextIOWrapper, delay_information):
        self.file = file
        self.last_event = delay_information
  
    def start(self):
        '''Start record process.'''
        self.last_event[0] = time()
        with keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release) as listener:
            listener.join()
    
    def on_press(self, key):
        delta = time() - self.last_event[0]
        self.last_event[0] = time()

        if key == keyboard.Key.esc:
            print('Record ended.')
            self.file.close()
            return False
        
        self.append_data(delta, 'ps', str(key))


    def on_release(self, key: keyboard.Key):
        delta = time() - self.last_event[0]
        self.last_event[0] = time()

        self.append_data(delta, 'rs', str(key))
    
    def append_data(self, delta: float, action: str, metadata: str):
        if 'Key' in metadata:
            metadata = metadata.replace('Key.', '')
        else:
            metadata = metadata.replace("'", '')
        data = f'k|&|{delta}|&|{action}|&|{metadata}-;-'
        self.file.write(data)

