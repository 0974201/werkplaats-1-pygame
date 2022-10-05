from turtle import width
import pygame
from pygame import mixer
from enemy import Enemy
from enemy import EnemyGroup
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

# Enemy (coordinaten nog aanpassen naar side shooter)
    
enemy = Enemy(0, 0, 0.5)
enemyGroup = EnemyGroup(10)


# game loop
running = True
while running:

    # Background color
    screen.fill(background_color)

    # hierboven moet de while loop komen
    # enemy(enemyX[i], enemyY[i], i)
    enemyGroup.update(screen)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Enemy movement/bewegingen (coordinaten nog aanpassen) de colission
    #moet hieronder komen!

    pygame.display.update()
