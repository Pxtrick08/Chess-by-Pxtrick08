# PXTRICK08s CHESS GAME

import pygame
from chess.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE
from chess.board import Board
from chess.piece import Piece

# Create window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pxtrick08s Chess Game")


def main():
    running: bool = True
    clock = pygame.time.Clock()
    board = Board()

    

    while running:
        # Check for user interaction 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.draw_board_pattern(WINDOW)
        for pieces in board.pieces:
            position = Piece.calc_image_position(pieces)
            image = Piece.load_img(pieces)
            scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            WINDOW.blit(scaled_image, position)
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()