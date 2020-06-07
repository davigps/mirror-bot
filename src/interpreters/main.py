from _io import TextIOWrapper
from typing import List
from interpreters.setence import Setence


class Interpreter:
    def __init__(self, record: TextIOWrapper):
        self.record = record.read()
        self.setences: List[Setence] = []
        self.read_record()
    
    def read_record(self):
        '''
        Read some mirror recorded file, by changing the string into Setence Object,
        then, append it in setence list.
        '''
        for string in self.record.split('-;-'):
            if not string: continue
            setence = Setence(string)
            self.setences.append(setence)
    
    def get_stream(self) -> List[Setence]:
        '''Return Setence List'''
        return self.setences