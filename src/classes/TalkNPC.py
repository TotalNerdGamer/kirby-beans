import pygame
import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes.Dialogue import Dialogue
from classes.Player import *

class TalkNPC:
    "Hello! As the shrimp NPC, I..."
    def __init__(self, dlg: Dialogue,x,y,width,height,sprites="default",emotion="neutral"):
        self.SPRITES_PATH = f"./assets/npcs/{sprites}"
        self.emotion = emotion
        self.talking = False
        self.cantalk = False
        self.dlg = dlg
        self.pos = pygame.Vector2(x,y)
        self.size = pygame.Vector2(width,height)
    def get_rect(self):
        return pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y)
    def update(self,player: Player, adddlg: function):
        keys = pygame.key.get_pressed()
        if player.get_rect().colliderect(self.get_rect()) and (keys[pygame.K_z] or keys[pygame.K_RETURN]) and player.con:
            adddlg(self.dlg)
            self.cantalk = True
            player.con = False
        if self.cantalk:
            self.talking = self.dlg.writing and self.dlg.speaker == ""
        if self.dlg.kill:
            player.con = True
        if self.dlg.specchar != "":
            spec = self.dlg.specchar
            #print(spec)
            if spec == "|":
                self.emotion = "neutral"
            elif spec == "(":
                self.emotion = "frown"
            elif spec == ")":
                self.emotion = "smile"
    def draw(self,screen: pygame.Surface):
        if self.talking:
            if self.emotion == "neutral":
                self.sprpath = f"{self.SPRITES_PATH}/talk/talk.png"
            else:
                self.sprpath = f"{self.SPRITES_PATH}/talk/talk-{self.emotion}.png"
        else:
            if self.emotion == "neutral":
                self.sprpath = f"{self.SPRITES_PATH}/base.png"
            else:
                self.sprpath = f"{self.SPRITES_PATH}/base-{self.emotion}.png"
        self.imgsurf = pygame.image.load(f"{self.sprpath}").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)