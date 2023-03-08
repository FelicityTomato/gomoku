import pygame as pg

class Piece(pg.sprite.Sprite):

    def __init__(self, x, y, top, left, diamater, display):
        super().__init__() 
        radius = diamater // 2 
        margin = radius // 5
        #self.x = x
        #self.y = y
        #self.left = left
        #self.top = top
        self.images = [
              pg.Surface((diamater, diamater), pg.SRCALPHA) #self.grab(display, left, top, diamater)   
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
            , pg.Surface((diamater, diamater), pg.SRCALPHA)
        ]

        self.images[0].blit(display, (0,0), (( left, top), ( left+diamater, top+diamater))) # Grab背景

        #pg.draw.circle(self.images[0], color,          (center_x, center_y), radius, 邊寬=0)      # example
        pg.draw.circle(self.images[1], (  0,   0,   0), (radius, radius), radius-margin, 1) # with black width        
        pg.draw.circle(self.images[2], (255, 255, 255), (radius, radius), radius-margin, 1) # with width

        pg.draw.circle(self.images[3], (  0,   0,   0), (radius, radius), radius-margin) # Black filled
        pg.draw.circle(self.images[4], (255, 255, 255), (radius, radius), radius-margin) # White filled
        
        self.imgIndex = 0
        self.image = self.images[self.imgIndex] 
        self.rect = self.image.get_rect(center = ( left + radius, top + radius))

    def update(self, event, type):
        #print(f" collidepoint(event.pos) = ({event.pos}) {self.rect.collidepoint(event.pos)}")
        if self.rect.collidepoint(event.pos):
            #print(f"Update type = {self.imgIndex}, {self.x}, {self.y}")
            self.image = self.images[type]
        else :
            self.image = self.images[0]     

    def draw(self, display, type):
        self.image = self.images[type+2]
        display.blit(self.image, self.rect)
        del self

