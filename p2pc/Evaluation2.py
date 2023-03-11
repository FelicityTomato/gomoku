import random
import judge
ROWS = 15
COLS = 15


def evaluation(grid,turn, x, y):
    plus = (0,1,3,10,30,100)#[0, 1, 1, 8, 17, 47]#(0,1,3,10,30,100)
    minus = (0,2,5,9,40,99)#[0, 1, 1, 20, 68, 94]
    p = (1,0,0,1,1,1,1,-1)
    v=0
    cnt=0
    k=1
    for t in range(4):
        while   x-k*p[t*2]>=0 and y-k*p[t*2+1]>=0 \
                and x-k*p[t*2]<ROWS and y-k*p[t*2+1]<COLS \
                and grid[x-k*p[t*2]][y-k*p[t*2+1]]==grid[x][y]:
            cnt+=1
            k+=1
        k=1
        while x+k*p[t*2]<ROWS and x+k*p[t*2]>=0 and y+k*p[t*2+1]<COLS and y+k*p[t*2+1]>=0 \
                and grid[x+k*p[t*2]][y+k*p[t*2+1]]==grid[x][y]:
            cnt+=1
            k+=1
    v=plus[min(cnt+1, 5)]
    k=1
    cnt=0
    for t in range(4):
        while x-k*p[t*2]>=0 and y-k*p[t*2+1]>=0 \
            and x-k*p[t*2]<ROWS and y-k*p[t*2+1]<COLS \
            and grid[x-k*p[t*2]][y-k*p[t*2+1]]!=turn and grid[x-k*p[t*2]][y-k*p[t*2+1]]!=0:
            cnt+=1
            k+=1
        k=1
        while x+k*p[t*2]<ROWS and x+k*p[t*2]>=0 and y+k*p[t*2+1]<COLS and y+k*p[t*2+1]>=0 \
                and grid[x+k*p[t*2]][y+k*p[t*2+1]]!=turn and grid[x+k*p[t*2]][y+k*p[t*2+1]]!=0:
            cnt+=1
            k+=1
    v-=minus[min(cnt+1, 5)]
    return v

def pr():
    for i in range(ROWS):
        for j in range(COLS):
            print(grid[i][j], end=' ')
        print(end='\n')

if __name__ == '__main__':
    grid=[[0]*COLS for _ in range(ROWS)]
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
        a=judge.judge(grid)
        if a==1:
            print("black win")
            break
        elif a==2:
            print("white win")
            break 