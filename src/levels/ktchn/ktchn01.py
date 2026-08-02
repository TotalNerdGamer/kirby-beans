import sys
import os
sys.path.append(os.path.abspath("./src"))
from classes import *
class Kitchen01(LevelScene):
    def __init__(self,switchscene):
        platforms = [Platform(1280,700,2560,40,"green"),Platform(1320,460,400,40,"green"),Platform(3590,700,500,40),Platform(1320,680-11,160,22),Platform(1160,680-11,160,22),Platform(1480,680-11,160,22)]
        colls = [Cheese(1320,400)]
        hazards = [Mousetrap(1320,620),Mousetrap(1160,620),Mousetrap(1480,620)]
        npcs = []
        super().__init__(switchscene,platforms,colls,hazards,npcs,50,600,3840)
        self.bg = "cabinets"
