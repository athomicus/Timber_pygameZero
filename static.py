import pgzrun
from pgzero.game import PGZeroGame
from pgzero.builtins import Actor
from pgzero.screen import Screen

screen : Screen

FULLSCREEN = False
WIDTH = 800
HEIGHT = 600

BASE_WIDTH = 1920 #max how we should scale because of impoorted pictures
BASE_HEIGHT = 1080
background = Actor('background',pos=(0,0), anchor=(0,0) ) 
