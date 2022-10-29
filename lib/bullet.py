import pygame
from pygame.locals import *
from pygame.sprite import Sprite


# Initialize class
class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/Bullet Nizar.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.speed = 5.0

    # Bullet movement
    def move(self):
        self.rect.x += self.speed

    # Update bullet
    def update(self, screen):
        self.move()
        screen.blit(self.image, self.rect)

        # Delete bullet when it goes off screen
        if self.rect.x > 800:
            self.kill()
