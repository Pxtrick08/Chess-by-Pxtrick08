# PIECE CREATION

import pygame
from typing import Literal
from .constants import SQUARE_SIZE, BOARD_SIZE
from .moves import *


class Piece:
    def __init__(self, color, rank, start_pos):
        self.color = color
        self.rank = rank
        self.position: dict = start_pos
        self.king: bool = (self.rank == "K")
        self.img = self.load_img()
        self.movement = self.get_movement()

    def __repr__(self):
        return f"{self.color}{self.rank}"

    def calc_image_position(self):
        pixel_pos = (self.position["col"]*SQUARE_SIZE, self.position["row"]*SQUARE_SIZE)
        return pixel_pos

    def load_img(self):
        return pygame.image.load(f"Images/{self.color}{self.rank}.svg")

    def draw_image(self, WINDOW):
        position = self.calc_image_position()
        image = self.load_img()
        scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        WINDOW.blit(scaled_image, position) 

    def get_movement(self):
        possible_moves = []
        if self.rank == "K":
            possible_moves.extend(king_movement(self.position["row"], self.position["col"]))
        elif self.rank == "Q":
            possible_moves.extend(king_movement(self.position["row"], self.position["col"]))
            possible_moves.extend(x_movement(self.position["row"], self.position["col"]))
        elif self.rank == "B":
            possible_moves.extend(x_movement(self.position["row"], self.position["col"]))
        elif self.rank == "N":
            possible_moves.extend(knight_movement(self.position["row"], self.position["col"]))
        elif self.rank == "R":
            possible_moves.extend(cross_movement(self.position["row"], self.position["col"]))
        elif self.rank == "P" and self.color == "b":
            possible_moves.extend(b_pawn_movement(self.position["row"], self.position["col"]))
        elif self.rank == "P" and self.color == "w":
            possible_moves.extend(w_pawn_movement(self.position["row"], self.position["col"]))
        return possible_moves

    def move(self, pos, WINDOW):
        self.position["row"], self.position["col"] = pos
        self.draw_image(WINDOW) 
        self.movement = self.get_movement()

    