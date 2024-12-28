import pygame
import time
import settings

from pac import Pac
from cell import Cell
from berry import Berry
from ghost import Ghost
from display import Display
from parse import CellType


class World:
    def __init__(self, screen, maze):
        self.screen = screen
        self.maze = maze

        self.player = pygame.sprite.GroupSingle()
        self.ghosts = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.berries = pygame.sprite.Group()

        self.display = Display(self.screen)

        self.game_over = False
        self.reset_pos = False
        self.player_score = 0
        self.game_level = 1

        self._generate_world()

    def _generate_world(self):
        for y_index, col in enumerate(self.maze):
            for x_index, char in enumerate(col):
                match char:
                    case CellType.WALL:
                        self.walls.add(
                            Cell(
                                x_index, y_index, settings.CHAR_SIZE, settings.CHAR_SIZE
                            )
                        )
                    case CellType.EMPTY:
                        self.berries.add(
                            Berry(x_index, y_index, settings.CHAR_SIZE // 8)
                        )
                    case CellType.BIG_DOT:
                        self.berries.add(
                            Berry(
                                x_index,
                                y_index,
                                settings.CHAR_SIZE // 4,
                                is_power_up=True,
                            )
                        )
                    case CellType.GHOST_SKYBLUE:
                        self.ghosts.add(Ghost(x_index, y_index, "skyblue"))
                    case CellType.GHOST_PINK:
                        self.ghosts.add(Ghost(x_index, y_index, "pink"))
                    case CellType.GHOST_ORANGE:
                        self.ghosts.add(Ghost(x_index, y_index, "orange"))
                    case CellType.GHOST_RED:
                        self.ghosts.add(Ghost(x_index, y_index, "red"))
                    case CellType.PACMAN:
                        self.player.add(Pac(x_index, y_index))

        self.walls_collide_list = [wall.rect for wall in self.walls.sprites()]

    def generate_new_level(self):
        for y_index, col in enumerate(self.maze):
            for x_index, char in enumerate(col):
                if char == CellType.EMPTY:  # for paths to be filled with berries
                    self.berries.add(Berry(x_index, y_index, settings.CHAR_SIZE // 8))
                elif char == CellType.BIG_DOT:  # for big berries
                    self.berries.add(
                        Berry(
                            x_index, y_index, settings.CHAR_SIZE // 4, is_power_up=True
                        )
                    )
        time.sleep(2)

    def restart_level(self):
        self.berries.empty()
        [ghost.move_to_start_pos() for ghost in self.ghosts.sprites()]
        self.game_level = 1
        self.player.sprite.pac_score = 0
        self.player.sprite.life = 3
        self.player.sprite.move_to_start_pos()
        self.player.sprite.direction = (0, 0)
        self.player.sprite.status = "idle"
        self.generate_new_level()

    def _dashboard(self):
        nav = pygame.Rect(0, settings.HEIGHT, settings.WIDTH, settings.NAV_HEIGHT)
        pygame.draw.rect(self.screen, pygame.Color("black"), nav)

        self.display.show_life(self.player.sprite.life)
        self.display.show_level(self.game_level)
        self.display.show_score(self.player.sprite.pac_score)

    def _check_game_state(self):
        if self.player.sprite.life == 0:
            self.game_over = True

        if len(self.berries) == 0 and self.player.sprite.life > 0:
            self.game_level += 1
            for ghost in self.ghosts.sprites():
                ghost.move_speed += self.game_level
                ghost.move_to_start_pos()

            self.player.sprite.move_to_start_pos()
            self.player.sprite.direction = (0, 0)
            self.player.sprite.status = "idle"
            self.generate_new_level()

    def update(self):
        if not self.game_over:
            pressed_key = pygame.key.get_pressed()
            self.player.sprite.animate(pressed_key, self.walls_collide_list)

            if self.player.sprite.rect.right <= 0:
                self.player.sprite.rect.x = settings.WIDTH
            elif self.player.sprite.rect.left >= settings.WIDTH:
                self.player.sprite.rect.x = 0

            for berry in self.berries.sprites():
                if self.player.sprite.rect.colliderect(berry.rect):
                    if berry.power_up:
                        self.player.sprite.immune_time = (
                            150  # Timer based from FPS count
                        )
                        self.player.sprite.pac_score += 50
                    else:
                        self.player.sprite.pac_score += 10
                    berry.kill()

            for ghost in self.ghosts.sprites():
                if self.player.sprite.rect.colliderect(ghost.rect):
                    if not self.player.sprite.immune:
                        time.sleep(2)
                        self.player.sprite.life -= 1
                        self.reset_pos = True
                        break
                    else:
                        ghost.move_to_start_pos()
                        self.player.sprite.pac_score += 100

        self._check_game_state()

        [wall.update(self.screen) for wall in self.walls.sprites()]
        [berry.update(self.screen) for berry in self.berries.sprites()]
        [ghost.update(self.walls_collide_list) for ghost in self.ghosts.sprites()]
        self.ghosts.draw(self.screen)

        self.player.update()
        self.player.draw(self.screen)
        self.display.game_over() if self.game_over else None

        self._dashboard()

        if self.reset_pos and not self.game_over:
            [ghost.move_to_start_pos() for ghost in self.ghosts.sprites()]
            self.player.sprite.move_to_start_pos()
            self.player.sprite.status = "idle"
            self.player.sprite.direction = (0, 0)
            self.reset_pos = False

        if self.game_over:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_r]:
                self.game_over = False
                self.restart_level()
