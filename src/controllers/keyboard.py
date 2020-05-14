from _io import TextIOWrapper
from time import time, sleep
from pynput import keyboard

class KeyboardController:
  '''Will record everything pressed on keyboard.'''

  def __init__(self, arq: TextIOWrapper):
    self.arq = arq
    self.initial_time: float = None
  
  def start(self):
    self.initial_time = time()
    

