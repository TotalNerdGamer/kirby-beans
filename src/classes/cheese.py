import pygame
from myimg import myimg
from Player import Player

class Cheese(myimg):
    def __init__(self,x,y):
        super().__init__(x,y,"collectibles/cheese/cheese.png")
        self.frame=0
        self.playing=False
    def update(self,player: Player):
        if self.playing:
            if self.frame == 0:
                self.frame = 1
            elif self.frame == 1:
                self.kill = True
                player.cheese += 1
        self.img=f"collectibles/cheese/{["cheese","cheese_collect"][self.frame]}.png"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert()