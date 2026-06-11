from __future__ import annotations
import pygame
import sys
import os



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
    "The title screen scene. I'm a poet and I didn't even know it!"
    def __init__(self,switchscene):
        super().__init__(switchscene)
        self.frame = 0
    def draw(self,screen: pygame.Surface):
        screen.fill("black")
    def update(self,dt):
        self.frame += 1