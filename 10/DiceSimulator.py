import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import time


class DiceSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Simulator")

        self.result_label = tk.Label(self.master, text="Wynik:")
        self.result_label.pack(pady=10)

        self.image_label = tk.Label(self.master)
        self.image_label.pack(pady=10)

        self.roll_button = tk.Button(self.master, text="Rzuć kostką", command=self.roll_dice)
        self.roll_button.pack(pady=10)

    def roll_dice(self):
        self.result_label.config(text="Wynik:")

        # Animacja losowania
        for _ in range(10):
            result = randint(1, 6)
            self.display_result(result)
            self.master.update()  # Force update do pokazywania zmian kostki
            time.sleep(0.05)  # Dostosowywanie długości pokazania poszczególnego zdjęcia

        # Wyświetlenie finalnego 'rzutu'
        self.display_result(result)

    def display_result(self, result):
        self.result_label.config(text=f"Wynik: {result}")

        # Obsługa obrazków
        image_path = f"images/dice_{result}.png"
        try:
            image = Image.open(image_path)
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo
        except FileNotFoundError:
            print("Brak pliku z obrazkiem dla kostki o numerze:", result)


def main():
    root = tk.Tk()
    DiceSimulator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
