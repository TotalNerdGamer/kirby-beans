import pygame
from functools import partial

class Button:
    def __init__(self,x,y,w,h,col,text,func: function,textcol="white"):
        self.pos=pygame.Vector2(x,y)
        self.size=pygame.Vector2(w,h)
        self.col=col
        self.text=text
        self.textcol=textcol
        self.func=func
    def draw(self,screen):
        pygame.draw.rect(screen,self.col,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y))
        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render(self.text, True, self.textcol)
            textpos = text.get_rect(centerx=self.pos.x, centery=self.pos.y)
            screen.blit(text, textpos)
    def update(self):
        pygame.event.get()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.pos.x-self.size.x/2<pos[0]<self.pos.x+self.size.x/2 and self.pos.y-self.size.y/2<pos[1]<self.pos.y+self.size.y/2:
                func = self.func
                func()
                #print("hi")