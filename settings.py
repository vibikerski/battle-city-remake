import os
from pygame import font

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PATH = os.path.dirname(__file__) + os.path.sep

# Коди сцен гри
MENU_STATE = 0
GAME_STATE = 1
DEATH_STATE = 2
WIN_STATE = 3

font.init()
FONT = font.Font('freesansbold.ttf', 32)