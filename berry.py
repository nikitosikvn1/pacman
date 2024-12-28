import pygame
import settings


class Berry(pygame.sprite.Sprite):
    def __init__(self, row, col, size, is_power_up=False):
        super().__init__()
        self.power_up = is_power_up
        self.size = size
        self.color = pygame.Color("yellow")
        self.thickness = size
        self.abs_x = (row * settings.CHAR_SIZE) + (settings.CHAR_SIZE // 2)
        self.abs_y = (col * settings.CHAR_SIZE) + (settings.CHAR_SIZE // 2)

        self.rect = pygame.Rect(self.abs_x, self.abs_y, self.size * 2, self.size * 2)

    def update(self, screen):
        self.rect = pygame.draw.circle(
            screen, self.color, (self.abs_x, self.abs_y), self.size, self.thickness
        )
