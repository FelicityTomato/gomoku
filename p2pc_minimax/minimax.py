import Evaluation
import judge
import random

ROWS = 7
COLS = 7

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


def pr():
    for i in range(ROWS):
        for j in range(COLS):
            print(grid[i][j], end=' ')
        print(end='\n')

def run_e(grid):
    mx1=-1e9
    idx1=[]
    mx2=-1e9
    idx2=[]
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]==0:
                grid[i][j]=2
                v=Evaluation.evaluation(grid,2)
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
                v=Evaluation.evaluation(grid,1)
                if v>mx1:
                    mx1=v
                    idx1=[i,j]
                elif v==mx1:
                    idx1.append(i)
                    idx1.append(j)
                grid[i][j]=0
    if mx1>mx2:
        t=random.randint(1,len(idx1)/2)
        return (mx1,idx1[2*t-2],idx1[2*t-1])
    else:
        t=random.randint(1,len(idx2)/2)
        return (mx2,idx2[2*t-2],idx2[2*t-1])

def dfs(grid,depth,alpha,beta):
    x=0
    y=0
    if depth==2:
        #print(times, end="")
        #return run_e(grid)
        return (Evaluation.evaluation(grid,2),-1,-1)
    if depth%2==0:
        mx=1e9
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=2
                    #Evaluation.evaluation(grid,2)
                    score,a,b=dfs(grid,depth+1,alpha,beta)
                    #score*=-1
                    if score<mx:
                        mx=score
                        x,y=i,j
                    grid[i][j]=0
                    beta=min(beta,score)
                    if beta<=alpha: break
        return (mx,x,y)
    else:
        mx=-1e9
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=1
                    #Evaluation.evaluation(grid,1)
                    score,a,b=dfs(grid,depth+1,alpha,beta)
                    #score*=-1
                    if score>mx:
                        mx=score
                        x,y=i,j
                    grid[i][j]=0
                    alpha=max(alpha,score)
                    if beta<=alpha: break
        return (mx,x,y)



if __name__ == '__main__':
    grid=[[0]*COLS for _ in range(ROWS)]
    pr()
    while True:
        r=int(input("your row: "))
        c=int(input("your column: "))
        grid[r][c]=1
        a=judge.judge(grid)
        if a==1:
            print("black win")
            break
        elif a==2:
            print("white win")
            break

        mx1=-1e9
        idx1=[]
        mx2=-1e9
        idx2=[]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    grid[i][j]=2
                    v=Evaluation.evaluation(grid,2)
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
                    v=Evaluation.evaluation(grid,1)
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
        pr()
        a=judge.judge(grid)
        if a==1:
            print("black win")
            break
        elif a==2:
            print("white win")
            break    
    pr()