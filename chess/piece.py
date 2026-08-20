# PIECE CREATION

import pygame
from typing import Literal

class Piece:
    def __init__(self, rank: dict, color: Literal["w", "b"], piece_number):
        self.rank = rank
        self.color = color
        self.piece_number = piece_number
        self.king = False if rank != "K" else self.king = True

    def __repr__(self):
        return f"{self.color}{self.rank["rank"]} ({self.piece_number})"