# controller.py

import time
import tkinter as tk
from tkinter import messagebox
from model import load_text, save_highscore, get_highscore

def wpm_test(master):
    def calculate_wpm(end_time, start_time, text_entered):
        words = len(text_entered.split())
        time_elapsed = end_time - start_time
        wpm = round((words / time_elapsed) * 60)
        return wpm

    def submit_text():
        end_time = time.time()
        text_entered = text_entry.get("1.0", tk.END)
        wpm = calculate_wpm(end_time, start_time, text_entered)
        highscore = get_highscore()
        if highscore is None or wpm > highscore:
            save_highscore(wpm, "YourName")  # Replace with a method to get the user's name
            messagebox.showinfo("New Highscore!", f"Congratulations! Your new highscore is {wpm} WPM.")
        else:
            messagebox.showinfo("Result", f"Your speed: {wpm} WPM. Highscore: {highscore} WPM.")

        top.destroy()

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