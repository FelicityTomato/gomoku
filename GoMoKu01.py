import pygame as pg
import judge
'''
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection

'''
FPS = 20
CELL_SIZE = 32
ROWS = 15
COLS = 15
MARGIN_LEFT = CELL_SIZE // 2
MARGIN_TOP =  CELL_SIZE // 2
GRID_WIDTH  = (COLS-1) * CELL_SIZE 
GRID_HEIGHT = (ROWS-1) * CELL_SIZE 
BG_COLOR = (150, 150, 150)      # Background-color
GRID_COLOR= (0, 0, 0)  #        # color of grid's line


#grid=[[0]*COLS for _ in range(ROWS)]

class Piece(pg.sprite.Sprite):
    
    def __init__(self, x, y, diamater, display):
        super().__init__() 
        radius = diamater // 2 
        self.x = x
        self.y = y
        left = MARGIN_LEFT + x * diamater
        top = MARGIN_TOP  + y * diamater
        self.images = [
              pg.Surface((diamater, diamater), pg.SRCALPHA) #self.grab(display, left, top, diamater)   
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
        ]

        self.images[0].blit(display, (0,0), (( left, top), ( left+diamater, top+diamater))) # Grab背景

        #pg.draw.circle(self.images[0], color,          (center_x, center_y), radius, 邊寬=0)      # example
        pg.draw.circle(self.images[1], (  0,   0,   0), (radius, radius), radius, 1) # with black width        
        pg.draw.circle(self.images[2], (255, 255, 255), (radius, radius), radius, 1) # with width

        pg.draw.circle(self.images[3], (  0,   0,   0), (radius, radius), radius) # Black filled
        pg.draw.circle(self.images[4], (255, 255, 255), (radius, radius), radius) # White filled
        
        self.imgIndex = 0
        self.image = self.images[self.imgIndex] 
        self.rect = self.image.get_rect(center = ( left + radius, top + radius))

    def update(self, event, type):
        #for event in event_list:
        #print(f" collidepoint(event.pos) = ({event.pos}) {self.rect.collidepoint(event.pos)}")
        if self.rect.collidepoint(event.pos):
            #print(f"Update type = {self.imgIndex}, {self.x}, {self.y}")
            self.image = self.images[type]
        else :
            self.image = self.images[0]


    def draw(self, display, type):
        self.image = self.images[type+2]
        display.blit(self.image, self.rect)

def draw_background(display):
    display.fill(BG_COLOR)
    SHIFT_L = MARGIN_LEFT +  CELL_SIZE // 2
    SHIFT_T = MARGIN_TOP +  CELL_SIZE // 2
    for x in range(COLS):
        pg.draw.line(display,GRID_COLOR , ( x * CELL_SIZE + SHIFT_L,                  SHIFT_T )
                                        , ( x * CELL_SIZE + SHIFT_L,    GRID_HEIGHT + SHIFT_T ))  # 直線
    for y in range(ROWS):
        pg.draw.line(display,GRID_COLOR , (                 SHIFT_L, y * CELL_SIZE  + SHIFT_T )
                                        , (    GRID_WIDTH + SHIFT_L, y * CELL_SIZE  + SHIFT_T ))  # 橫線
    pg.display.flip()

turn = 1
def play(event, CALLBACK_FUNC):
    global turn
    global run
    #event.pos = pg.mouse.get_pos()
    if event.type == pg.MOUSEMOTION:
        group.update(event, turn)
    elif event.type == pg.MOUSEBUTTONDOWN:
        
        (x, y) = event.pos
        gx = (x - MARGIN_LEFT) // CELL_SIZE
        gy = (y - MARGIN_TOP) // CELL_SIZE
        print(f"Update  =  ({x}, {y}) , grid({gx}, {gy}) index:{gy*COLS+gx}")
        if gx<0 or gy<0 or gx >= COLS or gy>=ROWS:
            return
        p = Pieces[gy*COLS+gx]
        if p != None:
            p.draw(display, turn)
            group.remove(p)
            Pieces[gy*COLS+gx] = None
            win = CALLBACK_FUNC( gx, gy, turn)
            run = False if win>0 else True 
            turn = turn ^ 3
    
def DoSomething(x, y, turn):
    print(f"DoSomething: ({x}, {y}, {turn})")
    judge.grid[x][y] = turn
    win = judge.judge()
    if win==1: print("black")
    elif win==2: print("white")
    return win


if __name__ == '__main__':
    
    # pygame initialize
    pg.init()

    # 建立 Display 即畫圖的視窗
    display = pg.display.set_mode((GRID_WIDTH + MARGIN_LEFT*2 + CELL_SIZE, GRID_HEIGHT + MARGIN_TOP*2+ CELL_SIZE))
    pg.display.set_caption('GoMoKu')
    draw_background(display)
    
    Pieces=[]
    for row in range(ROWS):
        for col in range(COLS):
            Pieces += [Piece( col, row, CELL_SIZE, display)]

    group = pg.sprite.Group(Pieces)

    FPS_CLOCK = pg.time.Clock()
    run = True
    while run:
        FPS_CLOCK.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            else:
                play(event, DoSomething)
        group.draw(display)
        pg.display.flip()


    pg.quit()
            