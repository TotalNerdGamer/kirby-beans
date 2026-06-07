import sys
import os
sys.path.append(os.path.abspath("./src/classes"))
from Player import Player
from Platform import Platform
from mypos import myPos
import pygame
from myimg import myimg
from cheese import Cheese

pygame.init()
screen = pygame.display.set_mode((1280,720))
dt = 0
running = True
clock = pygame.Clock()
lvlright = 3840
player = Player(50,50,0,0)
platforms = [Platform(1280,700,2560,40,"green"),Platform(1320,460,400,40,"green"),Platform(3590,700,500,40)]
colls = [Cheese(1320,420)]
basepos1=myPos(0,0)
basepos2 = myPos(lvlright,0)
scrollpoint = 3
bg1 = myimg(0,0,"backgrounds/cabinets.png")
bg2 = myimg(1280,0,"backgrounds/cabinets.png")
all = [player,basepos1,basepos2]
all.extend(platforms)
all.extend(colls)
ALL_SCROLL1_THINGS = all
all = [bg1,bg2]
ALL_SCROLL2_THINGS= all
all = []
all.extend(ALL_SCROLL2_THINGS)
all.extend(ALL_SCROLL1_THINGS)
ALL_THINGS = all


while running:
    screen.fill("white")
    player.update(dt,platforms,colls)
    if player.pos.y - 50 > 720 or player.health < 0:
        running=False
        endreason = "died"
    if ((player.pos.x <= 1280/scrollpoint and player.vel.x < 0) or (player.pos.x >= 1280*(scrollpoint-1)/scrollpoint and player.vel.x > 0)) and 1280 < basepos2.pos.x - player.vel.x*300*dt and basepos1.pos.x - player.vel.x*300*dt < 0:
        for i in ALL_SCROLL1_THINGS:
            i.pos.x -= player.vel.x*300*dt
        for i in ALL_SCROLL2_THINGS:
            i.pos.x -= player.vel.x*200*dt
            #print(i.pos.x)
        player.xcoll(platforms)
    bg1.update(screen)
    bg2.update(screen)
    for i in colls:
        i.update(player)
    for i in ALL_THINGS:
        i.draw(screen)
        try:
            if i.kill:
                ALL_THINGS.remove(i)
        except:
            pass
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()