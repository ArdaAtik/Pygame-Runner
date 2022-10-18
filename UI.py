import pygame
import math


class UI(pygame.sprite.Sprite):
    current_time = 0

    def __init__(self, text, color, x_pos, y_pos):
        super(UI, self).__init__()
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)  # scores and shessh
        self.image = self.font.render(text, False, color)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def display_score(self, start_time=0):
        current_time = math.floor(pygame.time.get_ticks() / 100) - start_time
        self.image = self.font.render(f'Score : {current_time}', False, (64, 64, 64))
        self.rect = self.image.get_rect(center=(400, 50))
        UI.current_time = current_time
