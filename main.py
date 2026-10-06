# PXTRICK08s CHESS GAME

import pygame
from chess.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE, BOARD_SIZE
from chess.game import Game
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
    game = Game()
    #board = Board()
    selected_piece = "--"

    

    while running:

        game.board.draw_board_pattern(WINDOW)
        game.board.draw_pieces(WINDOW)
        
        
        # Check for user interaction 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_piece == "--":
                    pos = pygame.mouse.get_pos()
                    row, col = get_pos_mouseclick(pos)
                    selected_piece = game.board.get_piece(row, col)
                else:
                    pos = pygame.mouse.get_pos()
                    row, col = get_pos_mouseclick(pos)
                    selected_piece.move((row, col), WINDOW)
                
                
        if selected_piece != "--":
            game.board.draw_moves(WINDOW, selected_piece.movement)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()