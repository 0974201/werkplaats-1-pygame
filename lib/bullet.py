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
        
        
    
