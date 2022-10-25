from email.headerregistry import Group
from tokenize import group
import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/images/Bullet Nizar.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5.0
        self.bullet_state = "ready"

    def move(self):
        self.bullet_state = "fire"
        self.rect.x += self.speed

    def update(self, screen):
        self.move()
        screen.blit(self.image, self.rect)


class BulletGroup(Group):
    def __init__(self):
        super().__init__()
        for i in range(num_of_enemy):
            enemy = Enemy(random.randint(400, 570),
                          random.randint(20, 150), 1.0)
            self.add(enemy)

    def move(self):
        for enemy in self.sprites():
            enemy.move()

    def update(self, screen):
        for enemy in self.sprites():
            enemy.update(screen)
