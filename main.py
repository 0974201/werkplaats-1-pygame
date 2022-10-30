import pygame, random
from pygame import *
import lib.button as button
from lib.player import Player
from lib.enemy import Enemy
from lib.enemy import EnemyGroup
from lib.bullet import Bullet

# const variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load("assets/images/background1.png")
START_IMG = pygame.image.load("assets/images/background2.png")
TUTORIAL_IMG = pygame.image.load("assets/images/background.png")
BACKGROUND_COLOUR = (31, 29, 29)
# https://helianthus-games.itch.io/pixel-art-space-shooter-kit
# https://deep-fold.itch.io/space-background-generator

# initialize pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Warriors")
background_animation = 0

# game objects
player = Player()  # hier roepen wij player aan.
player.rect.y = 300  # wordt op 300px gespawned
player_list = pygame.sprite.Group()  # hier gaat de sprite voor player in
player_list.add(player)  # en is nu toegevoegd.

# bullet object
bullet = Bullet(0, 0)
bullet_group = pygame.sprite.Group()

# Enemy
enemy = Enemy(0, 0, 0)
enemyGroup = EnemyGroup(10)

# Temp text
font = pygame.font.SysFont("comicsans", 50)
textX = 10
textY = 10

# Load button text
title_text = font.render("Space Warriors", True, (125, 38, 205))
start_text = font.render("Start", True, (0, 255, 0))
choose_diff_text = font.render("Difficulity", True, (0, 255, 0))
exit_text = font.render("Exit", True, (255, 0, 0))
tutorial_text = font.render("Tutorial", True, (250, 250, 10))
game_over_text = font.render("Game over", True, (200, 200, 200))

# Lives
lives_text = font.render("Lives = " + str(player.lives), True, (255, 255, 0))

# Create title and icon
title = button.Button(220, 100, title_text, 1.0)
icon = pygame.image.load("assets/images/ship.png")
pygame.display.set_icon(icon)

# Sounds
mixer.music.load("assets/sounds/Floating In Nothingness.wav")
mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("assets/sounds/HIT.wav")
game_sound = pygame.mixer.Sound("assets/sounds/Shoot_1.wav")

# Create buttons
start_button = button.Button(200, 250, start_text, 1.0)
exit_button = button.Button(500, 250, exit_text, 1.0)
tutorial_button = button.Button(300, 350, tutorial_text, 1.0)


# Score
hs_list = []
score_value = 0

# Score function
def show_score(x, y):
    score = font.render("Score = " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))


# Write score to file
def write_score():
    with open("score.txt", "a") as write_hs:
        write_hs.write(f"{str(score_value)}\n")


# Get highscore from file
def get_hs():
    hs = ""
    with open("score.txt", "r") as score:
        score_list = score.readlines()

        for score in reversed(score_list):
            hs_list.append(int(score))

    hs = str(max(hs_list))
    return hs


# Show lives
def show_lives(x, y):
    lives = font.render("Lives = " + str(player.lives), True, (255, 255, 0))
    screen.blit(lives, (x, y))


# Game over function
def game_over():
    screen.blit(START_IMG, (0, 0))
    screen.blit(game_over_text, (280, 150))
    highscore = font.render(
        "Your final score = " + str(score_value), True, (255, 255, 0)
    )
    highest_hs = font.render("All time highscore = " + get_hs(), True, (255, 255, 0))
    write_score()
    screen.blit(highscore, (180, 250))
    screen.blit(highest_hs, (90, 300))
    pygame.display.update()
    pygame.time.delay(3150)


# Start loop
start = True

while start:

    # Background image
    screen.blit(START_IMG, (0, 0))

    # Tutorial loop
    if title.draw(screen):
        start = True
    if tutorial_button.draw(screen):
        while tutorial_button:
            if MOUSEBUTTONDOWN:
                screen.blit(TUTORIAL_IMG, (0, 0))
                tutorial_image = pygame.image.load("assets/images/key buttons.png")

                tutorial_image = pygame.transform.scale(tutorial_image, (200, 200))
                screen.blit(tutorial_image, (300, 300))
                back_text = font.render("Back", True, (250, 250, 10))
                back_button = button.Button(20, 500, back_text, 1.0)
                instruction_text = font.render(
                    "Het spel is een side shooter game, die je bestuurd",
                    True,
                    (0, 204, 0),
                )
                instruction_button = button.Button(0, 0, instruction_text, 0.4)

                instruction_text2 = font.render(
                    "met de arrow keys up en down om de schip op en neer te laten",
                    True,
                    (0, 204, 0),
                )
                instruction_button2 = button.Button(0, 50, instruction_text2, 0.4)

                instruction_text3 = font.render(
                    "bewegen en de space bar die je gebruikt om de bullet af te kunnen schieten.",
                    True,
                    (0, 204, 0),
                )
                instruction_button3 = button.Button(0, 100, instruction_text3, 0.4)
                if back_button.draw(screen):
                    start = True
                    break
                if instruction_button.draw(screen):
                    start = True
                if instruction_button2.draw(screen):
                    start = True
                if instruction_button3.draw(screen):
                    start = True
                # Quit game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tutorial_button = False

                pygame.display.update()

    # Start game button
    if start_button.draw(screen):
        running = True
        start = False

    # Exit game button
    if exit_button.draw(screen):
        start = False

    # Tutorial background
    for event in pygame.event.get():
        if event.type == tutorial_button:
            screen.blit(TUTORIAL_IMG, (0, 0))

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    pygame.display.update()


# Game loop
while running:

    # Background image animation
    screen.blit(BACKGROUND_IMG, (background_animation, 0))
    screen.blit(BACKGROUND_IMG, (SCREEN_WIDTH + background_animation, 0))
    if background_animation == -SCREEN_WIDTH:
        screen.blit(BACKGROUND_IMG, (SCREEN_WIDTH + background_animation, 0))
        background_animation = 0
    background_animation -= 1

    # Laat enemies zien
    enemyGroup.update(screen)

    # ready - je kan de bullet niet zien
    # fire - je ziet de bullet verschijnen

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

            if event.key == pygame.K_SPACE:
                game_sound.play()
                bullet_group.add(player.shoot())
                print("space")

        # player movement stoppen
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.moveY(0)
                print("key released")
            # bullet movement stoppen
            if event.key == pygame.K_SPACE:
                print("spacebar released")

    # bullet collision
    for bullet in bullet_group:
        for enemy in enemyGroup:
            if bullet.rect.colliderect(enemy.rect):
                hit_sound.play()
                enemyGroup.remove(enemy)
                bullet_group.remove(bullet)
                score_value += 1
                enemy = Enemy(random.randint(400, 570), random.randint(20, 150), 1.0)
                enemyGroup.add(enemy)

    # player collision
    hits = pygame.sprite.spritecollide(player, enemyGroup, False)
    if hits:
        print("ENEMY HITS PLAYER!")
        player.lives -= 1
        player.rect.x = 0
        player.rect.y = 300
        game_sound.play()
        if player.lives == 0:
            enemyGroup.empty()
            bullet_group.empty()
            player_list.empty()
            game_over()
            running = False

    player_list.draw(screen)
    bullet_group.draw(screen)
    bullet_group.update(screen)
    player_list.update()  # nu kunnen we de player zien bewegen op het scherm
    show_score(textX, textY)  # laat de score zien
    show_lives(textX, textY + 50)  # laat de lives zien
    pygame.display.update()  # update het scherm

pygame.quit()
