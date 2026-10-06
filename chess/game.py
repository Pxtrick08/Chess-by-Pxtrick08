import pygame
from .constants import BLACK, WHITE
from .board import *

class Game: 
    def __init__(self, selected_piece = "--",):
        self.board = Board()
        self.turn = WHITE
        self.selected_piece = selected_piece
        self.win = False
        