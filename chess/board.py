# BOARD CREATION

import pygame
from .constants import BOARD_SIZE, SQUARE_SIZE, WHITE, BLACK, COLORS
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.pieces = []
        piece_ranks = [
                    {"rank": "K", "value": 0, "piece_count": 1},
                    {"rank": "Q", "value": 0, "piece_count": 1},
                    {"rank": "R", "value": 0, "piece_count": 2},
                    {"rank": "B", "value": 0, "piece_count": 2},  
                    {"rank": "N", "value": 0, "piece_count": 2},
                    {"rank": "P", "value": 0, "piece_count": 8}
                ]
        for color in COLORS:
            for rank in piece_ranks:
                for piece_number in range(rank["piece_count"]):
                    piece_number += 1
                    self.pieces.append(Piece(rank, color, piece_number))
                
                  

    def draw_board_pattern(self, window):
        for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    square_color = WHITE if (row + col) % 2 == 0 else BLACK
                    pygame.draw.rect(window, square_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))