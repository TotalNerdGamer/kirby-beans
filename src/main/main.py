import pygame
import sys
import os
sys.path.append(os.path.abspath("./classes"))
from classes.button import Button
from tkinter.messagebox import showerror
from functools import partial
from sys import exit
import subprocess
from time import sleep
from helpfulstuff.help import *
import threading

modcheck = ["pygame.font"]
for module in modcheck:
    try:
        attempt = eval(module)
    except:
        showerror("Module Error",f"\"{module}\" did not install correctly!")
        exit()
    else:
        if not attempt:
            showerror("Module Error",f"\"{module}\" did not install correctly!")
            exit()
def startGame():
    global running
    thread = threading.Thread(target=partial(python, f"{os.path.abspath("./src/levels/ktchn/ktchn01.py")}"))
    thread.start()
    #print(os.path.abspath("../levels/ktchn01.py"))
    sleep(1)
    running=False
    pygame.quit()
pygame.init()
start = Button(640,360,200,50,"blue","START",startGame)
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