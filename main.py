from tamagotchi import Tamagotchi
import game
import storage


def create_pets():
    return {
        "Tama": Tamagotchi("Tama"),
        "Mochi": Tamagotchi("Mochi"),
        "Pochi": Tamagotchi("Pochi"),
    }


def print_menu():
    print("1. Select a Tamagotchi")
    print("2. Show game statistics")
    print("3. Save game")
    print("4. Load game")
    print("5. Quit")


def print_pet_menu(pet):
    print(f"\nSelected: {pet.name}")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Heal")
    print("5. Show status")
    print("6. Back to main menu")


def select_pet(pets):
    print("\nAvailable pets:")
    for name in pets:
        print(f"- {name}")

    choice = input("Type the pet's name: ").strip()

    if choice not in pets:
        print("That pet does not exist.")
        return

    pet = pets[choice]

    while True:
        print_pet_menu(pet)
        action = input("Choose an option: ").strip()

        if action == "1":
            pet.feed()
        elif action == "2":
            pet.play()
        elif action == "3":
            pet.sleep()
        elif action == "4":
            pet.heal()
        elif action == "5":
            pet.show_status()
        elif action == "6":
            return
        else:
            print("Invalid option, try again.")


def main():
    pets = create_pets()

    while True:
        print("\n===== Tamagotchi Simulator =====")
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            select_pet(pets)
        elif choice == "2":
            game.show_statistics(pets)
        elif choice == "3":
            storage.save_game(pets)
        elif choice == "4":
            loaded = storage.load_game()
            if loaded is not None:
                pets = loaded
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
