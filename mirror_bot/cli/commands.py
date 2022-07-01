import argparse

from mirror_bot import MirrorBot

DESCRIPTION = '''
    You can run your C/C++ code
    just passing the filename as first argument.
    Example:
    'ggpp targetfile.cpp'
    | You can also pass other arguments to the g++.
    Example:
    'ggpp targetfile.cpp -Wall -H'
    '''

class Commands:
    

    def __init__(self) -> None:
        self.command_choices = {
            'list': self.list_mirrors,
            'play': self.play_mirror,
            'record': self.record_mirror
        }

        parse = argparse.ArgumentParser(description=DESCRIPTION)

        parse.add_argument(
            '-l', '--list', action='store_true'
        )
        parse.add_argument('-p', '--play')
        parse.add_argument('-r', '--record')

        args, unknown = parse.parse_known_args()
        self.args = args
        self.unknown = unknown
    
    def process(self):
        if self.args.list:
            self.list_mirrors()
            return
        
        if self.args.play:
            self.play_mirror(self.args.play)
            return
        
        if self.args.record:
            self.record_mirror(self.args.record)
            return

    def list_mirrors(self):
        print('bomdia')

    def play_mirror(self, mirror_name: str):
        MirrorBot.play_mirror(mirror_name)

    def record_mirror(self, mirror_name: str):
        MirrorBot.record_mirror(mirror_name)
