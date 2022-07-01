import argparse
import os

from mirror_bot.cli.commands import Commands


def run():
    commands = Commands()
    commands.process()

if __name__ == "__main__":
    run()