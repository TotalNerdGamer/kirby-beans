import pygame

class Platform:
    "The titular element of the genre."
    def __init__(self, x,y,width,height,col="green",type="grass"):
        self.pos = pygame.Vector2(x,y)
        self.size = pygame.Vector2(width,height)
        self.col = col
        self.type = type
    def draw(self,Surface):
        pygame.draw.rect(Surface,self.col,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y))
    def get_rect(self):
        return pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y)
