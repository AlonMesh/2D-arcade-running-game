import pygame
from Tiles import Tile
from settings import *
from Player import Player
from Camera import Camera


class Level:
    def __init__(self, level_map_data, surface):
        # Setup the level
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()  # Creating a group of tiles
        self.req_to_advance = 0
        self.setup(level_map_data)
        self.display_surface = surface  # Where the level will be displayed
        self.world_shift = 0  # The speed shifting of the camera on x line
        self.camera = Camera(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.left_edge = self.find_left_edge()

    def setup(self, layout):
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

        if player_x < (DISPLAY_WIDTH / 4) and player.moves_left and self.find_left_edge() < 0:
            self.world_shift = 5
            self.player.sprite.speed = 0
        elif player.moves_left and self.left_edge > player.rect.left:
            player.rect.left = 0
            player.score += 1
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
                    player.score += 1
                elif player.moves_right:
                    player.rect.right = sprite.rect.left
                    player.score -= 1

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
            player.rect.bottom = DISPLAY_HEIGHT - 30
            player.rect.left -= 50

    def find_left_edge(self):
        min1 = 100
        for tile in self.tiles:
            min1 = min(min1, tile.rect.x)
        return min1

    def score_board(self):
        font = pygame.font.Font(None, 50)
        txt_surface = font.render(f'Score: {self.player.sprite.score}', False, (30, 142, 58))
        self.display_surface.blit(txt_surface, (0, 0))

    def generate_continue(self):
        # Generate new map
        # new_map = generate_random_map()
        new_map = generate_random_map()

        # Set up the new map and player
        old_tiles = self.tiles.sprites().copy()
        right_edge = max(tile.rect.right for tile in old_tiles)

        for row_index, row in enumerate(new_map):
            for col_index, cell in enumerate(row):
                x = right_edge + col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

        # Remove old tiles that are not visible anymore
        for tile in old_tiles:
            if tile.rect.right < right_edge and tile.rect.right < self.player.sprite.rect.x - 800:
                tile.kill()

    def run(self):
        # Update & draw tiles
        self.tiles.update(self.world_shift)

        #  self.tiles.draw(self.display_surface)
        # Draw tiles
        for tile in self.tiles:
            self.display_surface.blit(tile.image, self.camera.apply(tile))

        self.scroll_x()

        # Update & draw player
        self.player.update()
        # self.player.draw(self.display_surface)
        # Draw player
        self.display_surface.blit(self.player.sprite.image, self.camera.apply(self.player.sprite))
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.camera.update(self.player.sprite)
        self.score_board()
        # self.is_dead()

        if self.player.sprite.score >= self.req_to_advance:
            self.generate_continue()
            self.req_to_advance += 100
