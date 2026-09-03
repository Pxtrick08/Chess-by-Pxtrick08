# CONSTANTS

import pygame
from typing import Literal

# board setup
START_BOARD = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

# colors
WHITE = (197,161,108)
BLACK = (123,79,45)
BLUE = (0, 0, 255)
COLORS = ["w", "b"]

# sizes
WIDTH, HEIGHT= 1000, 1000
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
PADDING = 30

# refresh rate
FPS = 60