import Evaluation
import judge
import random

ROWS = 15
COLS = 15

def contest(rand1,rand2,rand3,rand4):
    times=1
    grid=[[0]*COLS for _ in range(ROWS)]
    grid[7][7]=1
    while times<=224:   
        times+=2   
        mx1=-1e9
        idx1=[]
        mx2=-1e9
        idx2=[]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=2
                    v=Evaluation.evaluation(grid,2,rand3,rand4)
                    if v>mx2:
                        mx2=v
                        idx2=[i,j]
                    elif v==mx2:
                        idx2.append(i)
                        idx2.append(j)
                    grid[i][j]=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=1
                    v=Evaluation.evaluation(grid,1,rand3,rand4)
                    if v>mx1:
                        mx1=v
                        idx1=[i,j]
                    elif v==mx1:
                        idx1.append(i)
                        idx1.append(j)
                    grid[i][j]=0
        if mx1>mx2:
            t=random.randint(1,len(idx1)/2)
            grid[idx1[2*t-2]][idx1[2*t-1]]=2
        else:
            t=random.randint(1,len(idx2)/2)
            grid[idx2[2*t-2]][idx2[2*t-1]]=2
        a=judge.judge(grid)
        if a!=0: return a

        mx1=-1e9
        idx1=[]
        mx2=-1e9
        idx2=[]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=1
                    v=Evaluation.evaluation(grid,1,rand1,rand2)
                    if v>mx2:
                        mx2=v
                        idx2=[i,j]
                    elif v==mx2:
                        idx2.append(i)
                        idx2.append(j)
                    grid[i][j]=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=2
                    v=Evaluation.evaluation(grid,2,rand1,rand2)
                    if v>mx1:
                        mx1=v
                        idx1=[i,j]
                    elif v==mx1:
                        idx1.append(i)
                        idx1.append(j)
                    grid[i][j]=0
        if mx1>mx2:
            t=random.randint(1,len(idx1)/2)
            grid[idx1[2*t-2]][idx1[2*t-1]]=1
        else:
            t=random.randint(1,len(idx2)/2)
            grid[idx2[2*t-2]][idx2[2*t-1]]=1
        a=judge.judge(grid)
        if a!=0: return a
    return a

def hash(rand):
    k=0
    for i in rand:
        k+=i*100
    return k

if __name__ == '__main__':
    times=0
    set_s=set()
    rand3=[1, 1, 1, 1]
    rand4=[1, 1, 1, 1]
    set_s.add(hash(rand3+rand4))
    while len(set_s)<1e10:
        rand1=[1,3,10,30]
        rand2=[1,3,10,30]
        for i in range(4): rand1[i]=random.randint(1,100)
        for i in range(4): rand2[i]=random.randint(1,100)
        rand1.sort()
        rand2.sort()
        if hash(rand1+rand2) in set_s: continue
        set_s.add(hash(rand1+rand2))
        a=contest(rand1,rand2,rand3,rand4)
        if a!=1: 
            print("2:",rand1,rand2,times)
            times+=1
            if times==50:
                print(rand3,rand4)
                break
        else:
            times=0
            rand3=rand1
            rand4=rand2
            print("1:",rand1,rand2)