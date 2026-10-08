# BOARD CREATION

import pygame
from .constants import BOARD_SIZE, SQUARE_SIZE, WHITE, BLACK, BLUE, START_BOARD, PADDING
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.pieces = self.create_pieces()
         
    def create_pieces(self):
        self.pieces = []
        for row in range(BOARD_SIZE):
            self.board.append([])
            for col in range( BOARD_SIZE):
                code = START_BOARD[row][col]
                if code != "--":
                    self.board[row].append(Piece(color = code[0], rank = code[1], start_pos = {"row": row, "col": col}))
                else:
                    self.board[row].append("--")
        return self.pieces   
 
    def draw_board_pattern(self, window):
        for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    square_color = WHITE if (row + col) % 2 == 0 else BLACK
                    pygame.draw.rect(window, square_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, WINDOW):
        for row in self.board:
                    for piece in row:
                        if piece != "--":
                            piece.draw_image(WINDOW) 

    def get_piece(self, row, col):
            return self.board[row][col]

    def validate_moves(self, moves):
        pass

    def draw_moves(self, window, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2 , row * SQUARE_SIZE + SQUARE_SIZE//2), (SQUARE_SIZE//2-PADDING), width = 0)

    def move_piece(self, selected_piece, pos, WINDOW):
            #Change old board position to "--"
            self.board[selected_piece.position["row"]][selected_piece.position["col"]] = "--"
            #Change position of the piece
            selected_piece.position["row"], selected_piece.position["col"] = pos
            #Change new board position to selected piece
            self.board[selected_piece.position["row"]][selected_piece.position["col"]] = selected_piece
            selected_piece.draw_image(WINDOW) 
            selected_piece.movement = selected_piece.get_movement()
