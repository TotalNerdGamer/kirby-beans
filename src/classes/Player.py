import pygame

class Player:
    def __init__(self,x,y,velX,velY):
        self.pos = pygame.Vector2(x,y)
        self.vel = pygame.Vector2(velX,velY)
        self.speed = pygame.Vector2(0.1,7)
        self.jumping = True
        self.usedSave = False
        self.health = 3
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
    def update(self, dt, platforms):
        keys = pygame.key.get_pressed()
        termvel = 1
        termvely = 3
        dox = False
        if keys[pygame.K_a]:
            dox= True
            if self.vel.x > -1*termvel:
                self.vel.x -= self.speed.x
            else:
                self.vel.x = -1*termvel
        if keys[pygame.K_d]:
            dox = True
            if self.vel.x < termvel:
                self.vel.x += self.speed.x
            else:
                self.vel.x = termvel
        if not dox:
            self.vel.x = 0
        self.pos.x += self.vel.x*300*dt
        self.xcoll(platforms)
        if keys[pygame.K_w]:
            if not self.jumping:
                self.vel.y = self.speed.y
                self.jumping = True
        self.pos.y -= self.vel.y
        self.vel.y -= 0.1
        if self.vel.y <= -1*termvely:
            self.vel.y = -1*termvely
        self.jumping = True
        for platform in platforms:
            if self.get_rect().colliderect(platform.get_rect()):
                if self.pos.y < platform.pos.y:
                    self.pos.y = platform.pos.y - platform.size.y/2 - 50
                    self.jumping = False
                    self.usedSave = False
                    self.vel.y = 0
                elif self.pos.y > platform.pos.y:
                    self.pos.y = platform.pos.y + platform.size.y/2 + 50
                    self.vel.y = 0