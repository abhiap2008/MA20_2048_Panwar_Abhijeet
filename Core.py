#Abhijeet Singh Panwar
#MA-20
#05.02.2026
# --------- Contient la logique du jeu 2048 --------- #
# --------- Gère les déplacements, les fusions et les modifications de la grille --------- #

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Gfx import *
import random

game = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,2,0,0],]
winner = False
# ---------------------------------------- #
#       PACK4 FUNCTION
# ---------------------------------------- #
# ---------- Traite 4 cases d'une ligne ou colonne : déplace les zéros et fusionne les valeurs égales ---------- #
# ---------- Retourne les nouvelles valeurs après déplacement et fusion ---------- #
score = 0
def pack4(a,b,c,d):
    global score

# ----------------------------------------#
#       Passer les 0 à droite
# ----------------------------------------#
    cpt = 0
    if c == 0 and d>0:
        c, d = d, 0
        cpt += 1
    if b == 0 and c>0:
        b, c, d = c, d, 0
        cpt += 1
    if a == 0 and b>0:
        a, b, c, d = b, c, d, 0
        cpt += 1
# ----------------------------------------#
#       Fusion de gauche à droite
# ----------------------------------------#
    if a == b and a > 0:
        a = 2 * a
        score += a
        b, c, d = c, d, 0
        cpt += 1
    if b == c and b > 0:
        b = 2 * b
        score += b
        c, d = d, 0
        cpt += 1
    if c == d and c > 0:
        c = 2 * c
        score += c
        d = 0
        cpt += 1

    print("Les fusions se font en", cpt, "coups")
    return (a,b,c,d,cpt)


# ----------------------------------------#
#       Des tests
# ----------------------------------------#
#print(pack4(8,8,4,2))
#print(pack4(2,4,4,18))
#print(pack4(512,64,64,1024))
#print(pack4(128,128,128,128))
#print(pack4(4,16,512,128))
#print(pack4(4,4,4,4))

# ----------------------------------------#
#       MOVE DOWN
# ----------------------------------------#
# ---------- Cette fonction effectue le déplacement des tuiles vers le bas ---------- #
def down():
    cpt_total = 0
    for col in range(4):
        (game[3][col], game[2][col], game[1][col], game[0][col], cpt) = \
            (pack4(game[3][col], game[2][col], game[1][col], game[0][col]))
    cpt_total += cpt
    if cpt > 0:
        apparition()
    print(game)
    return cpt_total

# ----------------------------------------#
#       MOVE UP
# ----------------------------------------#
# --------- Cette fonction déplace les tuiles vers le haut --------- #
def up():
    cpt_total = 0
    for col in range(4):
        (game[0][col], game[1][col], game[2][col], game[3][col], cpt) = \
            (pack4(game[0][col], game[1][col], game[2][col], game[3][col]))
    cpt_total += cpt
    if cpt > 0:
        apparition()
    print(game)
    return cpt_total
# ----------------------------------------#
#       MOVE LEFT
# ----------------------------------------#
# ---------- Cette fonction déplace les tuiles vers la gauche ---------- #
def left():
    cpt_total = 0
    for line in range(4):
        (game[line][0], game[line][1], game[line][2], game[line][3], cpt) = \
            (pack4(game[line][0], game[line][1], game[line][2], game[line][3]))
    cpt_total += cpt
    if cpt > 0:
        apparition()
    print(game)
    return cpt_total
# ----------------------------------------#
#       MOVE RIGHT
# ----------------------------------------#
# ---------- Cette fonction déplace les tuiles vers la droite ---------- #
def right():
    cpt_total = 0
    for line in range(4):
        (game[line][3], game[line][2], game[line][1], game[line][0], cpt) = \
            (pack4(game[line][3], game[line][2], game[line][1], game[line][0]))
    cpt_total += cpt
    if cpt > 0:
        apparition()
    print(game)
    return cpt_total

# --------- C'est pour afficher une nouvelle tuile dans une case vide
def apparition():
# ---------- Affiche un message pour signaler qu'un nouveau bloc va apparaître
    print("nouvelle block")
# ---------- Choisit aléatoirement un nombre entre 1 et 10
    random_nb = random.randint(1, 10)
# ---------------------------------------------------------------------------#
# Définit la valeur du bloc : 2 avec 80% de chance, 4 avec 20% de chance
# ---------------------------------------------------------------------------#
    if random_nb <= 8:
        numéro = 2
    else:
        numéro = 4
# ----------------------------------------------------------------------#
#   Boucle jusqu'à trouver une case vide pour placer le nouveau bloc
# ----------------------------------------------------------------------#
    while True:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
# ----------------------------------------------------------------------#
#   Si la case est vide, on place le bloc et on sort de la boucle
# ----------------------------------------------------------------------#
        if game[row][col] == 0:
            game[row][col] = numéro
            break

# ------------------------------------------------------- #
#       Test gagné pour vérifer que 2048 est atteint      #
# ------------------------------------------------------- #

def test_fini():
    global winner
    for line in range(4):
        for col in range(4):
# ------------------------------------------------------- #
#       Vérifier qu'il n'y a pas plus grand que 2048      #
# ------------------------------------------------------- #
            if game[line][col] == 2048 and winner == False:
                messagebox.showinfo("Gagné", "Bravo ! Vous avez atteint le but 2048")
                winner = True
# --------------------- #
#       Test perdu      #
# --------------------- #

def test_empty_case():
    winner = False
    for line in range(4):
        for col in range(4):
# ------------------------------------------------------- #
#       Vérifier s'il en reste encore des cases vides     #
# ------------------------------------------------------- #
            if game[line][col] == 0:
                return # pas perdu
# ----------------------------------------------------------- #
#       Vérifier s'il en reste encore des fusions possibles    #
# ----------------------------------------------------------- #
    for line in range(4):       # Vérifie de Gauche à droite
        for col in range(3):    # Pour chaque ligne
            if game[line][col] == game[line][col + 1]: # compare la case actuelle avec celle de droite
                return
    for col in range(4):        # Vérifie de haut vers bas
        for line in range(3):   # Vérifie chaque colonne
            if game[line][col] == game[line + 1 ][col]:     # compare la case actuelle avec celle en dessous
                return      # pas de fussion possible
    messagebox.showinfo("Perdu","Dommage vous avez perdu !")
