import pygame as pg
from gomokuPiece import Piece
'''
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection

Step04: 改坐標系，並將piece獨立為class

'''

FPS = 20
CELL_SIZE = 32
ROWS = 15
COLS = 15
MARGIN_LEFT = CELL_SIZE // 2
MARGIN_TOP =  CELL_SIZE // 2
MARGIN_BOTTOM = 42
GRID_WIDTH  = (COLS-1) * CELL_SIZE 
GRID_HEIGHT = (ROWS-1) * CELL_SIZE 
BG_COLOR = (150, 150, 150)      # Background-color
GRID_COLOR= (0, 0, 0)  #        # color of grid's line
FONT_SIZE=MARGIN_BOTTOM -10


class gomokuBoard():
    def __init__(self, title, pg):
        # 建立 Display 即畫圖的視窗
        self.display = pg.display.set_mode((GRID_WIDTH + MARGIN_LEFT*2 + CELL_SIZE, GRID_HEIGHT + MARGIN_TOP + MARGIN_BOTTOM + CELL_SIZE))

        pg.display.set_caption(title)
        self.draw_background(self.display)
        
        self. base_font = pg.font.Font(None, FONT_SIZE)
        self.msg_rect = pg.Rect(MARGIN_LEFT//2, GRID_HEIGHT + MARGIN_TOP + CELL_SIZE + 10, GRID_WIDTH, FONT_SIZE)
        
        self.Pieces=[]
        #group = pg.sprite.Group()
        for col in range(COLS):
            for row in range(ROWS):
                self.Pieces += [Piece( row, col, MARGIN_TOP + row * CELL_SIZE, MARGIN_LEFT + col * CELL_SIZE, CELL_SIZE, self.display)]
                #group.add(Piece( col, row, CELL_SIZE, display))

        self.group = pg.sprite.Group(self.Pieces)    
        self.FPS_CLOCK = pg.time.Clock()
        self.turn = 1
        self.grid = [ [0]*COLS for _ in range(ROWS)]
        self.RUN = True

    def run(self):
        while True:
            self.FPS_CLOCK.tick(FPS)
            if not self.RUN:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return
                continue
            
            if self.turn == 1:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return
                    else:
                        self.human_turn(event)
            else:
                self.pc_turn()
    
            self.group.draw(self.display)
            pg.display.flip()

    def pc_turn(self):
        self.play(2,2)

    def draw_background(self, display):
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

    def human_turn(self, event):
        #event.pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEMOTION:
            self.group.update(event, self.turn)
        elif event.type == pg.MOUSEBUTTONDOWN:
            
            (x, y) = event.pos 
            gx = (y - MARGIN_LEFT) // CELL_SIZE # 因為 Screen 座標: X 是水平。但此處我定義 X 是 row
            gy = (x - MARGIN_TOP) // CELL_SIZE
            print(f"Update  =  ({x}, {y}) , grid({gx}, {gy})")    
            if gx<0 or gy<0 or gx >= ROWS or gy>=COLS:
                return
            self.play(gx, gy) 

    def play(self, gx, gy):
        idx = gy * ROWS + gx
        p = self.Pieces[idx]
        self.grid[gx][gy]= self.turn
        if p != None:
            p.draw(self.display, self.turn)
            self.group.remove(p)
            self.Pieces[idx] = None
            w = self.judge(gx,gy, self.turn)
            if w != 0 :
                self.RUN = False  
            self.turn = self.turn ^ 3
                

    def judge(self, x, y, turn):
        pass
        '''
        msg =f"DoSomething: ({x}, {y}), turn={turn}"
        self.message(msg)
        print(msg)
        '''
        
    def message (self, msg):
        if msg != "": msg_surface = self.base_font.render("", True, (0, 0, 0))  # Clean text Area

        pg.draw.rect(self.display, BG_COLOR, self.msg_rect)
        msg_surface = self.base_font.render(msg, True, (0, 0, 0))
        self.display.blit(msg_surface, (self.msg_rect.x+5, self.msg_rect.y+5))

if __name__ == '__main__':

    class game(gomokuBoard):
        '''
        def __init__(self, title, pg):
            super().__init()
        '''
    
        def judge(self, x, y, turn):
            msg =f"DoSomething: ({x}, {y}), turn={turn}"
            self.message(msg)
            print(msg)
            
    # pygame initialize
    pg.init()
    game = gomokuBoard('GoMoKu', pg)
    game.run()

    pg.quit()
            
