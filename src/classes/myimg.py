import pygame

class myimg:
    def __init__(self,x,y,img):
        self.pos = pygame.Vector2(x,y)
        self.img = img
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert()
    def draw(self,Surface):
        pygame.Surface.blit(Surface,self.imgsurf,self.pos)
    def update(self, screen):
        if self.pos.x + 1280 < -1:
            self.pos.x = 2560 + self.pos.x
        elif self.pos.x > 1281:
            self.pos.x = self.pos.x - 2560
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
    def get_rect(self):
        return self.imgsurf.get_rect()