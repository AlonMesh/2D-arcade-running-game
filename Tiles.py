import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))  # (x,y)
        self.image.fill((30, 104, 24))
        self.rect = self.image.get_rect(topleft=position)

    # Move the screen in x line, left is positive, right is negative
    def update(self, x_shift):
        self.rect.x += x_shift
