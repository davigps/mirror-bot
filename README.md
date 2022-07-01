<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=300px src="./assets/logo.png" alt="Bot logo"></a>
</p>

<h3 align="center">🤖 Mirror Bot</h3>

---

<p align="center"> 
    This bot record and/or reproduce everything you do <br>
    on your keyboard and mouse. 
</p>

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The purpose of this bot is to record everything you do on your keyboard and mouse, <br>
so, if daily you execute some routine on your PC, then, you can use the mirror bot <br>
to reproduce that routine previously saved. It's very useful to save your precious energy and time. Unfortunately, the bot was only tested on linux.

## 💭 How it works <a name = "working"></a>

The bot will record every button you press and when you release it on a file <br>
with extension .mirror, then, to reproduce your mirror file, it just interpret and <br>
follow its statements.

The entire bot is written in Python 3.6.

## 🎈 Usage <a name = "usage"></a>

To use the bot, you will need all requirements installed.
Then, just type:

```
poetry run mirror-bot
```

`mirror-bot [-h] [-l] [-p PLAY] [-r RECORD]`

Available options:

`-h, --help            show this help message and exit`

`-l, --list            list all saved mirrors`

`-p PLAY, --play PLAY  specify mirror to play`

`-r RECORD, --record RECORD   specify mirror name to be recorded`

### Installing Prerequisites

Clone repository on your local machine and open its directory.

```
git clone https://github.com/davigsousa/mirror-bot.git && cd mirror-bot
```

Then, install its requirements with [poetry](https://python-poetry.org/).

```
poetry install
```

Finally, you are ready to go!

## ⛏️ Built Using <a name = "built_using"></a>

- [Python3.6](https://www.python.org/)
- [PyDub](https://pypi.org/project/pydub/)
- [Pynput](https://pypi.org/project/pynput/)

## ✍️ Authors <a name = "authors"></a>

- [@davigsousa](https://github.com/davigsousa) - Idea & Initial work
