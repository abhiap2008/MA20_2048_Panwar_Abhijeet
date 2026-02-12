from tkinter import *
import tkinter as tk
from Dict_color import *

game = [[0,0,0,0],
        [0,0,1,0],
        [0,0,0,0],
        [1,0,0,0],]
game = [[2,4,8,16],
        [32,64,128,256],
        [512,1024,2048,4096],
        [8192,0,0,0],]


#----------------------------------------#
#       CREATE DIMENSION
#----------------------------------------#
labels = [[None,None,None,None],
          [None,None,None,None],
          [None,None,None,None],
          [None,None,None,None],]


#----------------------------------------#
#       DISTANCE BETWEEN LABELS
#----------------------------------------#
dx = 5      #Distance Horizonale
dy = 5     #Distance Vertical


#----------------------------------------#
#       CREATION OF WINDOW
#----------------------------------------#
window = tk.Tk()
window.title("Panwar")
window.geometry("500x550")
window.configure(background="blue")


#----------------------------------------#
#       TITLE
#----------------------------------------#
frm_title= Frame(window)
frm_title.pack(pady=10, padx=10)
lbl_title=Label(frm_title, text="2048", font=("Arial", 35), background="grey")
lbl_title.pack()


#----------------------------------------#
#      DISPLAY OF GRID
#----------------------------------------#
def display():
    for line in range(len(game)):
        for col in range(len(game[0])):
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=color[game[line][col]])
            else:
                labels[line][col].config(text="", bg=color[game[line][col]])


#----------------------------------------#
#       CREATING LABEL & POSITIONING
#----------------------------------------#
frm_game=Frame(window, bg="grey")
frm_game.pack()

for line in range(len(game)):
    for col in range(len(game[line])):
        # CREATION WITHOUT PLACEMENT
        labels[line][col] = Label(frm_game, text =game[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg=color[game[line][col]])
        # LABEL POSITIONING IN WINDOWS
        labels[line][col].grid (row=line+1,column=col,padx=dx,pady=dy)

frm_score=Frame(window, bg="grey")
frm_score.pack(pady=10, padx=10)
lbl_score=Label(frm_score, text="Meilleur Score", font=("Arial", 20), background="grey")
lbl_score.pack(side=BOTTOM)
