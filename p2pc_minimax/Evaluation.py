import random
import judge
ROWS = 7
COLS = 7


def evaluation(grid,turn):
    plus = (0,1,1,8,17,77)
    minus = (0,1,1,20,68,94)
    p = (1,0,0,1,1,1,1,-1)
    value = 0
    for i in range(ROWS):
        for j in range(COLS):    
            for t in range(4):
                if i-p[t*2]<0 or j-p[t*2+1]<0 \
                    or i-p[t*2]>=ROWS or j-p[t*2+1]>=COLS \
                    or grid[i-p[t*2]][j-p[t*2+1]]!=grid[i][j]:
                    for k in range(5):
                        if grid[i][j]!=0 \
                            and i+k*p[t*2]<ROWS and i+k*p[t*2]>=0 and j+k*p[t*2+1]<COLS and j+k*p[t*2+1]>=0 \
                            and grid[i+k*p[t*2]][j+k*p[t*2+1]]==grid[i][j]:
                            if k==4:
                                if grid[i][j]==turn: value+=plus[k+1]
                                else: value-=minus[k+1]
                                break
                        else:
                            if grid[i][j]==turn: value+=plus[k]
                            else: value-=minus[k]
                            break
    return value

def pr():
    for i in range(ROWS):
        for j in range(COLS):
            print(grid[i][j], end=' ')
        print(end='\n')

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
                    v=evaluation(grid,2)
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
                    v=evaluation(grid,1)
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