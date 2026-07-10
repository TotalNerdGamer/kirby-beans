import pygame

class Dialogue:
    "Blah blah blah blah blah."
    def decodeText(text: str,player):
        "scrapped func inspired by zelda OoT, used to turn placeholders into the correct values"
        return text.replace("%CHEESE%",player.cheese)
    def __init__(self, text: str, /, *, writedelay=2, portrait=False):
        self.text = text
        self.text = self.text.split("\r")
        self.showntext = ""
        self.frame = 0
        self.writedelay = writedelay
        self.boxindex = 0
        self.showindex = 0
        self.writing = True
        self.kill = False
        self.speaker = ""
        self.specchar = ""
    def draw(self,screen: pygame.Surface):
        s = pygame.Surface((1260,200))
        s.set_alpha(200)
        s.fill((200,200,200))
        screen.blit(s,(10,20))
        font = pygame.Font(None, 40)
        txt = font.render(self.showntext,True,(255,255,255))
        textpos = txt.get_rect(left=50, top=50)
        screen.blit(txt,textpos)
        
        #pygame.draw.rect(screen,pygame.Color(120,120,120,120),pygame.Rect(0,0,1280,100))
    def update(self,dt):
        self.frame = (self.frame+1)%self.writedelay
        self.speaker = (self.text[self.boxindex].split("\0s")[0] if len(self.text[self.boxindex].split("\0s")) > 1 else "")
        if self.showindex < len(self.text[self.boxindex]) and self.frame == self.writedelay - 1:
            if self.text[self.boxindex][self.showindex] != "\0":
                self.writing = True
                self.showntext += self.text[self.boxindex][self.showindex]
                self.showindex += 1
                self.specchar = ""
            else:
                self.writing = False
                if self.showindex < len(self.text[self.boxindex])-1:
                    self.specchar = self.text[self.boxindex][self.showindex+1]
                self.showindex += 2
        elif self.showindex >= len(self.text[self.boxindex]):
            self.writing = False
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_z] or keys[pygame.K_RETURN]) and not self.writing:
            if not self.boxindex == len(self.text)-1:
                self.boxindex += 1
                self.writing = True
                self.showntext = ""
                self.showindex = 0
            else:
                self.kill = True
                self.boxindex = 0
                self.showntext = ""
                self.showindex = 0
