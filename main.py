from turtle import width
import pygame
from pygame import mixer
import random
import math
import button

# initialize pygame
pygame.init()

# set up the drawing window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
background_color = (0, 0, 0)

# Load button images
start_img = pygame.image.load("assets/images/start.png")
exit_img = pygame.image.load("assets/images/exit.png")

#Title
pygame.display.set_caption("Space Warriors")

# Create buttons
start_button = button.Button(100, 200, start_img, 0.5)
exit_button = button.Button(450, 200, exit_img, 0.5)

# Temp text
font = pygame.font.SysFont("comicsans", 50)
textX = 250
textY = 250

def show_text(x, y):
    text = font.render("Game running", True, (255, 255, 255))
    screen.blit(text, (x, y))

start = True

while start:
    
    # Background color
    screen.fill(background_color)
    
    if start_button.draw(screen):
        running = True
        start = False
    if exit_button.draw(screen):
        start = False
        
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            
    pygame.display.update()
    

while running:

    # Background color
    screen.fill((255, 150, 50))
    
    show_text(textX, textY)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
            
pygame.quit()