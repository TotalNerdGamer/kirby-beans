from __future__ import annotations
import pygame
import sys
import os
import json


sys.path.append(os.path.abspath("./src"))
from tkinter.messagebox import showerror
from functools import partial
from sys import exit
import subprocess
from time import sleep
from helpfulstuff.help import *
import threading
from classes.Scene import Scene
class DeathScene(Scene):
    "It comes for us all in the end."
    def __init__(self,switchscene):
        super().__init__(switchscene)
        self.frame = 0
        with (open("data.json")) as f:
            self.lives = json.load(f)["lives"]
        self.text = f"Lives remaining: {self.lives}"
    def draw(self,screen: pygame.Surface):
        screen.fill("black")
        font = pygame.Font(None,32)
        txt = font.render(f"Lives: {self.lives}",True,(255,255,255))
        textpos = txt.get_rect(centerx=screen.get_width() / 2, centery=360)
        screen.blit(txt,textpos)
    def update(self,dt):
        self.frame += 1
        if self.frame >= 120 and (self.lives != -1):
            with (open("data.json","r")) as f:
                dct = json.load(f)
            dct["lives"] = self.lives
            with open("data.json","w") as f:
                json.dump(dct,f)
            self.switchscene(2)
        elif self.frame == 60:
            self.lives -= 1
        elif self.frame == 1 and self.lives == 0:
            self.switchscene(0)