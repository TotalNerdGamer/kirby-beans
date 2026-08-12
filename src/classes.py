from __future__ import annotations
import pygame
from functools import partial
import math
from pygame import Vector2
from sys import exit
from tkinter.messagebox import showerror
"Objects. If it's gonna be used often, it goes here."

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
class myimg:
    "My version of an image. Created so I could have an image with a pos for scrolling."
    def __init__(self,x,y,img):
        self.pos = pygame.Vector2(x,y)
        self.img = img
        
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert()
    def draw(self,Surface):
        pygame.Surface.blit(Surface,self.imgsurf,self.pos)
    def update(self):
        if self.pos.x + 1280 < -1:
            self.pos.x = 2560 + self.pos.x
        elif self.pos.x > 1281:
            self.pos.x = self.pos.x - 2560
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
    def get_rect(self):
        return self.imgsurf.get_rect()
class Cheese(myimg):
    "These descriptions seem a little cheesy if you ask me."
    def __init__(self,x,y):
        super().__init__(x,y,"collectibles/cheese/cheese.png")
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        self.pos=pygame.Vector2(x-self.imgsurf.get_width()/2,y-self.imgsurf.get_height()/2)
        self.yoffval = 0
        self.basey = self.pos.y
        self.yoff=math.sin(self.yoffval)
        self.frame=0
        self.playing=False
    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,self.imgsurf.get_width(),self.imgsurf.get_height())
    def update(self,player: Player):
        self.yoffval+=1
        self.yoff = 10*math.sin(self.yoffval/50)
        self.pos.y = self.basey + self.yoff
        if self.playing:
            if self.frame < 5:
                self.frame += 1
            elif self.frame == 5:
                self.kill = True
                player.cheese += 1
        self.img=f"collectibles/cheese/{["cheese","cheese_collect"][min(self.frame,1)]}.png"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()

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

class HUDHeart:
    "A heart in the HUD to represent the player's health."
    def __init__(self, x,y,id):
        self.full=True
        self.pos=pygame.Vector2(x,y)
        self.id = id
         
    def update(self,player: Player):
        self.full = (self.id <= player.health)
    def draw(self,screen):
        if self.full:
            self.img = "hud/heart_full.png"
        else:
            self.img = "hud/heart_empty.png"
        self.imgsurf = pygame.image.load(f"assets/{self.img}").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)
class Scene:
    "All the world's a stage."
    def __init__(self,switchscene):
        self.modcheck = ["pygame.font","pygame","pygame.Surface","pygame.display"]
        self.switchscene = switchscene
        for module in self.modcheck:
            try:
                self.attempt = eval(module)
            except:
                showerror("Module Error",f"\"{module}\" did not install correctly!")
                exit()
            else:
                if not self.attempt:
                    showerror("Module Error",f"\"{module}\" did not install correctly!")
                    exit()

