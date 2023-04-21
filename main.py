import pygame
from sys import exit
from settings import *
from Tiles import Tile
from Level import Level

## Generating levels
## Make GUI / choosing a normal level or generated

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

background1 = pygame.image.load("PNG/Backgrounds/set1_background.png").convert_alpha()
background1 = pygame.transform.scale(background1, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

background2 = pygame.image.load("PNG/Backgrounds/set3_tiles.png").convert_alpha()
background2 = pygame.transform.scale(background2, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

background = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
background.blit(background1, (0, 0))
background.blit(background2, (0, 0))

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
    screen.blit(background, (0, 0))

    level.run()

    # Update the screen
    pygame.display.update()
    clock.tick(60)
