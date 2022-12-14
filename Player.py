import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def set_gravity_zero(self):
        self.gravity = 0
        self.rect = self.image.get_rect(midbottom=(80, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 and not pygame.time.get_ticks() == 0:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()

    def animate(self):
        if self.rect.bottom < 300:
            # jump animation
            self.image = self.player_jump
        else:  # walk animation
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
