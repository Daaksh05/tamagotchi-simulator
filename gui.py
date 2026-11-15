import io
import tkinter as tk
from contextlib import redirect_stdout
from tkinter import messagebox, ttk

from tamagotchi import Tamagotchi
import game
import storage


class TamagotchiGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Tamagotchi Simulator")
        self.root.geometry("520x560")
        self.root.resizable(False, False)

        self.pets = {
            "Tama": Tamagotchi("Tama"),
            "Mochi": Tamagotchi("Mochi"),
            "Pochi": Tamagotchi("Pochi"),
        }

        self.selected_name = tk.StringVar(value="Tama")

        self.build_layout()
        self.refresh_status()

    def build_layout(self):
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack(fill="x")

        tk.Label(top_frame, text="Select pet:", font=("Arial", 11)).pack(side="left", padx=(15, 5))

        self.pet_menu = ttk.Combobox(
            top_frame,
            textvariable=self.selected_name,
            values=list(self.pets.keys()),
            state="readonly",
            width=15,
        )
        self.pet_menu.pack(side="left")
        self.pet_menu.bind("<<ComboboxSelected>>", lambda e: self.refresh_status())

        status_frame = tk.LabelFrame(self.root, text="Status", padx=15, pady=10)
        status_frame.pack(fill="x", padx=15, pady=10)

        self.status_label = tk.Label(status_frame, text="", justify="left", font=("Courier", 11))
        self.status_label.pack(anchor="w")

        self.health_bar = self.add_bar(status_frame, "Health")
        self.hunger_bar = self.add_bar(status_frame, "Hunger")
        self.boredom_bar = self.add_bar(status_frame, "Boredom")
        self.exhaustion_bar = self.add_bar(status_frame, "Exhaustion")

        action_frame = tk.LabelFrame(self.root, text="Actions", padx=15, pady=10)
        action_frame.pack(fill="x", padx=15, pady=5)

        buttons = [
            ("Feed", self.feed),
            ("Play", self.play),
            ("Sleep", self.sleep),
            ("Heal", self.heal),
        ]
        for text, command in buttons:
            tk.Button(action_frame, text=text, width=10, command=command).pack(side="left", padx=5)

        game_frame = tk.LabelFrame(self.root, text="Game", padx=15, pady=10)
        game_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(game_frame, text="Statistics", width=10, command=self.show_stats).pack(side="left", padx=5)
        tk.Button(game_frame, text="Save", width=10, command=self.save).pack(side="left", padx=5)
        tk.Button(game_frame, text="Load", width=10, command=self.load).pack(side="left", padx=5)

        log_frame = tk.LabelFrame(self.root, text="Log", padx=10, pady=10)
        log_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.log_text = tk.Text(log_frame, height=10, state="disabled", wrap="word")
        self.log_text.pack(fill="both", expand=True)

    def add_bar(self, parent, label):
        row = tk.Frame(parent)
        row.pack(fill="x", pady=2)

        tk.Label(row, text=f"{label}:", width=11, anchor="w").pack(side="left")
        bar = ttk.Progressbar(row, length=250, maximum=100)
        bar.pack(side="left", padx=5)

        return bar

    def current_pet(self):
        return self.pets[self.selected_name.get()]

    def run_action(self, action):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            action()

        output = buffer.getvalue().strip()
        if output:
            self.log(output)

        self.refresh_status()

        if not self.current_pet().is_alive:
            messagebox.showinfo("Pet died", f"{self.current_pet().name} has died.")

    def feed(self):
        self.run_action(self.current_pet().feed)

    def play(self):
        self.run_action(self.current_pet().play)

    def sleep(self):
        self.run_action(self.current_pet().sleep)

    def heal(self):
        self.run_action(self.current_pet().heal)

    def show_stats(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            game.show_statistics(self.pets)

        self.log(buffer.getvalue().strip())

    def save(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            storage.save_game(self.pets)

        self.log(buffer.getvalue().strip())

    def load(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            loaded = storage.load_game()

        self.log(buffer.getvalue().strip())

        if loaded is not None:
            self.pets = loaded
            self.pet_menu["values"] = list(self.pets.keys())
            self.selected_name.set(list(self.pets.keys())[0])
            self.refresh_status()

    def refresh_status(self):
        pet = self.current_pet()
        status = "Alive" if pet.is_alive else "Dead"

        self.status_label.config(text=f"{pet.name}  —  {status}")
        self.health_bar["value"] = pet.health
        self.hunger_bar["value"] = pet.hunger
        self.boredom_bar["value"] = pet.boredom
        self.exhaustion_bar["value"] = pet.exhaustion

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")


def main():
    root = tk.Tk()
    TamagotchiGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
