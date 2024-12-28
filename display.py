import pygame
import settings

pygame.font.init()


class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(
            settings.FONTS_DIR + "PressStart2P-Regular.ttf", 16
        )
        self.game_over_font = pygame.font.Font(
            settings.FONTS_DIR + "PressStart2P-Regular.ttf", 24
        )
        self.text_color = pygame.Color("white")

    def show_life(self, life):
        img_path = "assets/life/life.png"
        life_image = pygame.image.load(img_path)
        life_image = pygame.transform.scale(
            life_image, (settings.CHAR_SIZE, settings.CHAR_SIZE)
        )
        life_x = settings.CHAR_SIZE // 2

        if life != 0:
            for life in range(life):
                self.screen.blit(
                    life_image, (life_x, settings.HEIGHT + (settings.CHAR_SIZE // 2))
                )
                life_x += settings.CHAR_SIZE

    def show_level(self, level):
        level_x = settings.WIDTH // 3
        level = self.font.render(f"Level {level}", True, self.text_color)
        self.screen.blit(
            level, (level_x, (settings.HEIGHT + (settings.CHAR_SIZE // 2)))
        )

    def show_score(self, score):
        score_x = settings.WIDTH // 3
        score = self.font.render(f"{score}", True, self.text_color)
        self.screen.blit(
            score, (score_x * 2, (settings.HEIGHT + (settings.CHAR_SIZE // 2)))
        )

    def game_over(self):
        message = self.game_over_font.render(
            f"GAME OVER!!", True, pygame.Color("chartreuse")
        )
        instruction = self.font.render(
            f'Press "R" to Restart', True, pygame.Color("aqua")
        )
        self.screen.blit(message, ((settings.WIDTH // 4), (settings.HEIGHT // 3)))
        self.screen.blit(instruction, ((settings.WIDTH // 4), (settings.HEIGHT // 2)))
