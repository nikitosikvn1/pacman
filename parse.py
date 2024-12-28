from enum import Enum
from typing import List, Tuple


class CellType(Enum):
    EMPTY = 0
    BIG_DOT = 1
    WALL = 2
    DOOR = 3
    PACMAN = 4
    GHOST_RED = 5
    GHOST_PINK = 6
    GHOST_ORANGE = 7
    GHOST_SKYBLUE = 8

    @staticmethod
    def from_char(char: str) -> "CellType":
        mapping = {
            " ": CellType.EMPTY,
            "B": CellType.BIG_DOT,
            "1": CellType.WALL,
            "P": CellType.PACMAN,
            "r": CellType.GHOST_RED,
            "p": CellType.GHOST_PINK,
            "o": CellType.GHOST_ORANGE,
            "s": CellType.GHOST_SKYBLUE,
        }
        return mapping.get(char, CellType.EMPTY)


def parse_maze(input_str: str) -> List[List[CellType]]:
    lines = input_str.strip().split("\n")
    # assert all(
    #     len(line) == len(lines[0]) for line in lines
    # ), "All lines must have the same length"

    return [[CellType.from_char(cell) for cell in row] for row in lines]
