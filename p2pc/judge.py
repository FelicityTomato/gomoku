
ROWS = 15
COLS = 15



def judge(grid): # 0:draw 1:black 2:white 
    p = (1,0,0,1,1,1,1,-1)
    for i in range(ROWS):
        for j in range(COLS):
            for t in range(4):
                for k in range(5):
                    if grid[i][j]!=0 \
                        and i+k*p[t*2]<ROWS and i+k*p[t*2]>=0 and j+k*p[t*2+1]<COLS and j+k*p[t*2+1]>=0 \
                        and grid[i+k*p[t*2]][j+k*p[t*2+1]]==grid[i][j]:
                        if k==4:
                            return grid[i][j]
                    else:
                        break
            '''
            # 橫的
            #print(1)
            for k in range(5):
                if grid[i][j]!=0 and j+k<COLS and grid[i][j+k]==grid[i][j]:
                    if k==4:
                        return grid[i][j]
                else:
                    break
            # 直的
            #print(2)
            for k in range(5):
                if grid[i][j]!=0 and i+k<ROWS and grid[i+k][j]==grid[i][j]:
                    if k==4:
                        return grid[i][j]
                else:
                    break
            # 斜的
            #print(3)
            for k in range(5):
                if grid[i][j]!=0 and i+k<ROWS and j+k<COLS and grid[i+k][j+k]==grid[i][j]:
                    #print(i,j,k)
                    if k==4:
                        return grid[i][j]
                else:
                    break
            #print(4)
            for k in range(5):
                if grid[i][j]!=0 and i+k<ROWS and j-k>=0 and grid[i+k][j-k]==grid[i][j]:
                    if k==4:
                        return grid[i][j]
                else:
                    break
        '''
    return 0

def pr(grid):
    for i in range(ROWS):
        for j in range(COLS):
            print(grid[i][j], end=' ')
        print(end='\n')

if __name__ == '__main__':
    grid=[[0]*COLS for _ in range(ROWS)]
    b=0
    pr()
    while True:
        r=int(input("your row: "))
        c=int(input("your column: "))
        if grid[r][c]==0:
            grid[r][c]=(b%2+1)
        else:
            print("input again ")
            continue
        a=judge(grid)
        pr(grid)
        if a==1:
            print("black win")
            break
        elif a==2:
            print("white win")
            break
        b+=1
    