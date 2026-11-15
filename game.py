def count_living(pets):
    return sum(1 for pet in pets.values() if pet.is_alive)


def count_dead(pets):
    return sum(1 for pet in pets.values() if not pet.is_alive)


def average_health(pets):
    living = [pet for pet in pets.values() if pet.is_alive]
    if not living:
        return 0
    return sum(pet.health for pet in living) / len(living)


def average_hunger(pets):
    living = [pet for pet in pets.values() if pet.is_alive]
    if not living:
        return 0
    return sum(pet.hunger for pet in living) / len(living)


def average_boredom(pets):
    living = [pet for pet in pets.values() if pet.is_alive]
    if not living:
        return 0
    return sum(pet.boredom for pet in living) / len(living)


def average_exhaustion(pets):
    living = [pet for pet in pets.values() if pet.is_alive]
    if not living:
        return 0
    return sum(pet.exhaustion for pet in living) / len(living)


def show_statistics(pets):
    print("\n--- Game Statistics ---")
    print(f"Living pets: {count_living(pets)}")
    print(f"Dead pets: {count_dead(pets)}")
    print(f"Average health: {average_health(pets):.1f}")
    print(f"Average hunger: {average_hunger(pets):.1f}")
    print(f"Average boredom: {average_boredom(pets):.1f}")
    print(f"Average exhaustion: {average_exhaustion(pets):.1f}\n")
