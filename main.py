from turtle import width
import pygame
from pygame import mixer
import random
import math

# initialize pygame
pygame.init()


# set up the drawing window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
background_color = (0, 0, 0)






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

    # Background color
    screen.fill(background_color)


    #hierboven moet de while loop komen
    enemy(enemyX, enemyY)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()