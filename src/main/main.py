from __future__ import annotations
import pygame
import sys
import os



sys.path.append(os.path.abspath("./src"))
from classes.button import Button
from tkinter.messagebox import showerror
from functools import partial
from sys import exit
import subprocess
from time import sleep
from helpfulstuff.help import *
import threading
from classes.Scene import Scene
class MainScene(Scene):
    def __init__(self,screen,clock):
        super().__init__
        
        start = Button(640,540,200,50,"blue","START",partial(switchScene,),float=True)
        screen = pygame.display.set_mode((1280,720))
        dt = 0
        clock = pygame.Clock()
        running = True
        while running:
            screen.fill("white")
            start.draw(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            start.update()