from __future__ import annotations
import pygame
import sys
import os
import json


sys.path.append(os.path.abspath("./src"))
from classes.Scene import Scene
from main.INS import resolvename
class DeathScene(Scene):
    "It comes for us all in the end."
    def __init__(self,switchscene):
        super().__init__(switchscene)
        self.frame = 0
        self.shakepath = [(0,0),(0,-1),(0,1),(1,0),(-1,0),(-1,1),(0,0)]
        self.shakemult = 3
        
        self.target = 2
        with (open("data.json")) as f:
            self.lives = json.load(f)["lives"]
        self.text = f"Lives remaining: {self.lives}"
        if self.lives <= 0:
            self.shakemult = 5
    def draw(self,screen: pygame.Surface):
        screen.fill("black")
        font = pygame.Font(None,40)
        shakeindex = max(0,min(self.frame - 60, len(self.shakepath)-1))
        shake = self.shakepath[shakeindex]
        txt = font.render(f"Lives: {max(self.lives,0)}",True,(255,255,255))
        textpos = txt.get_rect(centerx=screen.get_width() / 2 + shake[0]*self.shakemult, centery=360+shake[1]*self.shakemult)
        screen.blit(txt,textpos)
    def update(self,dt):
        self.frame += 1
        if self.frame >= 120 and (self.lives != -1):
            with (open("data.json","r")) as f:
                dct = json.load(f)
            dct["lives"] = self.lives
            with open("data.json","w") as f:
                json.dump(dct,f)
            self.switchscene(self.target)
        elif self.frame >= 120:
            self.switchscene(self.target)
        elif self.frame == 60:
            self.lives -= 1
        elif self.frame == 1 and self.lives == 0:
            self.target = (resolvename("Game Over"))