import pygame
from pygame import *

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('assets/images/background.png')

# Caption and Icon
pygame.display.set_caption("Space Warriors")

# Player
playerImg = pygame.image.load('assets/images/ship.png')
playerX = 10
playerY = 300
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_SPACE:
                print("pew")


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 579:
        playerY = 579

    player(playerX, playerY)
    pygame.display.update()