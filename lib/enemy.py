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
            self.speed = random.randint(1, 3)
            self.rect.x += random.randint(-40, -20)
        elif self.rect.y >= 570:
            self.speed = random.randint(-3, -1)
            self.rect.x += random.randint(-40, -20)

    def update(self, screen):
        self.move()
        screen.blit(self.image, self.rect)


class EnemyGroup(Group):
    def __init__(self, num_of_enemy):
        super().__init__()
        for i in range(num_of_enemy):
            enemy = Enemy(random.randint(400, 570), random.randint(20, 150), 1.0)
            self.add(enemy)

    def move(self):
        for enemy in self.sprites():
            enemy.move()

    def update(self, screen):
        for enemy in self.sprites():
            enemy.update(screen)
