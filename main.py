import pygame
from sys import exit
from settings import *
from Tiles import Tile
from Level import Level

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

level = Level(level_map_1, screen)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            exit()

    # Clear the screen
    screen.fill('black')
    level.run()

    # Update the screen
    pygame.display.update()
    clock.tick(60)
