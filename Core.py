#Abhijeet Singh Panwar
#MA-20
#05.02.2026
import Gfx
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Gfx import *

game = [[0,2,0,0],
        [0,2,2,0],
        [0,2,2,0],
        [0,0,0,0],]
def pack4(a,b,c,d):
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
    if a == b and a>0 :
        a, b, c, d = 2*a, c, d, 0
        cpt += 1
    if b == c and b>0 :
        b, c, d  = 2*b, d, 0
        cpt += 1
    if c == d and c>0 :
        c, d = 2*c, 0
        cpt += 1

    print("Les fusions se font en", cpt, "coups")
    return (a,b,c,d, )


# ----------------------------------------#
#       Des tests
# ----------------------------------------#
#print(pack4(8,8,4,2))
print(pack4(2,4,4,18))
print(pack4(512,64,64,1024))
print(pack4(128,128,128,128))
print(pack4(4,16,512,128))
print(pack4(4,4,4,4))


def down():
    cpt_total = 0
    for col in range(4):
        (game[3][col], game[2][col], game[1][col], game[0][col]) = pack4(game[3][col], game[2][col], game[1][col],
                                                                      game[0][col])
    print(game)

def up():
    for col in range(4):
        (game[0][col], game[1][col], game[2][col], game[3][col]) = pack4(game[0][col], game[1][col], game[2][col],
                                                                         game[3][col])
    print(game)

def left():
    for line in range(4):
        (game[line][0], game[line][1], game[line][2], game[line][3]) = pack4(game[line][0], game[line][1], game[line][2],
                                                                         game[line][3])
    print(game)


def right():
    for line in range(4):
        (game[line][3], game[line][2], game[line][1], game[line][0]) = pack4(game[line][3], game[line][2], game[line][1],
                                                                              game[line][0])
    print(game)





