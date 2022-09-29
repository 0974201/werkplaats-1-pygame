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
enemyImg = pygame.image.load('images/alienvijand.png)')
enemyX = random.randint (0, 800)
enemyY = random.randint (50, 150)
enemyX_change = 0.3 
enemyY_change = 0.3

def enemy(x, y):
    screen.blit(enemyImg, (x, y()))




#game loop
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

    


   # Enemy movement/bewegingen (coordinaten nog aanpassen)
    enemyX += enemyX_change

    if enemyX <=0:
        enemyX_change = 0.6
        enemyY += enemyY_change
    elif enemyX >=735:
        enemyX_change = -0.6 



pygame.display.update()