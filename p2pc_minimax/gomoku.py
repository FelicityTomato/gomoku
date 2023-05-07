import pygame as pg
from gomokuPiece import Piece
from gomokuBoard import *
from minimax import pc_turn

class gomokuGame(gomokuBoard):
    
    def pc_turn(self):
        pc_turn(self, ROWS, COLS)
        
    

if __name__ == '__main__':
    
    while True:
        pg.init()
        game = gomokuGame('GoMoKu', pg)
        game.run()
        pg.quit()

        if input("Play again?(y/N) ").upper() != "Y" :
            break
            