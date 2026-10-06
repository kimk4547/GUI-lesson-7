from tkinter import *

import random

import tkinter.font as font

root = Tk()

root.geometry("700x300")

root.title("Flip a Coin")

app_font = font.Font(size = 12)

options = ['heads', 'tails']

def get_computer_choice():
    result = random.choice(options)
    end_label.config(text = result)


h_or_t_label = Label(root, text = "Heads or Tails?", font = font.Font(size = 18))

h_or_t_label.pack(pady = 20)

flip_btn = Button(root, text = "Flip Coin", font = app_font, bg = "gold", fg = "black", command = get_computer_choice)

flip_btn.pack(pady = 20)

end_label = Label(root, font = app_font, fg = "blue")

end_label.pack(pady = 20)

root.mainloop()

