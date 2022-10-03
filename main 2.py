import pygame
from pygame import *

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('assets/images/ra_logo.png')

# Caption and Icon
pygame.display.set_caption("Space Warriors")

# Player
playerImg = pygame.image.load('assets/images/ra_logo.png')
playerX = 15
playerY = 250
playerX_change = 0

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
                playerX_change = -5
            if event.key == pygame.K_DOWN:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                #if bullet_state is "ready":
                    print("pew")
                    # Get the current x cordinate of the spaceship
                    #bulletX = playerX
                    #fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()