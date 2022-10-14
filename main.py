import pygame
import random
import lib.button as button
from lib.player import Player
from lib.enemy import Enemy
from lib.enemy import EnemyGroup
from lib.bullet import Bullet

#const var, hier zitten wij verder niet meer aan.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('assets/images/background1.png')
START_IMG = pygame.image.load('assets/images/background2.png')
BACKGROUND_COLOUR = (31, 29, 29) 
#https://helianthus-games.itch.io/pixel-art-space-shooter-kit
#https://deep-fold.itch.io/space-background-generator

# initialize pygame
pygame.init()
pygame.mixer.init(2)

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")
background_animation = 0

#game objects
player = Player() #hier roepen wij player aan.
player.rect.y = 300 #wordt op 300px gespawned
player_list = pygame.sprite.Group() #hier gaat de sprite voor player in
player_list.add(player) #en is nu toegevoegd.

# Enemy
enemyGroup = EnemyGroup(10)

# Temp text
font = pygame.font.SysFont("comicsans", 50)
textX = 10
textY = 10

# Load button text
title_text = font.render("Space Warriors", True, (125, 38, 205))
start_text = font.render("Start", True, (0, 255, 0))
exit_text = font.render("Exit", True, (255, 0, 0))
game_over_text = font.render("Game over", True, (200, 200, 200))

# Lives
lives_text = font.render("Lives = " + str(player.lives), True, (255, 255, 0))

# Creat title and icon
title = button.Button(220, 100, title_text, 1.0)
icon = pygame.image.load("assets/images/ship.png")
pygame.display.set_icon(icon)

#music
pygame.mixer.music.load("assets/music/bg_music.mp3") #dit wordt niet de final bgm, dit is een placeholder

# Create buttons
start_button = button.Button(200, 250, start_text, 1.0)
exit_button = button.Button(500, 250, exit_text, 1.0)

score_value = 0

# bullet object
bullet = Bullet(0, 0)

def show_score(x, y):
    score = font.render("Score = " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))

def write_score(): #zou dit bij assets kunnen????? who knows!!!
    with open("score.txt", "a") as write_hs: #maakt file aan in map waar game zit, "a" geeft aan dat het een file moet creëren en daarna mag aanpassen
        write_hs.write(f"{str(score_value)}\n") #schrijft naar bestand die hierboven is aangemaakt
        #with sluit de file automatisch, als ik mij niet vergis, dus close() is niet meer nodig

def show_lives(x, y):
    lives = font.render("Lives = " + str(player.lives), True, (255, 255, 0))
    screen.blit(lives, (x, y))
    
def game_over():
    screen.blit(game_over_text, (300, 250))
    highscore = font.render("Your final score = " + str(score_value), True, (255, 255, 0))
    screen.blit(highscore, (180, 300))
    pygame.mixer.music.stop()
    pygame.display.update()
    pygame.time.delay(2000)

# start loop
start = True

while start:
    
    # Background image
    screen.blit(START_IMG, (0, 0))

    #music
    pygame.mixer.music.play(-1) #-1 zorgt dat bgm blijft loopen (hier gezet omdat hij anders niet speelde)
    pygame.mixer.music.set_volume(0.0) #volume, waarde moet ergens tussen 0.1 en 1.0 zijn
    
    if title.draw(screen):
        start = True
    
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
    screen.blit(BACKGROUND_IMG,(background_animation, 0))#nieuwe achtergrond toegevoegd
    screen.blit(BACKGROUND_IMG,(SCREEN_WIDTH + background_animation, 0))
    if (background_animation ==- SCREEN_WIDTH):
        screen.blit(BACKGROUND_IMG,(SCREEN_WIDTH + background_animation, 0))
        background_animation = 0
    background_animation -= 1
    
    #music
    pygame.mixer.music.set_volume(0.2) 
    
    # laat enemies zien
    enemyGroup.update(screen)
    
    #bullet
    if bullet.bullet_state == "fire":
        bullet.update(screen)

    if bullet.rect.x > 800:
        bullet.bullet_state = "ready"
        bullet.rect.x = 0
    
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
                bullet.update(screen)
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                print("space")
                
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
    
    # bullet collision
    hitsBullet = pygame.sprite.spritecollide(bullet, enemyGroup, True)
    if hitsBullet:
        bullet.bullet_state = "ready"
        score_value += 1
        bullet.rect.y = 0
        bullet.rect.x = 0
        enemy = Enemy(random.randint(350, 750), random.randint(0, 350), 5.5)
        enemyGroup.add(enemy)
                
    # player collision 
    hits = pygame.sprite.spritecollide(player, enemyGroup, False)
    if hits:
        player.lives -= 1
        player.rect.x = 0
        player.rect.y = 300
        if player.lives == 0:
            enemyGroup.empty()
            player_list.empty()
            game_over()
            write_score()
            running = False
        

    player_list.draw(screen) #alleen is ie niet op t scherm, maar hij pakt de veranderde kleurwaardes van background ook niet. wat.
    player_list.update() #was dit vergeten toe te voegen, nu kunnen we de player zien bewegen op het scherm    
    show_score(textX, textY) # laat de score zien
    show_lives(textX, textY + 50) # laat de lives zien
    pygame.display.update() #update het scherm
            
pygame.quit()