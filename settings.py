import pygame as pg
vec = pg.math.Vector2

import tkinter as tk
root = tk.Tk()



# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

DARKRED = (102, 3, 19)

CYAN = (128, 247, 216)
LIGHTGREEN =(129, 237, 91)
MIDDLERED =(181, 43, 33)
CLOUDYWHITE =(217, 224, 240)
BROWN =(107, 75, 37)
MIDDLEGREY =(63, 70, 76)
MIDDLEYELLOW =(246, 246, 116)
MIDDLEORANGE =(224, 131, 53)
MIDDLEPINK =(219, 95, 183)
MIDDLEGREEN =(59, 126, 57)
MIDDLEBLUE = (26, 45, 201)
MIDDLEPURPLE =(100, 50, 181)



# game settings
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
'''WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12'''
WIDTH = int(screen_width -screen_width*(7/15))
HEIGHT = int(screen_height -screen_height*(13/45))

FPS = 25
TITLE = "Game"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


# Player settings
PLAYER_SPEED = 135
PLAYER_RUN_SPEED = 200
PLAYER_IMG = 'sprite_2.png' #this is the image character initially spawns with
PLAYER_HIT_RECT = pg.Rect(0, 0, 27, 60)