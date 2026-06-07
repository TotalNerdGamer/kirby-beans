import pygame
from classes.Player import Player

class HUDHeart:
    "A heart in the HUD to represent the player's health."
    def __init__(self, x,y,id):
        self.full=True
        self.pos=pygame.Vector2(x,y)
        self.id = id
         
    def update(self,player: Player):
        self.full = (self.id <= player.health)
    def draw(self,screen):
        if self.full:
            self.img = "hud/heart_full.png"
        else:
            self.img = "hud/heart_empty.png"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)
        