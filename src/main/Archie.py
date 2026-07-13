import sys
import os
sys.path.append(os.path.abspath("./src"))
from TitleScreen import TitleScene
from levels.ktchn.ktchn01 import Kitchen01
import pygame
from levels.DebugScene import DebugScene
from main.DeathScene import DeathScene
from main.GameOverScene import GameOverScene

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.Clock()
def switchscene(id):
    "Switches scenes. Who would have guessed?"
    global clock
    global screen
    global scene
    global scenes
    global sceneindex
    sceneindex = id
    scene = scenes[sceneindex]
    scene.__init__(switchscene)
scenes = [TitleScene(switchscene),DeathScene(switchscene),DebugScene(switchscene),Kitchen01(switchscene),GameOverScene(switchscene)]
sceneindex = 0
dt = 0
scene = scenes[sceneindex]
scene.__init__(switchscene)
running = True
while running:
    scene = scenes[sceneindex]
    scene.update(dt)
    scene.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False