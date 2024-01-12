import random
import time
import tkinter as tk

import keyboard
import txt


def game():
    words = [
        'dupa'
        'cycki'
        'chuj'
    ]

    word = random.randint(0, (len(words)-1))

    window = tk.Tk()
    window.title('Typing Speed')
    window.configure(bg='black')
    window.geometry('850x400')

    text = tk.Text(wrap=WORD, height=5, width=50, font="Arial 20")
    text.insert(END, words[word])
    text.place(x=60, y=40)


def callback():
    global x, i, count, icount, new_str, copy, idx, ln

    if txt.get() != '':
        if x == 1:
            i = 0
            x = 2
            count = 0
            icount = 0
            new_str = ' '
            copy = ' '
            idx = 0
            ln = 0

            global start
            start = time.time()

        if keyboard.is_pressed('space'):
            try:
                a = txt.get().split()[-1]
                if a != copy:
                    b = words[word].split()[-1]
                    if a == b:
                        count += 1
                        new_str = new_str + b + ' '
                        c = new_str + ' '.join(words[word].split()[i+1:])

                        idx = words[word].index(b, idx+ln)
