# view.py
import time
import tkinter as tk
from tkinter import messagebox
from controller import wpm_test
from model import get_highscore, load_text


class StartScreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Typing Game")
        self.master.geometry("1200x800+200+200")
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

        # menu_label = tk.Label(self.master, text="How fast you think you can type? Select difficulty level:",
        menu_label = tk.Label(self.master, text="How fast you think you can type?",
                              font=("Helvetica", 16), fg="white", bg="black")
        menu_label.pack(padx=20, pady=20)

        buttonframe = tk.Frame(self.master)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.rowconfigure(0, weight=1)
        buttonframe.rowconfigure(1, weight=1)
        buttonframe.rowconfigure(2, weight=1)
        # buttonframe.rowconfigure(3, weight=1)

        # button1 = tk.Button(buttonframe, text="Fast and Furious!  (easy mode - typing speed only)",
        button1 = tk.Button(buttonframe, text="Play game",
                            font=("Helvetica", 14), fg="white", bg="black",
                            command=self.start_wpm_test)
        button1.grid(row=1, column=0, sticky=tk.W + tk.E)

        # button2 = tk.Button(buttonframe, text="Watch your steps!  (hard mode - typing speed + errors counter)",
        #                     font=("Helvetica", 14), fg="white", bg="black",
        #                     command=lambda: self.display_message("Button 2"))
        # button2.grid(row=2, column=0, sticky=tk.W + tk.E)

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
            highscore, nickname = self.get_highscore()
            if highscore is not None:
                messagebox.showinfo("Highscore", f"Current highscore is {highscore} WPM by {nickname}.")
            else:
                messagebox.showinfo("Highscore", "No highscore set yet.")
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

    def start_wpm_test(self):
        # Wywołaj funkcję wpm_test z aktualnym obiektem Tkinter (self.master)
        wpm_test(self.master)


def display_text(wpm):
    # Wczytaj losowy ciąg znaków z modelu
    target_text = load_text()
    current_text = target_text

    # Tworzenie nowego okna Toplevel
    top = tk.Toplevel()
    top.title("Fast and Furious test!")
    top.geometry("800x600+200+200")
    top.configure(bg='black')

    # Usuń istniejące elementy z nowego okna (jeśli są)
    for widget in top.winfo_children():
        widget.destroy()

    # Etykieta z tekstem do przepisania
    text_to_write = tk.Label(top, text=target_text,
                             font=("Helvetica", 16), fg="white", bg="black")
    text_to_write.pack(padx=20, pady=20)

    # Pole tekstowe do wprowadzania tekstu
    textbox = tk.Text(top, height=3, font=("Helvetica", 14))
    textbox.pack(padx=40, pady=40)

    # Etykieta z aktualnym WPM
    wpm_counter = tk.Label(top, text=f"WPM: {wpm}",
                           font=("Helvetica", 16), fg="white", bg="black")
    wpm_counter.pack()

    reset_button = tk.Button(top, text="Reset", font=("Helvetica", 14), fg="white", bg="black",
                             command=lambda: reset_text(text_to_write, textbox, wpm_counter, current_text))
    reset_button.pack()


def reset_text(text_label, text_box, wpm_label, current_text):
    new_text = load_text()

    # Sprawdź, czy nowy tekst jest różny od obecnego
    while new_text == current_text:
        new_text = load_text()

    # Zaktualizuj etykietę z tekstem
    text_label.config(text=new_text)

    # Wyczyść pole tekstowe
    text_box.delete(1.0, tk.END)

    # Zaktualizuj etykietę z WPM
    wpm_label.config(text="WPM: 0")