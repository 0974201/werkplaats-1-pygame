import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    #uh ok, dus dit is constructor van de player.
    #zeg maar de blauwprint van de player als ie (in de game) wordt aangeroepen.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.image.load('assets/images/ship.png') #hier gaat img voor player object in
        #self.image.fill(colour) #hier krijgt t een kleurtje, kan ook achterwege gelaten worden als er een img file gebruikt wordt.
        self.rect = self.image.get_rect() #haalt op wat er in bovenstaande regels is aangemaakt
        
        self.changeX = 0
        self.changeY = 0

    def moveX(self, x):
        self.changeX = x #update movement on x-axis

    def moveY(self, y):
        self.changeY = y #update movement on y-axis

    def update(self):
        self.rect.x += self.changeX #update positie op het scherm
        self.rect.y += self.changeY
        
        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        if self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height #dit zorgt ervoor dat hij in het scherm blijft
