from tkinter import *

import random

import tkinter.font as font

root = Tk()

root.geometry("700x300")

root.title("Rock, Paper, Scissors")

app_font = font.Font(size = 12)

player_score = 0

computer_score = 0

options = [('rock', 0),('paper', 1), ('scissors', 2)]

def computer_wins():
    global computer_score, player_score
    computer_score = computer_score + 1
    winner_label.config(text = "Computer Wins!")
    cs_label.config(text = 'Computer Score : '+str(computer_score))
    ps_label.config(text = 'Player Score : '+str(player_score))

def player_wins():
    global computer_score, player_score
    player_score = player_score + 1
    winner_label.config(text = "Player Wins!")
    cs_label.config(text = 'Computer Score : '+str(computer_score))
    ps_label.config(text = 'Player Score : '+str(player_score))

def tie():
    global computer_score, player_score
    computer_score = computer_score
    player_score = player_score
    winner_label.config(text = "Tie!")
    cs_label.config(text = 'Computer Score : '+str(computer_score))
    ps_label.config(text = 'Player Score : '+str(player_score))

def get_computer_choice():
    return random.choice(options)



title_label = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')

title_label.pack()

winner_label = Label(text = "Let's Start The Game...", font = font.Font(size = 15), fg = 'green')

winner_label.pack(pady = 8)

frame = Frame(root)

frame.pack()

po_label = Label(frame, text = 'player options', font = app_font, fg = 'grey')

po_label.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(frame, text = "Rock", width = 15, bd = 0, bg = 'pink', pady = 5)

rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(frame, text = "Paper", width = 15, bd = 0, bg = 'green', pady = 5)

paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(frame, text = "Scissors", width = 15, bd = 0, bg = 'blue', pady = 5)

scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

score_label = Label(frame, text = "Score:", font = app_font, fg = "grey")

score_label.grid(row = 2, column = 0)

pc_label = Label(frame, text = "Player Choice : --", font = app_font)

pc_label.grid(row = 3, column = 1, pady = 5)

ps_label = Label(frame, text = "Player Score : --", font = app_font)

ps_label.grid(row = 3, column = 2, pady = 5)

cc_label = Label(frame, text = "Computer Choice : --", font = app_font)

cc_label.grid(row = 4, column = 1, pady = 5)

cs_label = Label(frame, text = "Computer Score : --", font = app_font)

cs_label.grid(row = 4, column = 2, pady = 5)

root.mainloop()

