# PXTRICK08s CHESS GAME

import pygame
from chess.constants import WIDTH, HEIGHT, FPS
from chess.board import Board

# Create window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pxtrick08s Chess Game")


def main():
    running: bool = True
    clock = pygame.time.Clock()
    board = Board()
    print(board.pieces)

    while running:
        # Check for user interaction 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.draw_board_pattern(WINDOW)
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()