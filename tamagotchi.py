import random


class Tamagotchi:

    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.health = 100
        self.boredom = 50
        self.exhaustion = 50
        self.is_alive = True

    def feed(self):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot be fed.")
            return

        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0

        print(f"You fed {self.name}. Hunger is now {self.hunger}.")
        self.random_event()
        self.check_health()

    def play(self):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot play.")
            return

        self.boredom -= 25
        if self.boredom < 0:
            self.boredom = 0

        self.hunger += 10
        self.exhaustion += 15

        self._clamp_stats()

        print(f"You played with {self.name}. Boredom is now {self.boredom}.")
        self.random_event()
        self.check_health()

    def sleep(self):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot sleep.")
            return

        self.exhaustion -= 30
        if self.exhaustion < 0:
            self.exhaustion = 0

        print(f"{self.name} took a nap. Exhaustion is now {self.exhaustion}.")
        self.random_event()
        self.check_health()

    def heal(self):
        if not self.is_alive:
            print(f"{self.name} is dead and cannot be healed.")
            return

        self.health += 25
        if self.health > 100:
            self.health = 100

        print(f"You healed {self.name}. Health is now {self.health}.")

    def random_event(self):
        roll = random.randint(1, 10)

        if roll == 1:
            print(f"Oh no, {self.name} got sick!")
            self.health -= 15
        elif roll == 2:
            print(f"{self.name} found some food lying around!")
            self.hunger -= 15
        elif roll == 3:
            bonus = random.randint(-10, 10)
            if bonus >= 0:
                print(f"{self.name} got a random health bonus of {bonus}.")
            else:
                print(f"{self.name} got a random health penalty of {bonus}.")
            self.health += bonus

        self._clamp_stats()

    def check_health(self):
        self.hunger += 5
        self.boredom += 5
        self.exhaustion += 5

        self._clamp_stats()

        if self.hunger >= 100 or self.exhaustion >= 100:
            self.health -= 10
            self._clamp_stats()

        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"{self.name} has died.")

    def _clamp_stats(self):
        self.hunger = max(0, min(100, self.hunger))
        self.health = max(0, min(100, self.health))
        self.boredom = max(0, min(100, self.boredom))
        self.exhaustion = max(0, min(100, self.exhaustion))

    def show_status(self):
        status = "Alive" if self.is_alive else "Dead"
        print(f"\n--- {self.name} ---")
        print(f"Status: {status}")
        print(f"Health: {self.health}")
        print(f"Hunger: {self.hunger}")
        print(f"Boredom: {self.boredom}")
        print(f"Exhaustion: {self.exhaustion}\n")

    def to_dict(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "health": self.health,
            "boredom": self.boredom,
            "exhaustion": self.exhaustion,
            "is_alive": self.is_alive,
        }

    @staticmethod
    def from_dict(data):
        pet = Tamagotchi(data["name"])
        pet.hunger = data["hunger"]
        pet.health = data["health"]
        pet.boredom = data["boredom"]
        pet.exhaustion = data["exhaustion"]
        pet.is_alive = data["is_alive"]
        return pet
