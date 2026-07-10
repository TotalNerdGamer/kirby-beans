import pygame
import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes.Player import Player
from classes.Platform import Platform
from classes.mypos import myPos
from classes.myimg import myimg
from classes.cheese import Cheese
from classes.hudheart import HUDHeart
from classes.mousetrap import Mousetrap
from classes.Scene import Scene
from classes.Dialogue import Dialogue
class LevelScene(Scene):
    "Why don't we level the playing field?"
    def __init__(self,switchscene,platforms,colls,hazards,npcs,x,y,lvlright=1280):
        super().__init__(switchscene)
        self.platforms = platforms
        self.colls = colls
        self.hazards = hazards
        self.lvlright = lvlright
        self.player = Player(x,y)
        self.basepos1=myPos(0,0)
        self.basepos2 = myPos(self.lvlright,0)
        self.scrollpoint = 3
        self.hearts=[HUDHeart(5,5,1),HUDHeart(70,5,2),HUDHeart(135,5,3)]
        self.dlg = []
        self.npcs = npcs
        self.bg = "cabinets"
        self.bg1 = myimg(0,0,f"backgrounds/{self.bg}.png")
        self.bg2 = myimg(1280,0,f"backgrounds/{self.bg}.png")
        all = []
        all.extend(npcs)
        all.extend([self.player,self.basepos1,self.basepos2])
        all.extend(platforms)
        all.extend(colls)
        all.extend(hazards)
        
        self.ALL_SCROLL1_THINGS = all
        all = [self.bg1,self.bg2]
        self.ALL_SCROLL2_THINGS= all
        all = []
        all.extend(self.ALL_SCROLL2_THINGS)
        all.extend(self.ALL_SCROLL1_THINGS)
        all.extend(self.hearts)
        all.extend(self.dlg)
        self.ALL_THINGS = all
        #print("A")
    def update(self,dt):
        #print("D")
        self.player.update(dt,self.platforms,self.colls)
        if self.player.pos.y - 50 > 720 or self.player.health <= 0:
            #print("B")
            self.switchscene(1)
            
        #print("C")
        if ((self.player.pos.x <= 1280/self.scrollpoint and self.player.vel.x < 0) or (self.player.pos.x >= 1280*(self.scrollpoint-1)/self.scrollpoint and self.player.vel.x > 0)) and 1280 < self.basepos2.pos.x - self.player.vel.x*300*dt and self.basepos1.pos.x - self.player.vel.x*300*dt < 0:
            for i in self.ALL_SCROLL1_THINGS:
                i.pos.x -= self.player.vel.x*300*dt
            for i in self.ALL_SCROLL2_THINGS:
                i.pos.x -= self.player.vel.x*200*dt
                #print(i.pos.x)
            self.player.xcoll(self.platforms)
        self.bg1.update()
        self.bg2.update()
        for i in self.colls:
            i.update(self.player)
        for i in self.hazards:
            i.update(self.player)
        for i in self.hearts:
            i.update(self.player)
        for i in self.dlg:
            i.update(dt)
        for i in self.npcs:
            i.update(self.player,self.adddlg)
        
    def draw(self,screen):
        screen.fill("white")
        for i in self.ALL_THINGS:
            i.draw(screen)
            try:
                if i.kill:
                    self.ALL_THINGS.remove(i)
                    if type(i) == Dialogue:
                        self.dlg.remove(i)
            except:
                pass
    def adddlg(self, dlg: Dialogue):
        dlg.kill = False
        self.dlg.append(dlg)
        self.ALL_THINGS.append(dlg)
        