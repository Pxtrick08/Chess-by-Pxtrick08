# PXTRICK08s CHESS GAME

import pygame
from chess.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE, BOARD_SIZE
from chess.board import Board
from chess.piece import Piece



# Create window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pxtrick08s Chess Game")

def get_pos_mouseclick(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col

def main():
    running: bool = True
    clock = pygame.time.Clock()
    board = Board()
    selected_piece = "--"

    

    while running:

        board.draw_board_pattern(WINDOW)
        for row in board.board:
            for piece in row:
                if piece != "--":
                    position = piece.calc_image_position()
                    image = piece.load_img()
                    scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
                    WINDOW.blit(scaled_image, position)

        # Check for user interaction 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_mouseclick(pos)
                selected_piece = board.get_piece(row, col)
                
                
        if selected_piece != "--":
            board.draw_moves(WINDOW, selected_piece, selected_piece.movement)
    
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()