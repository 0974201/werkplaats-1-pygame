import pygame
from pygame.locals import *
from player import Player

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('assets/images/background.png')
#PLAYER_COLOUR = (148, 24, 24)
#BACKGROUND_COLOUR = (31, 29, 29) 
#https://helianthus-games.itch.io/pixel-art-space-shooter-kit
#https://deep-fold.itch.io/space-background-generator

# initialize pygame
pygame.init()


# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

#gaem objects
player = Player() #hier roepen wij player aan.
player.rect.y = 300 #wordt op 300px gespawned
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.






# Bunyamin/ eerste enemys:

# Enemy (coordinaten kloppen nog niet)
enemyImg = pygame.image.load('alienvijand.png)')
enemyX = 370
enemyY = 50
enemyX_change = 0 

def enemy(x, y):
    screen.blit(enemyImg, (x, y()))





running = True

while running:
    
    screen.blit(BACKGROUND_IMG, (0,0)) #nieuwe achtergrond toegevoegd
    
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.moveY(-1)
                print("up")
            if event.key == pygame.K_DOWN:
                player.moveY(1)
                print("down")
            if event.key == pygame.K_LEFT:
                player.moveX(-1)
                print("left")
            if event.key == pygame.K_RIGHT:
                player.moveX(1)
                print("right")
            if event.key == pygame.K_SPACE:
                print("pew")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                player.moveY(0)
                print("key released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.moveX(0)
                print("key released")
            if event.key == pygame.K_SPACE:
                print("spacebar released")
