# PXTRICK08s CHESS GAME

import pygame
from chess.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE, BOARD_SIZE
from chess.game import Game
from chess.board import Board
from chess.piece import Piece



# Create window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pxtrick08s Chess Game")



def main():
    running: bool = True
    clock = pygame.time.Clock()
    game = Game()


    while running:

        game.board.draw_board_pattern(WINDOW)
        game.board.draw_pieces(WINDOW)
        
        
        # Check for user interaction 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.selected_piece == "--":
                    game.select()
                else:
                    game.move(WINDOW)
            
        if game.selected_piece != "--":
            game.board.draw_moves(WINDOW, game.selected_piece.movement)
        
        

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()