<h2 align="center">A Selenium Quizlet Bot</h2>

<p align="center">
<a href="https://github.com/arozx/quizlet_bot/blob/main/LICENSE"><img alt="License: OpenBSD 3 Clause" src="https://img.shields.io/badge/licence-BSD%203--Clause-blueviolet"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

---

# Installation and usage

## Installation

You need to have _python3_, _selenium_, if you are **NOT** using firefox you must change line 21 in in the bot to:
```python
driver = webdriver."your webrowser here"()
```
_The bot's_ python dependancies can be installed by running `pip install -r requirements.txt`.

## Usage

### Linux

You **MUST** change line 18 in [linux_bot.py](linux_bot.py) to match the location of the selenium driver

```sh
python3 quizlet_bot/linux_bot.py -url -u -p -t
```

-url = flashcards **_full_** url

-u = Quizlet Username

-p = Quizlet Password

-t = Time in minutes

---

### Windows

```sh
python3 quizlet_bot/windows_bot.py -url -u -p -t
```

-url = flashcards **_full_** url

-u = Quizlet username

-p = Quizlet password

-t = Time in minutes

# Roadmap

<div align="center">

```mermaid
graph TD;
    Quizlet-Bot--> Graphical-User-Interface;
    Quizlet-Bot-->Flashcards;
    Flashcards-->Multiple-Sets;
    Flashcards-->Advanced-Time-Control;
    Quizlet-Bot-->Match;
    Quizlet-Bot-->Learn;
```
</div>