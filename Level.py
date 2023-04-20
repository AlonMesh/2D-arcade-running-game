import pygame
from Tiles import Tile
from settings import *
from Player import Player


class Level:
    def __init__(self, level_map_data, surface):
        # Setup the level
        self.setup(level_map_data)
        self.display_surface = surface  # Where the level will be displayed
        self.world_shift = 0

    def setup(self, layout):
        self.tiles = pygame.sprite.Group()  # Creating a group of tiles
        self.player = pygame.sprite.GroupSingle()

        # Checking each cell in the layout (map)
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    # Creating a tile in the cell's indexes and add it to self's tiles group
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    # if there is 2 players throw error
                    singleton_player = Player((x, y))
                    self.player.add(singleton_player)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (DISPLAY_WIDTH / 4) and player.moves_left:
            self.world_shift = 5
            self.player.sprite.speed = 0

        elif player_x > (DISPLAY_WIDTH - (DISPLAY_WIDTH / 4)) and player.moves_right:
            self.world_shift = -5
            self.player.sprite.speed = 0

        else:
            self.world_shift = 0
            self.player.sprite.speed = 5

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x  # the player movement

        # Checks if a player collate any tile
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.moves_left:
                    player.rect.left = sprite.rect.right
                elif player.moves_right:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.in_jump = False

    def is_dead(self):
        player = self.player.sprite

        if player.rect.bottom >= DISPLAY_HEIGHT:
            print("reset")

    def run(self):
        # Update & draw tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Update & draw player
        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.is_dead()
