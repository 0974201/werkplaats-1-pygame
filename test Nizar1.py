import pygame
from pygame.locals import *
import math
import random
import button
from player import Player
from enemy import Enemy
from enemy import EnemyGroup

# const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load("assets/images/background.png")
# PLAYER_COLOUR = (148, 24, 24)
BACKGROUND_COLOUR = (31, 29, 29)
# https://helianthus-games.itch.io/pixel-art-space-shooter-kit
# https://deep-fold.itch.io/space-background-generator

# initialize pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

# game objects
player = Player()  # hier roepen wij player aan.
player.rect.y = 300  # wordt op 300px gespawned
player_list = pygame.sprite.Group()  # hier gaat de sprite voor player in
player_list.add(player)  # en is nu toegevoegd.

# Enemy (coordinaten nog aanpassen naar side shooter)
enemy = Enemy(0, 0, 0.5)
enemyGroup = EnemyGroup(10)

# Bullet spawn

BulletImage = pygame.image.load("assets/images/Bullet Nizar.png")
BulletX = 0
BulletY = player.rect.y
BulletX_Move = 10
BulletY_Move = 0
Bullet = "ready"

# Load button images
start_img = pygame.image.load("assets/images/start.png")
exit_img = pygame.image.load("assets/images/exit.png")

# Create buttons
start_button = button.Button(100, 200, start_img, 0.5)
exit_button = button.Button(450, 200, exit_img, 0.5)

# Temp text
font = pygame.font.SysFont("comicsans", 50)
textX = 250
textY = 250

score = 0


def Fire_Bullet(x, y):
    global Bullet
    Bullet = "fire"
    screen.blit(BulletImage, (x, y))


def show_text(x, y):
    text = font.render("Game running", True, (255, 255, 255))
    screen.blit(text, (x, y))


# start loop
start = True

while start:

    # Background color
    screen.fill(BACKGROUND_COLOUR)

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

# game loop
while running:

    # achtergrond afbeelding
    screen.blit(BACKGROUND_IMG, (0, 0))  # nieuwe achtergrond toegevoegd

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
                if Bullet == "ready":
                    BulletY = player.rect.y
                    Fire_Bullet(BulletX, player.rect.y)

        # player movement stoppen
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.moveY(0)
                print("key released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.moveX(0)
                print("key released")
    # Bullet beweegt mee met spaceship
    if BulletX >= 800:
        BulletX = 0
        Bullet = "ready"

    if Bullet == "fire":
        Fire_Bullet(BulletX, BulletY)
        BulletX += BulletX_Move
    # Collision
    Collision = pygame.sprite.spritecollide(Bullet, enemyGroup, False)
    if Collision:
        running = False
    # alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.
    player_list.update()  # was dit vergeten toe te voegen, nu kunnen we de player zien bewegen op het scherm
    pygame.display.update()
