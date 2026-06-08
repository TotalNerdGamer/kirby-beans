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
        super().__init__(screen,clock)
        self.start = Button(640,540,200,50,"blue","START",partial(switchScene,),float=True)
        
        self.dt = 0
        self.running = True
        
            
    def draw(self,screen):
        screen.fill("white")
        self.start.draw(screen)
    def update(self)