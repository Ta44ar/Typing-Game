# app.py
import tkinter as tk
from tkinter import ttk
from view import StartScreen, MenuScreen
from pygame import mixer
from PIL import Image, ImageTk


def resize_image(path, width, height):
    original_image = Image.open(path)
    resized_image = original_image.resize((width, height))
    tk_image = ImageTk.PhotoImage(resized_image)
    return tk_image


def stop_music():
    mixer.music.stop()


class App:
    def __init__(self, master):
        self.master = master

        # Inicjalizacja modułu mixer z pygame
        mixer.init()

        # Załaduj utwór muzyczny
        mixer.music.load("Gopnik.mp3")

        # Rozpocznij odtwarzanie muzyki
        mixer.music.play(loops=-1)  # loops=-1 oznacza, że utwór będzie odtwarzany w nieskończoność

        self.screen1 = StartScreen(self.master)
        self.screen2 = MenuScreen(self.master)

        # Dodaj przycisk do zatrzymania muzyki z ikoną
        stop_image = resize_image("mutek.png", width=32, height=32)
        stop_button = tk.Button(master, image=stop_image, command=stop_music)
        stop_button.image = stop_image  # Zapisz referencję do obiektu obrazu, aby uniknąć problemów z GC
        stop_button.pack(pady=20)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