class LevelScene(Scene):
    "Why don't we level the playing field?"
    def __init__(self,switchscene,platforms,colls,hazards,npcs,x,y,lvlright=1280):
        super().__init__(switchscene)
        self.platforms = platforms
        self.colls = colls
        self.hazards = hazards
        self.lvlright = lvlright
        self.player = Player(x,y)
        self.basepos1=myPos(0,0)
        self.basepos2 = myPos(self.lvlright,0)
        self.scrollpoint = 3
        self.hearts=[HUDHeart(5,5,1),HUDHeart(70,5,2),HUDHeart(135,5,3)]
        self.dlg = []
        self.npcs = npcs
        self.bg = "cabinets"
        self.bg1 = myimg(0,0,f"backgrounds/{self.bg}.png")
        self.bg2 = myimg(1280,0,f"backgrounds/{self.bg}.png")
        all = []
        all.extend(npcs)
        all.extend([self.player,self.basepos1,self.basepos2])
        all.extend(platforms)
        all.extend(colls)
        all.extend(hazards)
        
        self.ALL_SCROLL1_THINGS = all
        all = [self.bg1,self.bg2]
        self.ALL_SCROLL2_THINGS= all
        all = []
        all.extend(self.ALL_SCROLL2_THINGS)
        all.extend(self.ALL_SCROLL1_THINGS)
        all.extend(self.hearts)
        all.extend(self.dlg)
        self.ALL_THINGS = all
        #print("A")
    def update(self,dt):
        #print("D")
        self.player.update(dt,self.platforms,self.colls)
        if self.player.pos.y - 50 > 720 or self.player.health <= 0:
            #print("B")
            self.switchscene(1)
            
        #print("C")
        if ((self.player.pos.x <= 1280/self.scrollpoint and self.player.vel.x < 0) or (self.player.pos.x >= 1280*(self.scrollpoint-1)/self.scrollpoint and self.player.vel.x > 0)) and 1280 < self.basepos2.pos.x - self.player.vel.x*300*dt and self.basepos1.pos.x - self.player.vel.x*300*dt < 0:
            for i in self.ALL_SCROLL1_THINGS:
                i.pos.x -= self.player.vel.x*300*dt
            for i in self.ALL_SCROLL2_THINGS:
                i.pos.x -= self.player.vel.x*200*dt
                #print(i.pos.x)
            self.player.xcoll(self.platforms)
        self.bg1.update()
        self.bg2.update()
        for i in self.colls:
            i.update(self.player)
        for i in self.hazards:
            i.update(self.player)
        for i in self.hearts:
            i.update(self.player)
        for i in self.dlg:
            i.update(dt)
        for i in self.npcs:
            i.update(self.player,self.adddlg)
        
    def draw(self,screen):
        screen.fill("white")
        for i in self.ALL_THINGS:
            i.draw(screen)
            try:
                if i.kill:
                    self.ALL_THINGS.remove(i)
                    if type(i) == Dialogue:
                        self.dlg.remove(i)
            except:
                pass
    def adddlg(self, dlg: Dialogue):
        dlg.kill = False
        self.dlg.append(dlg)
        self.ALL_THINGS.append(dlg)

class Mousetrap:
    """The player turns the crank A which rotates the gears B causing the lever C to move and push the stop sign against the shoe D. The shoe tips the bucket holding the metal marble E.
    The marble rolls down the rickety stairs F and into the rain gutter G, which leads it to the helping hand rod H. This causes the other metal marble I to fall from the top of the
    helping hand rod through the thing-a-ma-jig J and bathtub K, landing on the diving board L.
    The weight of the metal marble catapults the diver M through the air and into the washtub N, causing the cage O to fall from the top of the post P and trap the unsuspecting mouse."""
    def __init__(self, x,y):
        self.activated = False
        self.damaged = False
        self.frame = 0
        self.pos = pygame.Vector2(x-80,y-60)
    def draw(self,screen):
        self.img = ["open","mid1","mid2","mid3","mid4","close"][self.frame]
        self.imgsurf = pygame.image.load(f"assets/hazards/mousetrap/{self.img}.png").convert_alpha()
        pygame.Surface.blit(screen,self.imgsurf,self.pos)
    def get_rect(self):
        return pygame.Rect(self.pos.x,self.pos.y,160,120)
    def update(self,player: Player):
        if not self.activated:
            if self.pos.y+96< player.pos.y+50 < self.pos.y+99 and player.get_rect().colliderect(self.get_rect()):
                self.activated = True
        else:
            if self.frame < 5:
                self.frame += 1
            elif not self.damaged:
                if self.get_rect().colliderect(player.get_rect()):
                    player.dmg()
                self.damaged = True
                




class myPos:
    "A tracker for a position. Used to measure scrolling."
    def __init__(self,x,y):
        self.pos=Vector2(x,y)
    def draw(self,unused):
        pass

class Platform:
    "The titular element of the genre."
    def __init__(self,x,y,width,height,col="green",type="grass"):
        self.pos = pygame.Vector2(x,y)
        self.size = pygame.Vector2(width,height)
        self.col = col
        self.type = type
    def draw(self,Surface):
        if not self.col == None:
            pygame.draw.rect(Surface,self.col,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y))
        pass
    def get_rect(self):
        return pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y)

