import pygame
from settings import *


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # print("Target rect:", target.rect)
        x = -target.rect.x + int(DISPLAY_WIDTH / 2)
        y = -target.rect.y + int(DISPLAY_HEIGHT / 2)
        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - DISPLAY_WIDTH), x)  # right
        y = max(-(self.height - DISPLAY_HEIGHT), y)  # bottom
        # print("x=", x, ", y=", y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
