# BOARD CREATION

import pygame
from .constants import BOARD_SIZE, SQUARE_SIZE, WHITE, BLACK, COLORS
from .piece import *

class Board:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["--", "--","--", "--","--", "--","--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        # Create all pieces
        self.pieces = []
        for row in range(BOARD_SIZE):
            for col in range( BOARD_SIZE):
                code = self.board[row][col]
                if code != "--":
                    self.pieces.append(Piece(color = code[0], rank = code[1], start_pos = {"row": row, "col": col}))
                
                
                  

    def draw_board_pattern(self, window):
        for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    square_color = WHITE if (row + col) % 2 == 0 else BLACK
                    pygame.draw.rect(window, square_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))