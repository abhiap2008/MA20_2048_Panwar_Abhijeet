# Abhijeet Singh Panwar
# MA-20
# 05.02.2026
# ----------- Gère l'interface graphique du jeu 2048 avec Tkinter ----------- #
# ----------- Affiche la grille, les couleurs et détecte les touches du clavier ----------- #

import tkinter as tk
from Dict_color import *
from Core import *

import time
start_time = time.time()


#game = [[0,0,0,0],
#        [0,0,2,0],
#        [0,0,0,0],
#        [2,0,0,0],]
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
dx = 10      #Distance Horizonale
dy = 10     #Distance Vertical


#----------------------------------------#
#       CREATION OF WINDOW
#----------------------------------------#
window = tk.Tk()
window.title("Panwar")
window.geometry("600x600")
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
# ---------- Met à jour l'affichage de la grille 2048 ---------- #
# ---------- Affiche les nombres et applique la couleur correspondante ---------- #

def display():
    for line in range(len(game)):
        for col in range(len(game[0])):
            if game[line][col] > 0:
                labels[line][col].config(text=game[line][col], bg=color[game[line][col]])
            else:
                labels[line][col].config(text="", bg=color[game[line][col]])
    from Core import score
    lbl_score_value.config(text=str(score))


frm_separation=Frame(window)
frm_separation.pack(pady=10, padx=10)
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


#----------------------------------------#
#       FRAME MEILLEUR SCORE
#----------------------------------------#
frm_meileur_score = Frame(window, bg="blue")
frm_meileur_score.pack(pady=10, padx=10)

lbl_best = Label(frm_meileur_score, text="Meilleur Score", font=("Arial", 15), bg="grey")
lbl_best.pack(side="left", padx=50)

#----------------------------------------#
#       QUIT BUTTTON
#----------------------------------------#

btn_quitter = Button(frm_meileur_score, text="Quitter", font=("Arial", 15), command=window.quit, bg="grey")
btn_quitter.pack(side="left", padx=50)

#----------------------------------------#
#           Chronomètre
#----------------------------------------#
def update_timer():
    elapsed = int(time.time() - start_time)
    lbl_timer.config(text=str(elapsed) + "s")
    window.after(1000, update_timer)
#----------------------------------------#
#       FRAME SCORE
#----------------------------------------#
frm_score = Frame(frm_meileur_score, bg="blue")
frm_score.pack(side="left", padx=40)

lbl_score_text = Label(frm_score, text="Score", font=("Arial", 15), bg="grey")
lbl_score_text.pack()

lbl_score_value = Label(frm_score, text="0", font=("Arial", 15), bg="grey")
lbl_score_value.pack(pady=10)

lbl_timer = Label(frm_meileur_score, text="0s", font=("Arial", 15), bg="grey")
lbl_timer.pack(side="left", padx=20)

def restart():
    import Core
    global start_time

    start_time = time.time()  # reset timer
    Core.score = 0            # reset score

    for i in range(4):
        for j in range(4):
            Core.game[i][j] = 0

btn_restart = Button(frm_meileur_score, text="Restart", command=restart, bg="blue")
btn_restart.pack(side="left", padx=20)
# ------------------------------------------------------------------------------#
#       Fonction appellé à chaque fois le touche du clavier est pressé
# ------------------------------------------------------------------------------#
from Core import *
def key_pressed(event):
    touche = event.keysym
# -------------------------------------------------------------------- #
#      Touche S/s ou  la flèche bas : déplace les tuiles vers le bas
# -------------------------------------------------------------------- #
    if touche=="Down" or touche=="s" or touche=="S":
        down()
# -------------------------------------------------------------------------- #
#      Touche W/w ou  la flèche en haut : déplace les tuiles vers le haut
# -------------------------------------------------------------------------- #
    if touche == "Up" or touche=="w" or touche=="W":
        up()
# -------------------------------------------------------------------------- #
#      Touche A/a ou  la flèche gauche : déplace les tuiles vers la gauche
# -------------------------------------------------------------------------- #
    if touche == "Left" or touche=="a" or touche=="A":
        left()
# ---------------------------------------------------------------------------- #
#      Touche D/d ou  la flèche droite : déplace les tuiles vers la droite
# ---------------------------------------------------------------------------- #
    if touche == "Right" or touche=="d" or touche=="D":
        right()
    display()
    test_fini()
    test_empty_case()
    update_timer()
window.bind("<Key>", key_pressed)
