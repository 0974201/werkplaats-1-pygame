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

# Load button images
start_img = pygame.image.load("assets/images/start.png")
exit_img = pygame.image.load("assets/images/exit.png")

#Title
pygame.display.set_caption("Space Warriors")

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        # Mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Check if mouse is over the button
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Create buttons
start_button = Button(100, 200, start_img, 0.5)
exit_button = Button(450, 200, exit_img, 0.5)

start = True

while start:
    
    # Background color
    screen.fill(background_color)
    
    if start_button.draw():
        print("Start")
    if exit_button.draw():
        print("Exit")
        
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            
    pygame.display.update()
    

while running:

    # Background color
    screen.fill((255, 255, 255))

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()