import pygame as pg
from gomokuPiece import Piece
from gomokuBoard import *
import judge
import Evaluation
import random
import minimax

class gomokuGame(gomokuBoard):

    def judge(self, x, y, turn):
        win = judge.judge(self.grid)
        if win==1: self.message("Black Win")
        elif win==2: self.message("white Win")
        return win
        
    def pc_turn(self):
        mx,x,y=minimax.dfs(self.grid,0,-1e9,1e9)
        self.play(x,y)
        #print(mx)
        #self.play(idx[2*t-2],idx[2*t-1])
        


if __name__ == '__main__':
    
    #while True:
    pg.init()
    game = gomokuGame('GoMoKu', pg)
    game.run()
    pg.quit()

    #    if input("Play again?(y/N) ").upper() != "Y" :
    #        break
            