class Player:
    "The player. Simple as that."
    def __init__(self,x,y,velX=0,velY=0,cheese=0):
        self.pos = pygame.Vector2(x,y)
        self.vel = pygame.Vector2(velX,velY)
        self.speed = pygame.Vector2(0.1,7)
        self.jumping = True
        self.usedSave = False
        self.health = 3
        self.iframes = 0
        self.con = True
        self.cheese = cheese
        self.airframes = 0
    def draw(self, Surface):
        pygame.draw.rect(Surface,"lightgray",pygame.Rect(self.pos.x-50,self.pos.y-50,100,100))
    def get_rect(self):
        return pygame.Rect(self.pos.x-50,self.pos.y-50,100,100)
    def xcoll(self, platforms):
        for platform in platforms:
            if self.get_rect().colliderect(platform.get_rect()):
                if self.pos.x < platform.pos.x:
                    self.pos.x = platform.pos.x - platform.size.x/2 - 50
                elif self.pos.x > platform.pos.x:
                    self.pos.x = platform.pos.x + platform.size.x/2 + 51
                self.vel.x = 0
    def update(self, dt, platforms,colls):
        keys = pygame.key.get_pressed()
        #print(self.jumping)
        #print(self.airframes)
        if self.airframes >= 5:
            termvel = 0.3
        else:
            termvel = 0.8
        termvely = 5
        dox = False
        if self.iframes > 0:
            self.iframes -= 1
        if self.con:
            if keys[pygame.K_a]:
                dox= True
                if self.vel.x > -1*termvel:
                    self.vel.x -= self.speed.x #- abs(self.vel.y)/10
                else:
                    self.vel.x = -1*termvel
            if keys[pygame.K_d]:
                #print("hi")
                dox = True
                if self.vel.x < termvel:
                    self.vel.x += self.speed.x #- abs(self.vel.y)/10
                else:
                    self.vel.x = termvel
            if not dox and not self.jumping:
                self.vel.x = 0
            """if self.jumping and not dox:
                if self.vel.x > 0:
                    self.vel.x -= 0.2
                elif self.vel.x < 0:
                    self.vel.x += 0.2"""
        else:
            self.vel.x = 0
        #print(f"1) {self.pos.x}")
        self.pos.x += self.vel.x*300*dt
        #print(f"2) {self.pos.x}")
        #print(self.vel.x)
        self.xcoll(platforms)
        if self.con:
            if keys[pygame.K_w]:
                if not self.jumping:
                    self.vel.y = self.speed.y
                    self.jumping = True
        self.pos.y -= self.vel.y
        self.vel.y -= 0.1 if self.vel.y > 0 else 0.2
        if self.vel.y <= -1*termvely:
            self.vel.y = -1*termvely
        self.jumping = True
        self.airframes += 1
        for platform in platforms:
            if self.get_rect().colliderect(platform.get_rect()):
                if self.pos.y < platform.pos.y:
                    self.pos.y = platform.pos.y - platform.size.y/2 - 50
                    self.jumping = False
                    self.airframes = 0
                    self.usedSave = False
                    self.vel.y = 0
                elif self.pos.y > platform.pos.y:
                    self.pos.y = platform.pos.y + platform.size.y/2 + 50
                    self.vel.y = 0
        for collectible in colls:
            if collectible.get_rect().colliderect(self.get_rect()):
                collectible.playing = True
    def dmg(self):
        if self.iframes > 0:
            return False
        else:
            self.health -= 1
            self.iframes = 60
            return True



class TalkNPC:
    "Hello! As the shrimp NPC, I..."
    def __init__(self, dlg: Dialogue,x,y,width,height,sprites="default", /, *, emotion="neutral"):
        self.SPRITES_PATH = f"./assets/npcs/{sprites}"
        self.emotion = emotion
        self.talking = False
        self.cantalk = False
        self.dlg = dlg
        self.encon = False
        self.pos = pygame.Vector2(x,y)
        self.size = pygame.Vector2(width,height)
    def get_rect(self):
        return pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y)
    def update(self,player: Player, adddlg: function):
        keys = pygame.key.get_just_pressed()
        if self.encon:
            self.encon = False
            player.con = True
        if player.get_rect().colliderect(self.get_rect()) and (keys[pygame.K_z] or keys[pygame.K_RETURN]) and player.con:
            adddlg(self.dlg)
            self.cantalk = True
            player.con = False
        if self.cantalk:
            self.talking = self.dlg.writing and self.dlg.speaker == ""
        if self.dlg.kill:
            self.encon = True
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
        pygame.Surface.blit(screen,self.imgsurf,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y))

class TLPlatform(Platform):
    "A shift in genre."
    def __init__(x,y,w,h,col="green",type="grass"):
        super().__init__(x+w/2,y+h/2,w,h,col,type)