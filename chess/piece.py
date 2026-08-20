# PIECE CREATION

import pygame
from typing import Literal
from .constants import SQUARE_SIZE


class Piece:
    def __init__(self, color, rank, start_pos):
        self.color = color
        self.rank = rank
        self.position = start_pos
        self.king: bool = (self.rank == "K")
        self.img = self.load_img()


    def __repr__(self):
        return f"{self.color}{self.rank}"

    def calc_image_position(self):
        pixel_pos = (self.position["col"]*SQUARE_SIZE, self.position["row"]*SQUARE_SIZE)
        return pixel_pos

    def load_img(self):
        return pygame.image.load(f"Images/{self.color}{self.rank}.svg")


    