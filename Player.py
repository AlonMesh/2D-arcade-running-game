import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # self.image = pygame.Surface((20, 54))  # (x,y)
        # self.image.fill((72, 113, 196))
        self.image = pygame.image.load("PNG/Players/Player Blue/playerBlue_stand.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (22.5, 27))
        print(self.image.get_height(), "x", self.image.get_width())
        self.rect = self.image.get_rect(topleft=position)
        self.score = 0

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -15
        self.moves_left = False
        self.moves_right = False
        self.in_jump = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = self.speed
            self.moves_left = False
            self.moves_right = True
            self.score += 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1 * self.speed
            self.moves_left = True
            self.moves_right = False
            self.score -= 1
        else:
            self.direction.x = 0
            self.moves_left = False
            self.moves_right = False

        if keys[pygame.K_SPACE] and self.in_jump is False:
            self.jump()
            self.in_jump = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
