import pygame
from pygame.locals import *
import math
import random
from player import Player
from enemy import Enemy
from enemy import EnemyGroup

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('assets/images/background.png')
#PLAYER_COLOUR = (148, 24, 24)
#BACKGROUND_COLOUR = (31, 29, 29) 
#https://helianthus-games.itch.io/pixel-art-space-shooter-kit
#https://deep-fold.itch.io/space-background-generator
from turtle import width
import pygame
from pygame import mixer
import random
import math

# initialize pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

#game objects
player = Player() #hier roepen wij player aan.
player.rect.y = 300 #wordt op 300px gespawned
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.

# Enemy (coordinaten nog aanpassen naar side shooter)
enemy = Enemy(0, 0, 0.5)
enemyGroup = EnemyGroup(10)


# game loop
running = True
while running:
    
    # achtergrond afbeelding
    screen.blit(BACKGROUND_IMG, (0,0)) #nieuwe achtergrond toegevoegd
    
    # laat enemies zien
    enemyGroup.update(screen)
    
    # player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.moveY(-1)
                print("up")
            if event.key == pygame.K_DOWN:
                player.moveY(1)
                print("down")
            if event.key == pygame.K_LEFT:
                player.moveX(-1)
                print("left")
            if event.key == pygame.K_RIGHT:
                player.moveX(1)
                print("right")
            if event.key == pygame.K_SPACE:
                print("pew")
                
        # player movement stoppen
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                player.moveY(0)
                print("key released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.moveX(0)
                print("key released")
            if event.key == pygame.K_SPACE:
                print("spacebar released")

    player_list.draw(screen) #alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.
    player_list.update() #was dit vergeten toe te voegen, nu kunnen we de player zien bewegen op het scherm
    pygame.display.update()
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