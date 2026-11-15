import json

from tamagotchi import Tamagotchi

SAVE_FILE = "savegame.json"


def save_game(pets):
    data = {name: pet.to_dict() for name, pet in pets.items()}

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("Game saved.")


def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No save file found.")
        return None
    except json.JSONDecodeError:
        print("Save file is corrupted or invalid.")
        return None

    pets = {}
    for name, pet_data in data.items():
        pets[name] = Tamagotchi.from_dict(pet_data)

    print("Game loaded.")
    return pets
