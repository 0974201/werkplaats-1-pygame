import pygame
import random
from pygame.sprite import Sprite, Group, collide_rect


# Initialize class
class Enemy(Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy_4.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # Enemy movement
    def move(self):
        self.rect.y += self.speed
        if self.rect.y <= 0:
            self.speed = random.randint(self.speed + 4, self.speed + 4)
            self.rect.x += random.randint(-15, -5)
        elif self.rect.y >= 570:
            self.speed = random.randint(-4, -4)
            self.rect.x += random.randint(-15, -5)

    # Update enemy
    def update(self, screen):
        self.move()
        screen.blit(self.image, self.rect)


# Initialize group class
class EnemyGroup(Group):
    def __init__(self, num_of_enemy):
        super().__init__()
        for i in range(num_of_enemy):
            enemy = Enemy(random.randint(400, 570), random.randint(20, 150), 1.0)
            self.add(enemy)

    # Enemygroup movement
    def move(self):
        for enemy in self.sprites():
            enemy.move()

    # Enemygroup update
    def update(self, screen):
        for enemy in self.sprites():
            enemy.update(screen)
