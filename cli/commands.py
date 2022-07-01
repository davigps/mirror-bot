import argparse

import cli.bridge as command

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
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)

        self.parser.add_argument(
            '-l', '--list', action='store_true'
        )
        self.parser.add_argument('-p', '--play')
        self.parser.add_argument('-r', '--record')

        args, unknown = self.parser.parse_known_args()
        self.args = args
        self.unknown = unknown
    
    def process(self):
        if self.args.list:
            command.list_mirrors()
            return
        
        if self.args.play:
            command.play_mirror(self.args.play)
            return
        
        if self.args.record:
            command.record_mirror(self.args.record)
            return
        
        self.parser.print_help()
