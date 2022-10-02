import pygame
from pygame import mixer
#from turtle import width
import random
import math

# initialize pygame
pygame.init()

# set up the drawing window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
background_color = (25, 25, 25) #als je dit ziet, zit je niet in de goede branch yo

class Player(pygame.sprite.Sprite):
    #uh ok, dus dit is constructor van de player.
    #zeg maar de blauwprint van de player als ie in de game wordt aangeroepen.
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups) #dank je vs code. ik had dit absoluut niet nodig.
    print("test")


##################

player = Player() #hier roepen wij player aan.
running = True

while running:

    # Background color
    screen.fill(background_color)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False