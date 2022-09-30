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

# Enemy (coordinaten nog aanpassen naar side shooter)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 10

for i in range(num_of_enemy):
enemyImg.append(pygame.image.load('images/alienvijand.png)'))
enemyX.append(random.randint(0, 800))
enemyY.append(random.randint(50, 150))
enemyX_change.append(4)
enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# game loop
running = True
while running:

    # Background color
    screen.fill(background_color)

    # hierboven moet de while loop komen
    enemy(enemyX, enemyY)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Enemy movement/bewegingen (coordinaten nog aanpassen) de colission
    moet hieronder komen!!!
    for i in range(num_of_enemy):
    enemyX += enemyX_change
    if enemyX[i] <= 0:
        enemyX_change[i] = 4
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 735:
        enemyX_change[i] = -4
        enemyY[i] += enemyY_change[i]


enemy(enemyX[i], enemyY[i])
pygame.display.update()
