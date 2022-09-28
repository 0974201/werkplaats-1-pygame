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

running = True

while running:

    # Background color
    screen.fill(background_color)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False