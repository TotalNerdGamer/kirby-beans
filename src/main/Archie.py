from main import MainScene
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.Clock()
def switchscene(i):
    global clock
    global screen
    global scene
    global scenes
    "hi"
    sceneindex = i
    scene = scenes[sceneindex]
    scene.__init__(switchscene)
scenes = [MainScene(switchscene)]
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
