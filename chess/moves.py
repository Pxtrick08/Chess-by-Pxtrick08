# CREATE VALID MOVES

import pygame
from .constants import BOARD_SIZE


def king_movement(row, col):
    possible_moves = []
    for x in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            possible_moves.append((row + x, col + i))
    possible_moves.remove((row, col))
    return possible_moves

def b_pawn_movement(row, col):
    possible_moves = []
    x = 1
    for i in [-1, 0, 1]:
        possible_moves.append((row + x, col + i))
    possible_moves.append((row + 2, col))
    return possible_moves

def w_pawn_movement(row, col):
    possible_moves = []
    x = -1
    for i in [-1, 0, 1]:
        possible_moves.append((row + x, col + i))
    possible_moves.append((row - 2, col))
    return possible_moves

def knight_movement(row, col):
    possible_moves = []
    for x in [-1, 1]:
        for i in [-2, 2]:
            possible_moves.append((row + x, col + i))
            possible_moves.append((row + i, col + x))
    return possible_moves

def x_movement(row, col):
    possible_moves = []
    for x in range(-BOARD_SIZE, BOARD_SIZE):
        possible_moves.append((row + x, col + x))
        possible_moves.append((row - x, col + x))
    possible_moves.remove((row, col))
    possible_moves.remove((row, col))
    return possible_moves

def cross_movement(row, col):
    possible_moves = []
    for x in range(-BOARD_SIZE, BOARD_SIZE):
        possible_moves.append((row + x, col))
        possible_moves.append((row, col + x))
    possible_moves.remove((row, col))
    return possible_moves

