from main.main import MainScene
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.Clock()
scenes = [MainScene(screen,clock)]
sceneindex = 0
scene = scenes[sceneindex]
running = True
def switchscene(i):
    global clock
    global screen
    global scene
    "hi"
    sceneindex = i
    scene = scenes[sceneindex]
    scene.__init__()

    
