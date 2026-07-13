from __future__ import annotations
import pygame
from functools import partial
import math

class Button:
    "Cute as a button."
    def __init__(self,x,y,w,h,col,text,func: function, /, *, textcol="white",float=False,tsize=64):
        self.pos=pygame.Vector2(x,y)
        self.size=pygame.Vector2(w,h)
        self.col=col
        self.text=text
        self.textcol=textcol
        self.updown = float
        self.textsize = tsize
        self.func=func
        self.yoff=0
        self.yoffval=0
        self.growshrink = 1
        self.growshrinkgrowshrink = 1/100
        self.pressed = False
        self.pressframes = 0
    def draw(self,screen):
        pygame.draw.rect(screen,self.col,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2+self.yoff,self.size.x,self.size.y))
        if pygame.font:
            font = pygame.font.Font(None, self.textsize)
            text = font.render(self.text, True, self.textcol)
            textpos = text.get_rect(centerx=self.pos.x, centery=self.pos.y+self.yoff)
            screen.blit(text, textpos)
    def update(self):
        if self.updown and not self.pressed:
            self.yoffval += 1
            self.yoff=10*math.sin(self.yoffval/100)
        pygame.event.get()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.pos.x-self.size.x/2<pos[0]<self.pos.x+self.size.x/2 and self.pos.y+self.yoff-self.size.y/2<pos[1]<self.pos.y+self.yoff+self.size.y/2:
                self.pressed=True
        if self.pressed:
            if self.pressframes < 30:
                self.pressframes+=1
                self.size.x -= 2*self.growshrink
                self.size.y -= 1*self.growshrink
                self.textsize -= round(self.growshrink)
                self.growshrink += self.growshrinkgrowshrink
            elif self.pressframes == 30:
                self.pressframes += 1
                func = self.func
                func()
            elif self.pressframes < 60:
                self.pressframes += 1
                self.size.x += 2*self.growshrink
                self.size.y += 1*self.growshrink
                self.textsize += round(self.growshrink)
                self.growshrink-=self.growshrinkgrowshrink
            else:
                self.pressed = False
                self.pressframes = 0