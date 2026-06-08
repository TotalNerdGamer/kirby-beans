import pygame
import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes.Player import Player
from classes.Platform import Platform
from classes.mypos import myPos
from classes.myimg import myimg
from classes.cheese import Cheese
from classes.hudheart import HUDHeart
from classes.mousetrap import Mousetrap
from classes.Scene import Scene
class LevelScene(Scene):
    "Why don't we level the playing field?"
    def __init__(self,platforms,colls,hazards,x,y):
        self.platforms = platforms
        self.colls = colls
        self.hazards = hazards
        self.lvlright = 1280
        self.player = Player(x,y)
        self.basepos1=myPos(0,0)
        self.basepos2 = myPos(self.lvlright,0)
        self.scrollpoint = 3
        self.hearts=[HUDHeart(5,5,1),HUDHeart(70,5,2),HUDHeart(135,5,3)]
        self.bg = "cabinets"
        self.bg1 = myimg(0,0,f"backgrounds/{self.bg}.png")
        self.bg2 = myimg(1280,0,f"backgrounds/{self.bg}.png")