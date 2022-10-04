import pygame
from pygame import *

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_COLOUR = (148, 24, 24)
BACKGROUND_COLOUR = (31, 29, 29) 
#BACKGROUND_COLOUR = (0x1F1D1D)

#player class:
class Player(pygame.sprite.Sprite):
    #uh ok, dus dit is constructor van de player.
    #zeg maar de blauwprint van de player als ie (in de game) wordt aangeroepen.
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.Surface([width, height]) #dit maakt dus de image (in dit geval een blok) voor de player object aan
        self.image.fill(color) #hier krijgt t een kleurtje, kan ook achterwege gelaten worden als er een img file gebruikt wordt.
        self.rect = self.image.get_rect() #haalt op wat er in bovenstaande regels is aangemaakt
        
        self.changeX = 0
        self.changeY = 0

    def move(self, x, y):
        self.changeX += x
        self.changeY += y

    def update(self):
        self.rect.x += self.changeX #update positie op het scherm
        self.rect.y += self.changeY
        
        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        if self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height #dit zorgt ervoor dat hij in het scherm blijft

# initialize pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

#gaem objects
player = Player(PLAYER_COLOUR, 50, 50) #hier roepen wij player aan.
player.rect.y = 250 #wordt op 250px gespawned
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.

running = True

while running:
    
    # Background color
    screen.fill(BACKGROUND_COLOUR)
    
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -2)
                print("up")
            if event.key == pygame.K_DOWN:
                player.move(0, 2)
                print("down")
            if event.key == pygame.K_LEFT:
                player.move(-2, 0)
                print("left")
            if event.key == pygame.K_RIGHT:
                player.move(2, 0)
                print("right")
            if event.key == pygame.K_SPACE:
                print("pew")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.move(0, 0)
                print("up released")
            if event.key == pygame.K_DOWN:
                player.move(0, 0)
                print("down released")
            if event.key == pygame.K_LEFT:
                player.move(0, 0)
                print("left released")
            if event.key == pygame.K_RIGHT:
                player.move(0, 0)
                print("right released")
            if event.key == pygame.K_SPACE:
                print("spacebar released")

    player_list.draw(screen) #alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.
    player_list.update() #was dit vergeten toe te voegen, nu kunnen we de player zien bewegen op het scherm
    pygame.display.flip() #oh joh. okay. ik had dit dus nodig. dit updatetedtdtft het hele scherm met alles wat er tot nu toe is toegevoegd. (als ik het goed begrijp)