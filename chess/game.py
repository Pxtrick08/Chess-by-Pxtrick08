import pygame
from .constants import BLACK, WHITE
from .board import *

class Game: 
    def __init__(self, selected_piece = "--",):
        self.board = Board()
        self.move_counter = 0
        self.turn = "w"
        self.selected_piece = selected_piece
        self.win = False

    def update_turn(self):
        self.turn = "w" if (self.move_counter % 2) == 0 else "b"

    def get_pos_mouseclick(self, pos):
        x, y = pos
        row = y//SQUARE_SIZE
        col = x//SQUARE_SIZE
        return row, col

    def move(self, WINDOW):
        pos = pygame.mouse.get_pos()
        row, col = self.get_pos_mouseclick(pos)
        if (row, col) in self.selected_piece.movement:
            self.board.move_piece(self.selected_piece, (row, col), WINDOW)
            self.move_counter += 1
            self.update_turn()
        self.selected_piece = "--"

    def select(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_pos_mouseclick(pos)
        if self.board.get_piece(row, col) != "--":
            self.selected_piece = self.board.get_piece(row, col) if self.board.get_piece(row, col).color == self.turn else "--"