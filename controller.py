# controller.py

import time
import tkinter as tk
from tkinter import simpledialog, messagebox
from model import load_text, save_highscore, get_highscore


def wpm_test(master):

    total_errors = 0

    def calculate_wpm(end_time, start_time, text_entered, text_original):
        words = len(text_original.split())
        time_elapsed = end_time - start_time
        wpm = round((words / time_elapsed) * 60)

        # Calculate errors
        errors = total_errors
        return wpm, errors

    def prompt_for_nickname(wpm):
        nickname = simpledialog.askstring("New Highscore!", f"Congratulations! Your speed: {wpm} WPM. Enter your nickname:",
                                          parent=top)
        return nickname

    def highlight_text():
        nonlocal total_errors  # Użyj zmiennej globalnej w funkcji
        text_entered = text_entry.get("1.0", tk.END)
        text_entry.tag_remove("correct", "1.0", tk.END)
        text_entry.tag_remove("incorrect", "1.0", tk.END)

        current_errors = 0
        for i, (char_entered, char_original) in enumerate(zip(text_entered, text_to_type)):
            if i >= len(text_to_type):
                break
            tag = "correct"
            if char_entered != char_original:
                tag = "incorrect"
                current_errors += 1
            text_entry.tag_add(tag, f"1.{i}", f"1.{i + 1}")

        if current_errors > 0 and text_entry.get("1.0", tk.END)[-1] != '\n':
            total_errors += current_errors
    def submit_text():
        end_time = time.time()
        text_entered = text_entry.get("1.0", tk.END).strip()
        # Weryfikacja czy tekst został w pełni wpisany
        if text_entered != text_to_type:
            messagebox.showwarning("Warning", "Text does not match the source. Please check again.")
            return

        wpm, errors = calculate_wpm(end_time, start_time, text_entered, text_to_type)
        highscore, highscore_nickname = get_highscore()
        message = f"Your speed: {wpm} WPM with {errors} errors."

        if highscore is None or wpm > highscore:
            nickname = prompt_for_nickname(wpm)
            if nickname:
                save_highscore(wpm, nickname)
                message += f"\nCongratulations, {nickname}! Your new highscore is {wpm} WPM."
            else:
                message += "\nHighscore not saved as no nickname was entered."
        elif highscore is not None:
            message += f"\nCurrent highscore is {highscore} WPM by {highscore_nickname}."

        messagebox.showinfo("Result", message)
        restart_test()

    def restart_test():
        nonlocal start_time
        total_errors = 0
        text_entry.delete("1.0", tk.END)
        start_time = time.time()

    top = tk.Toplevel(master)
    top.title("WPM Test")
    top.geometry("1200x1000+250+100")
    top.configure(bg='black')

    text_to_type = load_text()
    if text_to_type is None:
        messagebox.showerror("Error", "Could not load the text.")
        return

    start_time = time.time()

    instruction_label = tk.Label(top, text="Type the text below as fast as you can:", font=("Helvetica", 14), fg="white", bg="black")
    instruction_label.pack(padx=20, pady = 20)

    text_label = tk.Label(top, text=text_to_type, font=("Helvetica", 20), fg="white", bg="black")
    text_label.pack(padx=20, pady= 20)

    text_entry = tk.Text(top, height=3, font=("Helvetica", 20))
    text_entry.pack(padx=20, pady=20)
    text_entry.bind("<KeyRelease>", lambda event: highlight_text())

    text_entry.tag_configure("correct", foreground="green")
    text_entry.tag_configure("incorrect", foreground="red")

    submit_button = tk.Button(top, text="Submit", font=("Helvetica", 14), fg="white", bg="black", command=submit_text)
    submit_button.pack(padx=20, pady = 20)
