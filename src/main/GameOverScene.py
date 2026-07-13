from __future__ import annotations
import pygame
import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes.button import Button
from functools import partial
from classes.Scene import Scene
import json
class GameOverScene(Scene):
    "ba ba doo ba da da da da da dadada"
    def __init__(self,switchscene):
        super().__init__(switchscene)
        self.cont = Button(640,540,200,50,"white","RETURN",partial(self.contin),float=True, textcol="black")
    def draw(self,screen: pygame.Surface):
        screen.fill("black")
        self.cont.draw(screen)
    def update(self,dt):
        self.cont.update()
    def contin(self):
        with (open("data.json","r")) as f:
            dct = json.load(f)
        dct["lives"] = 5
        dct["continues"] += 1
        with open("data.json","w") as f:
            json.dump(dct,f)
        self.switchscene(0)