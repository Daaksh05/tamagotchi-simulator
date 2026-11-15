# Tamagotchi Simulator

A Python Tamagotchi-style virtual pet simulator built for the Introduction to Python Programming course (EPITA, IPP, Fall 2026).

The player manages three virtual pets and keeps them alive by feeding, playing, putting them to sleep, and healing them. Each pet has four stats — hunger, health, boredom, and exhaustion — that change over time and with random events. The game can be played through a command-line menu or a Tkinter graphical interface.

## Features

- Three pets, each with hunger, health, boredom, and exhaustion stats
- Feed, play, sleep, and heal actions that affect stats differently
- Random events (getting sick, finding food, random health bonus/penalty)
- Pets die if health reaches zero and can no longer perform actions
- Game statistics (living/dead pet counts, average stats)
- Save and load game state using JSON
- Error handling for invalid input, dead pets, and missing/corrupted save files
- Optional Tkinter GUI with live status bars, action buttons, and a log panel

## Project structure

```
tamagotchi/
|-- main.py        command-line interface
|-- gui.py         optional Tkinter graphical interface
|-- tamagotchi.py  Tamagotchi class (stats, actions, random events)
|-- game.py        game statistics
|-- storage.py     save/load game state as JSON
```

## Requirements

- Python 3.10+
- Tkinter (only needed to run `gui.py`; on macOS with Homebrew Python, install with `brew install python-tk`)

## Running the CLI version

```bash
python3 main.py
```

Follow the on-screen menu to select a pet, perform actions, view statistics, and save or load the game.

## Running the GUI version

```bash
python3 gui.py
```

Select a pet from the dropdown, use the action buttons to feed/play/sleep/heal, and check Statistics, Save, or Load from the Game panel. All actions and random events are shown in the log.

## Saving and loading

The game saves to `savegame.json` in the project folder. Loading a missing or corrupted save file is handled gracefully without crashing the program.
