from _io import TextIOWrapper
from time import time, sleep
from pynput import keyboard

class MouseController:
  '''Will record everything pressed on keyboard.'''

  def __init__(self, arq: TextIOWrapper):
    self.arq = arq
    self.initial_time: float = None
  
  def start(self):
    '''Start and set recorder's initial time.'''
    self.initial_time = time()
    

