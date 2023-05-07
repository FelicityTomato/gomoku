from Evaluation import evaluation

def pc_turn( gomoku, ROWS, COLS):
    _, x, y = dfs(gomoku, gomoku.EvaSet, 2, -1e9, 1e9, ROWS, COLS, gomoku.turn)
    print (f'Move {x},{y}')
    gomoku.play(x, y)
    '''
    max_score, x, y = -1, -1, -1
    for (i,j) in gomoku.EvaSet:
        if gomoku.grid[i][j]==0:
            gomoku.grid[i][j]=gomoku.turn
            S = set()
            for (dx, dy) in gomoku.rounddir:
                xx = i+dx
                yy = j+dy
                if  xx< 0 or xx >= COLS or yy < 0 or yy >=ROWS:
                    continue
                if gomoku.grid[xx][yy] == 0:
                    S.add((xx, yy))
            score = minimax(gomoku, gomoku.EvaSet.union(S), 2, ROWS, COLS, 3-gomoku.turn, xx, yy)
            gomoku.grid[i][j] = 0
            if score > max_score:
                max_score = score
                x, y= i, j
    gomoku.play(x, y)
    '''

def minimax(gomoku, EvaSet, depth,  ROWS, COLS, turn, x, y):
    if depth == 0:
        w = gomoku.judge(x, y, turn)
        return w if w>=0 else -w

    grid = gomoku.grid
    alpha = -1e9
    for (i,j) in EvaSet:
        if grid[i][j]==0:
                grid[i][j]=turn
                S = set()
                for (dx, dy) in gomoku.rounddir:
                    xx = i+dx
                    yy = j+dy
                    if  xx< 0 or xx >= COLS or yy < 0 or yy >=ROWS:
                        continue
                    if gomoku.grid[xx][yy] == 0:
                        S.add((xx, yy))
                alpha = max(alpha, -minimax(gomoku, EvaSet.union(S), depth-1, ROWS, COLS, 3-turn, x, y))
                grid[i][j]=0

    return alpha

def dfs(gomoku, EvaSet, depth, alpha, beta, ROWS, COLS, turn):
    grid = gomoku.grid
    
    if depth == 0:
        return evaluation(gomoku, EvaSet, ROWS, COLS, turn)

    if turn==2:
        mx,x,y= evaluation(gomoku, EvaSet, ROWS, COLS, turn)  
        #x,y = -1, -1 
        for (i,j) in EvaSet:
            if grid[i][j]==0:
                grid[i][j]=turn
                S = set()
                for (dx, dy) in gomoku.rounddir:
                    xx = i+dx
                    yy = j+dy
                    if  xx< 0 or xx >= COLS or yy < 0 or yy >=ROWS:
                        continue
                    if gomoku.grid[xx][yy] == 0:
                        S.add((xx, yy))
                score,a,b = dfs(gomoku, EvaSet.union(S), depth-1, alpha,beta, ROWS, COLS, 3-turn)
                score /= 2
                grid[i][j]=0
                
                if score>mx:
                    mx=score
                    x,y=i,j
                '''
                alpha=max(alpha,score)
                if beta<=alpha: 
                    return (mx,x,y)
                    break
                '''
        return (mx,x,y)
    else:
        mn, x,y = evaluation(gomoku, EvaSet, ROWS, COLS, turn)   #???
        #x,y = -1, -1 
        for (i,j) in gomoku.EvaSet:
            if grid[i][j]==0:
                grid[i][j]=turn
                S = set()
                for (dx, dy) in gomoku.rounddir:
                    xx = i+dx
                    yy = j+dy
                    if  xx< 0 or xx >= COLS or yy < 0 or yy >=ROWS:
                        continue
                    if gomoku.grid[xx][yy] == 0:
                        S.add((xx, yy))
                score, _, _=dfs(gomoku, EvaSet.union(S), depth-1, alpha, beta, ROWS, COLS, 3-turn)
                score /= 2
                grid[i][j]=0
                if score<mn:
                    mn=score
                    x,y=i,j
                grid[i][j]=0
                '''
                beta=min(beta,score)
                if beta<=alpha: 
                    return (mn,x,y)
                    break
                '''
        return (mn,x,y)
        

