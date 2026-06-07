import pygame
from Player import Player

class HUDHeart:
    "A heart in the HUD to represent the player's health."
    def __init__(self, x,y,id):
        self.full=True
        self.pos=pygame.Vector2(x,y)
        self.id = id
         
    def update(self,player: Player):
        self.full = (self.id <= player.health)