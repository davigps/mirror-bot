from mirror_bot.cli.bridge import Bridge


def run():
    bridge = Bridge()
    bridge.process()

if __name__ == "__main__":
    run()