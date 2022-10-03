import pygame
from pygame.locals import *
from player import Player

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('assets/images/background.png')
#PLAYER_COLOUR = (148, 24, 24)
#BACKGROUND_COLOUR = (31, 29, 29) 
#https://helianthus-games.itch.io/pixel-art-space-shooter-kit
#https://deep-fold.itch.io/space-background-generator

# initialize pygame
pygame.init()


# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")

#gaem objects
player = Player() #hier roepen wij player aan.
player.rect.y = 300 #wordt op 300px gespawned
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.


# Bunyamin/ eerste enemys:

# Enemy (coordinaten nog aanpassen naar side shooter)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 10

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('assets/images/alienvijand.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(20)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# game loop
running = True
while running:
<<<<<<< HEAD
    
    screen.blit(BACKGROUND_IMG, (0,0)) #nieuwe achtergrond toegevoegd
    
=======

    # Background color
    screen.fill(background_color)

    # hierboven moet de while loop komen
    enemy(enemyX[i], enemyY[i], i)

>>>>>>> 166bb18 (10 enemies toegevoegd en enemy movements)
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
<<<<<<< HEAD
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                player.moveY(0)
                print("key released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.moveX(0)
                print("key released")
            if event.key == pygame.K_SPACE:
                print("spacebar released")
=======
    


   # Enemy movement/bewegingen (coordinaten nog aanpassen)
=======
    # Enemy movement/bewegingen (coordinaten nog aanpassen) de colission
    #moet hieronder komen!
    for i in range(num_of_enemy):
<<<<<<< HEAD
>>>>>>> 166bb18 (10 enemies toegevoegd en enemy movements)
    enemyX += enemyX_change
    if enemyX[i] <= 0:
        enemyX_change[i] = 4
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 735:
        enemyX_change[i] = -4
        enemyY[i] += enemyY_change[i]


<<<<<<< HEAD

pygame.display.update()
>>>>>>> 2de661b (enemy movement is toegevoegd)
=======
enemy(enemyX[i], enemyY[i])
pygame.display.update()
>>>>>>> 166bb18 (10 enemies toegevoegd en enemy movements)
=======
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 735:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]


        enemy(enemyX[i], enemyY[i], i)
    pygame.display.update()
>>>>>>> 80bc6a0 (debugs van enemies, is nu klaar)
