# controller.py

import time
import tkinter as tk
from tkinter import simpledialog, messagebox
from model import load_text, save_highscore, get_highscore

def wpm_test(master):
    def calculate_wpm(end_time, start_time, text_entered, text_original):
        words = len(text_original.split())
        time_elapsed = end_time - start_time
        wpm = round((words / time_elapsed) * 60)

        # Calculate errors
        errors = sum(1 for a, b in zip(text_entered, text_original) if a != b)
        return wpm, errors

    def prompt_for_nickname(wpm):
        nickname = simpledialog.askstring("New Highscore!", f"Congratulations! Your speed: {wpm} WPM. Enter your nickname:",
                                          parent=top)
        return nickname

    def submit_text():
        end_time = time.time()
        text_entered = text_entry.get("1.0", tk.END).strip()
        wpm, errors = calculate_wpm(end_time, start_time, text_entered, text_to_type)
        highscore = get_highscore()
        message = f"Your speed: {wpm} WPM with {errors} errors."

        if highscore is None or wpm > highscore:
            nickname = prompt_for_nickname(wpm)
            if nickname:
                save_highscore(wpm, nickname)
                message += f"\nCongratulations, {nickname}! Your new highscore is {wpm} WPM."
            else:
                message += "\nHighscore not saved as no nickname was entered."

        messagebox.showinfo("Result", message)
        restart_test()

    def restart_test():
        nonlocal start_time
        text_entry.delete("1.0", tk.END)
        start_time = time.time()

    top = tk.Toplevel(master)
    top.title("WPM Test")

    text_to_type = load_text()
    if text_to_type is None:
        messagebox.showerror("Error", "Could not load the text.")
        return

    start_time = time.time()

    instruction_label = tk.Label(top, text="Type the text below as fast as you can:")
    instruction_label.pack()

    text_label = tk.Label(top, text=text_to_type, wraplength=500)
    text_label.pack()

    text_entry = tk.Text(top, height=10, width=50)
    text_entry.pack()

    submit_button = tk.Button(top, text="Submit", command=submit_text)
    submit_button.pack()
