# controller.py
import tkinter as tk
from view import StartScreen, MenuScreen


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.frames = {
            "StartScreen": StartScreen(self),
            "MenuScreen": MenuScreen(self),
        }

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()


def function():
    pass


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
