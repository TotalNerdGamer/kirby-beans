import pygame
from classes.Player import Player

class Mousetrap:
    """The player turns the crank A which rotates the gears B causing the lever C to move and push the stop sign against the shoe D. The shoe tips the bucket holding the metal marble E.
    The marble rolls down the rickety stairs F and into the rain gutter G, which leads it to the helping hand rod H. This causes the other metal marble I to fall from the top of the
    helping hand rod through the thing-a-ma-jig J and bathtub K, landing on the diving board L.
    The weight of the metal marble catapults the diver M through the air and into the washtub N, causing the cage O to fall from the top of the post P and trap the unsuspecting mouse."""
    def __init__(self, x,y):
        self.activated = False
        self.pos = pygame.Vector2(x-80,y-60)
    def draw(self,screen):
        if self.activated:
            self.img = "hazards/mousetrap/open"
        else:
            self.img = "hazards/mousetrap/close"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)
    def update(self,player: Player):
        if not self.activated:
            if self.pos.y<player.pos.y+50 < self.pos.y+120 - 98:
                self.activated = True
                player.dmg()
    