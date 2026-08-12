from __future__ import annotations
import pygame
import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes import *
from functools import partial
class TitleScene(Scene):
    "The title screen scene. I'm a poet and I didn't even know it!"
    def __init__(self,switchscene):
        super().__init__(switchscene)
        self.frame = 0
        self.start = Button(
            640,
            540,
            200,
            50,
            "blue",
            "START",
            partial(switchscene,2),
            float=True)
    def draw(self,screen: pygame.Surface):
        screen.fill("white")
        if self.frame >= 300:
            self.start.draw(screen)
    def update(self,dt):
        self.frame += 1
        if self.frame >= 300:
            self.start.update()