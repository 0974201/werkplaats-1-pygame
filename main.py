import pygame
#from pygame import mixer
#from turtle import width
#import random
#import math


class Player(pygame.sprite.Sprite):
    #uh ok, dus dit is constructor van de player.
    #zeg maar de blauwprint van de player als ie (in de game) wordt aangeroepen.
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    print("test") #check of hij aangeroepen wordt.

# initialize pygame
pygame.init()

# set up the drawing window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
player_colour = (148, 24, 24)
background_color = (217, 176, 176) #als je dit ziet, zit je niet in de goede branch yo

##################

player = Player(player_colour, 50, 50) #hier roepen wij player aan. hopelijk pakt ie hex colour
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.


running = True

while running:
    
    # Background color
    screen.fill(background_color)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player_list.draw(screen) #alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.