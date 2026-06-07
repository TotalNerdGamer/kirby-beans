import pygame
from classes.Player import Player

class Mousetrap:
    """The player turns the crank A which rotates the gears B causing the lever C to move and push the stop sign against the shoe D. The shoe tips the bucket holding the metal marble E.
    The marble rolls down the rickety stairs F and into the rain gutter G, which leads it to the helping hand rod H. This causes the other metal marble I to fall from the top of the
    helping hand rod through the thing-a-ma-jig J and bathtub K, landing on the diving board L.
    The weight of the metal marble catapults the diver M through the air and into the washtub N, causing the cage O to fall from the top of the post P and trap the unsuspecting mouse."""
    def __init__(self, x,y):
        self.activated = False
        self.frame = 0
        self.pos = pygame.Vector2(x-80,y-60)
    def draw(self,screen):
        self.img = ["open","mid1","mid2","mid3","mid4","close"][self.frame]
        self.imgsurf = pygame.image.load(f"assets/hazards/mousetrap/{self.img}.png").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)
    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,160,120)
    def update(self,player: Player):
        if not self.activated:
            if self.pos.y+96< player.pos.y+50 < self.pos.y+98 and player.get_rect().colliderect(self.get_rect()):
                self.activated = True
                player.dmg()
        else:
            if self.frame < 5:
                self.frame += 1
                

    