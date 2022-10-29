import pygame


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, window):
        action = False

        # Mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is over the button
        if self.rect.collidepoint(mouse_pos):
            # Check if mouse is clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # Reset mouse click
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        window.blit(self.image, (self.rect.x, self.rect.y))
        return action
