import pygame

class Dialogue:
    "Blah blah blah blah blah."
    def decodeText(text: str,player):
        "scrapped func inspired by zelda OoT, used to turn placeholders into the correct values"
        return text.replace("%CHEESE%",player.cheese)
    def __init__(self, text, /, *, portrait=False):
        self.text = text
    def draw(self,screen: pygame.Surface):
        s = pygame.Surface((1260,200))
        s.set_alpha(200)
        s.fill((200,200,200))
        screen.blit(s,(10,20))
        #pygame.draw.rect(screen,pygame.Color(120,120,120,120),pygame.Rect(0,0,1280,100))
    def update(self,dt):
        pass