from classes.Platform import Platform

class TLPlatform(Platform):
    "A shift in genre."
    def __init__(x,y,w,h,col="green",type="grass"):
        super().__init__(x+w/2,y+h/2,w,h,col,type)