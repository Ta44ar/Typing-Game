# app.py
import tkinter as tk
from view import StartScreen, MenuScreen


class App:
    def __init__(self, master):
        self.master = master
        self.screen1 = StartScreen(self.master)
        self.screen2 = MenuScreen(self.master)

        # Show the initial screen
    #     self.show_screen1()
    #     self.show_screen2()
    #
    # def show_screen1(self):
    #     # Hide Screen 2
    #     self.screen2.pack_forget()
    #
    #     # Show Screen 1
    #     self.screen1.pack()
    #
    # def show_screen2(self):
    #     # Hide Screen 1
    #     self.screen1.pack_forget()
    #
    #     # Show Screen 2
    #     self.screen2.pack()
        # self.frames = {
        #     "StartScreen": StartScreen(self),
        #     "MenuScreen": MenuScreen(self),
        # }

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
