import pygame
import random
from pygame.sprite import Sprite, Group, collide_rect


class Enemy(Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy_4.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        if self.rect.y <= 0:
            self.speed = 1.0
            self.rect.x += -20
        elif self.rect.y >= 570:
            self.speed = -1.0
            self.rect.x += -20

    def update(self, screen):
        self.move()
        screen.blit(self.image, self.rect)


class EnemyGroup(Group):
    def __init__(self, num_of_enemy):
        super().__init__()
        for i in range(num_of_enemy):
            enemy = Enemy(random.randint(350, 750), random.randint(0, 350), 1.0)
            self.add(enemy)

    def move(self):
        for enemy in self.sprites():
            enemy.move()

    def update(self, screen):
        for enemy in self.sprites():
            enemy.update(screen)
