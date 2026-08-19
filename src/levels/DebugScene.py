import sys
import os

sys.path.append(os.path.abspath("./src"))
from classes import *
from myhelp import *
class DebugScene(LevelScene):
    "EXTERMINATE"
    def __init__(self,switchscene):
        platforms = [
            TLPlatform(0,680,3840,40,"red"),
            ]
        colls = [
            Cheese(1320,400),
            ]
        hazards = [
            ]
        npcs = []
        mtk = TalkNPC(
            Dialogue(
                    conv([
                        "KIRBY DEJA DE COMER FRIJOLES HORNEADOS!",
                        "ME ESTOY PONIENDO FURIOSO!",
                        ])
                        ),
                1280,
                360,
                128,
                128,
                "metaknight",
                emotion="frown"
                )
        chefk = TalkNPC(
            Dialogue(
                conv(
                    [
                        "Hi Kirby. \rIt's me, Chef Kawasaki. Here, in this theater. \rI made ten cans of baked beans. \rSee if you can get them all!"
                    ]
                    )
                )
        )
        npcs.append(mtk)
        super().__init__(
            switchscene,
            platforms,
            colls,
            hazards,
            npcs,
            50,
            600,
            3840)
        self.bg = "cabinets"