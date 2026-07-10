import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes.Player import Player
from classes.Platform import Platform
from classes.mypos import myPos
import pygame
from classes.myimg import myimg
from classes.cheese import Cheese 
from classes.hudheart import HUDHeart
from classes.mousetrap import Mousetrap
from classes.LevelScene import LevelScene
from classes.TalkNPC import TalkNPC
from classes.Dialogue import Dialogue
class DebugScene(LevelScene):
    def __init__(self,switchscene):
        platforms = [Platform(1280,700,2560,40,"green"),Platform(1320,460,400,40,"green"),Platform(3590,700,500,40),Platform(1320,680-11,160,22),Platform(1160,680-11,160,22),Platform(1480,680-11,160,22)]
        colls = [Cheese(1320,400)]
        hazards = [Mousetrap(1320,620),Mousetrap(1160,620),Mousetrap(1480,620)]
        npcs = []
        testnpc = TalkNPC(Dialogue("Hey there! I'm Mr. Tomato.\rWelcome to the code playground.\rThis is where objects are tested!\rHow do you feel knowing our entire lives aren't real?\rArchie\0s: Uhh... bad, I guess?\0|\rOh. Well, that's pessimistic if you ask me."),1280,300,40,40,"tomato","smile")
        npcs.append(testnpc)
        super().__init__(switchscene,platforms,colls,hazards,npcs,50,600,3840)
        self.bg = "cabinets"
        
