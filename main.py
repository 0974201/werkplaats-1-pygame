import pygame
from pygame import *

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_COLOUR = (148, 24, 24)
BACKGROUND_COLOUR = (217, 176, 176) #note to self; verander dit weer terug naar zwart. problem is fixed.

class Player(pygame.sprite.Sprite):
    #uh ok, dus dit is constructor van de player.
    #zeg maar de blauwprint van de player als ie (in de game) wordt aangeroepen.
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height]) #dit maakt dus de image (in dit geval een blok) voor de player object aan
        self.image.fill(color) #hier krijgt t een kleurtje, kan ook achterwege gelaten worden als er een img file gebruikt wordt.

        self.rect = self.image.get_rect() #haalt op wat er in bovenstaande regels is aangemaakt

    def move(self, x, y):
        return "todo"

    def update(self):
        return "todo"

# initialize pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

#gaem objects
player = Player(PLAYER_COLOUR, 55, 55) #hier roepen wij player aan.
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
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("up released")
            if event.key == pygame.K_DOWN:
                print("down released")

    player_list.draw(screen) #alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.
    pygame.display.flip() #oh joh. okay. ik had dit dus nodig. dit updatetedtdtft het hele scherm met alles wat er tot nu toe is toegevoegd. (als ik het goed begrijp)