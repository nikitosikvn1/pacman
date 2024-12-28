import sys, os
import argparse
import pygame
import settings

from pprint import pprint
from typing import List, Tuple
from parse import CellType, parse_maze
from world import World


class Main:
    def __init__(self, screen, maze):
        self.screen = screen
        self.maze = maze
        self.FPS = pygame.time.Clock()

    def main(self):
        world = World(self.screen, self.maze)
        while True:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            world.update()
            pygame.display.update()
            self.FPS.tick(30)


def load_maze_from_file(file_path: str) -> str:
    if not os.path.isfile(file_path):
        print(f"Error: Maze file '{file_path}' not found.")
        sys.exit(1)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            map_str = f.read()
        return map_str
    except Exception as e:
        print(f"Error reading the map file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Launching the Pacman game with the specified maze."
    )
    parser.add_argument(
        "--maze",
        type=str,
        default=None,
        help="Path to the file with the maze. If not specified, the default maze is used.",
    )
    args = parser.parse_args()

    if args.maze:
        maze = load_maze_from_file(args.maze)
    else:
        maze = settings.DEFAULT_MAZE

    maze = parse_maze(maze)

    settings.BOARD_RATIO = (len(maze[0]), len(maze))
    settings.WIDTH, settings.HEIGHT = (
        settings.BOARD_RATIO[0] * settings.CHAR_SIZE,
        settings.BOARD_RATIO[1] * settings.CHAR_SIZE,
    )

    print(f"Width: {settings.WIDTH}, Height: {settings.HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT + settings.NAV_HEIGHT)
    )
    pygame.display.set_caption("Pacman")

    play = Main(screen, maze)
    play.main()
