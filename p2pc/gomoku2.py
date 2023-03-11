import pygame as pg
from gomokuPiece import Piece
from gomokuBoard import *
import judge
import Evaluation
import Evaluation2
import random

class gomokuGame(gomokuBoard):

    def judge(self, x, y, turn):
        win = judge.judge(self.grid)
        if win==1: self.message("Black Win")
        elif win==2: self.message("white Win")
        return win
        
    def pc_turn(self):
        mx1=-1e9
        idx1=[]
        mx2=-1e9
        idx2=[]
        for i in range(ROWS):
            for j in range(COLS):
                if self.grid[i][j]==0:
                    self.grid[i][j]=2
                    v=Evaluation2.evaluation(self.grid,2,i,j)
                    if v>mx2:
                        mx2=v
                        idx2=[i,j]
                    elif v==mx2:
                        idx2.append(i)
                        idx2.append(j)
                    self.grid[i][j]=0
        for i in range(ROWS):
            for j in range(COLS):
                if self.grid[i][j]==0:
                    self.grid[i][j]=1
                    v=Evaluation2.evaluation(self.grid,1,i,j)
                    if v>mx1:
                        mx1=v
                        idx1=[i,j]
                    elif v==mx1:
                        idx1.append(i)
                        idx1.append(j)
                    self.grid[i][j]=0
        if mx1>mx2:
            t=random.randint(1,len(idx1)/2)
            self.grid[idx1[2*t-2]][idx1[2*t-1]]=2
            self.play(idx1[2*t-2],idx1[2*t-1])
        else:
            t=random.randint(1,len(idx2)/2)
            self.grid[idx2[2*t-2]][idx2[2*t-1]]=2
            self.play(idx2[2*t-2],idx2[2*t-1])
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
            