# view.py
import time
import tkinter as tk
from tkinter import messagebox
from model import get_highscore


class StartScreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Typing Game")
        self.master.geometry("1200x800")
        self.master.configure(bg='black')

        title_label = tk.Label(self.master, text="Super Mega Impressive Typing Game Deluxe!", font=("Helvetica", 24),
                               fg="green", bg="black")
        title_label.pack(pady=200)

        colors = ["red", "green", "yellow", "blue", "magenta"]
        for _ in range(1):
            for color in colors:
                title_label.config(fg=color)
                self.master.update()
                time.sleep(0.2)
                self.master.update()
                time.sleep(0.1)

        title_label.config(fg="white")


class MenuScreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.master.title("Typing Game")
        self.master.geometry("1200x800")
        self.master.configure(bg='black')

        menu_label = tk.Label(self.master, text="How fast you think you can type? Select difficulty level:",
                              font=("Helvetica", 16), fg="white", bg="black")
        menu_label.pack(padx=20, pady=20)

        buttonframe = tk.Frame(self.master)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.rowconfigure(0, weight=1)
        buttonframe.rowconfigure(1, weight=1)
        buttonframe.rowconfigure(2, weight=1)
        buttonframe.rowconfigure(3, weight=1)

        button1 = tk.Button(buttonframe, text="Fast and Furious!  (easy mode - typing speed only)",
                            font=("Helvetica", 14), fg="white", bg="black",
                            command=lambda: self.display_message("Button 1"))
        button1.grid(row=1, column=0, sticky=tk.W + tk.E)

        button2 = tk.Button(buttonframe, text="Watch your steps!  (hard mode - typing speed + errors counter)",
                            font=("Helvetica", 14), fg="white", bg="black",
                            command=lambda: self.display_message("Button 2"))
        button2.grid(row=2, column=0, sticky=tk.W + tk.E)

        button3 = tk.Button(buttonframe, text="Current highscore",
                            font=("Helvetica", 14), fg="white", bg="black", command=self.display_highscore_message)
        button3.grid(row=3, column=0, sticky=tk.W + tk.E)

        button4 = tk.Button(buttonframe, text="Quit",
                            font=("Helvetica", 14), fg="white", bg="black", command=self.quitting_app)
        button4.grid(row=4, column=0, sticky=tk.W + tk.E)

        buttonframe.pack(fill='x')

    @staticmethod
    def display_message(button_text):
        messagebox.showinfo("Button Clicked", f"You clicked {button_text}!")

    def display_highscore_message(self):
        try:
            highscore = self.get_highscore()
            messagebox.showinfo("Highscore", f"Current highscore is {highscore} WPM.")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Highscore file not found. {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error while getting highscore. {str(e)}")

    @staticmethod
    def get_highscore():
        return get_highscore()

    def quitting_app(self):
        messagebox.showinfo("Exiting", "Closing the application...")
        self.master.destroy()


def display_text(root, target, wpm):
    root.title("Typing Game")
    root.geometry("800x600")
    root.configure(bg='black')

    # Usuń istniejące elementy z okna głównego (jeśli są)
    for widget in root.winfo_children():
        widget.destroy()

    # Etykieta z tekstem do przepisania
    text_to_write = tk.Label(root, text=target,
                             font=("Helvetica", 16), fg="white", bg="black")
    text_to_write.pack(padx=20, pady=20)

    # Pole tekstowe do wprowadzania tekstu
    textbox = tk.Text(root, height=3, font=("Helvetica", 14))
    textbox.pack(padx=40, pady=40)

    # Etykieta z aktualnym WPM
    wpm_counter = tk.Label(root, text=f"WPM: {wpm}",
                           font=("Helvetica", 16), fg="white", bg="black")
    wpm_counter.pack()
