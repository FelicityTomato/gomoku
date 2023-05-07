def pc_turn( gomoku, ROWS, COLS):
    _, x, y = evaluation(gomoku, gomoku.EvaSet, ROWS, COLS, gomoku.turn)
    gomoku.play(x, y)


def evaluation(gomoku, EvaSet, ROWS, COLS, turn):
    ret = (0, ROWS//2, COLS//2)
    for (x, y) in EvaSet:
        score = getScore(gomoku, x, y, ROWS, COLS, turn, True)            # Offence        
        score += getScore(gomoku, x, y, ROWS, COLS, 3-turn, False)  # Defence
        if score >= ret[0]:
            ret =  (score,  x, y)
    return ret  # (socre, X, Y)


def getScore(gomoku, x, y, ROWS, COLS, turn, isOffence=True):
    #          -  1   2    3    4    5     6     7    8    
    offence = (0, 2,  4,  16, 64,  256, 256, 256, 256, 256)
    defence = (0, 2,  8,  32, 128,  512, 512, 512, 512, 512)
    #defence = (0, 1, 10,   30, 200,  40000,  40000,  40000,  40000)

    scorelist= offence if isOffence else defence
    score = 0
    
    for dx, dy in ((1,0), (0,1), (1,1), (1, -1)):
        scoreIdx = 1
        for k in range(-1,-6, -1):
            gx = x+ k*dx; gy = y+ k*dy     # 往前
            if gx >= 0 and gx < ROWS and gy >= 0 and gy < COLS :
                if gomoku.grid[gx][gy] == turn:
                    scoreIdx+=1
                else:
                    break
        for k in range(1,6):
            gx = x+ k*dx; gy = y+k*dy     # 往後
            if gx >= 0 and gx < ROWS and gy >= 0 and gy < COLS :
                if gomoku.grid[gx][gy] == turn:
                    scoreIdx+=1
                else:
                    break
        scoreIdx = 5 if scoreIdx > 5 else scoreIdx
        score += scorelist[scoreIdx]
    return score

