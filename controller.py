# controller.py
import time
import tkinter as tk
from tkinter import messagebox
from model import load_text


def wpm_test(root):
    target_text = load_text()
    current_text = []
    errors = 0
    wpm = 0
    start_time = time.time()

    def update_wpm_label():
        nonlocal wpm
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 2)
        wpm_label.config(text=f"WPM: {wpm}")

    def check_completion():
        if current_text == list(target_text):
            messagebox.showinfo('Result', f"Your Typing Speed: {wpm} WPM")
            reset_text()
            update_wpm_label()

    def key_pressed(event):
        nonlocal errors
        nonlocal current_text
        pressed_key = event.char

        # Jeśli użytkownik wcisnął spację, to sprawdź poprzednie słowo
        if pressed_key == ' ':
            check_completion()
        else:
            # Dodaj warunek, aby uniknąć przekroczenia długości target_text
            if len(current_text) < len(target_text):
                target_char = target_text[len(current_text)]
                if pressed_key == target_char:
                    current_text.append(pressed_key)
                else:
                    errors += 1  # Zlicz błędy (jeśli potrzebujesz tej informacji)

                update_wpm_label()

    def reset_text():
        nonlocal target_text
        nonlocal current_text
        nonlocal errors
        nonlocal start_time
        nonlocal wpm

        target_text = load_text()
        current_text = []
        errors = 0
        start_time = time.time()
        wpm = 0

        # Zaktualizuj etykietę z tekstem
        text_to_write.config(text=target_text)

        # Wyczyść pole tekstowe
        textbox.delete(1.0, tk.END)

        # Zaktualizuj etykietę z WPM
        update_wpm_label()

    # Tworzenie nowego okna Toplevel
    top = tk.Toplevel(root)
    top.title("Fast and Furious test!")
    top.geometry("1000x600")
    top.configure(bg='black')

    # Etykieta z tekstem do przepisania
    text_to_write = tk.Label(top, text=target_text, font=("Helvetica", 16), fg="white", bg="black")
    text_to_write.pack(padx=20, pady=20)

    # Pole tekstowe do wprowadzania tekstu
    textbox = tk.Text(top, height=3, font=("Helvetica", 14))
    textbox.pack(padx=40, pady=40)

    # Etykieta z aktualnym WPM
    wpm_label = tk.Label(top, text=f"WPM: {wpm}", font=("Helvetica", 16), fg="white", bg="black")
    wpm_label.pack()

    # Dodaj obsługę zdarzeń klawiatury
    textbox.bind('<Key>', key_pressed)

    # Przycisk Reset
    reset_button = tk.Button(top, text="Reset", font=("Helvetica", 14), fg="white", bg="black", command=reset_text)
    reset_button.pack()
