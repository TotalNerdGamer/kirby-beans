import json
import os

import pygame
from myimg import myimg
from Player import Player
import math

class Cheese(myimg):
    def __init__(self,x,y):
        super().__init__(x,y,"collectibles/cheese/cheese.png")
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        self.pos=pygame.Vector2(x-self.imgsurf.get_width()/2,y-self.imgsurf.get_height()/2)
        self.yoffval = 0
        self.basey = self.pos.y
        self.yoff=math.sin(self.yoffval)
        self.frame=0
        self.playing=False
    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,self.imgsurf.get_width(),self.imgsurf.get_height())
    def update(self,player: Player):
        self.yoffval+=1
        self.yoff = 10*math.sin(self.yoffval/50)
        self.pos.y = self.basey + self.yoff
        if self.playing:
            if self.frame < 5:
                self.frame += 1
            elif self.frame == 5:
                self.kill = True
                player.cheese += 1
        self.img=f"collectibles/cheese/{["cheese","cheese_collect"][min(self.frame,1)]}.png"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        