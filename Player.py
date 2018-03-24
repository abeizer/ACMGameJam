import pygame
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
class Player():
    def __init__(self,x,y):
        self.speed = .5
        self.thickness = 10
        self.up = False
        self.down = False
        self.left=False
        self.right=False
        self.x=x
        self.y=y
        self.width=20
        self.height=20
        self.gain=10
    def draw(self,gameDisplay):
        pygame.draw.rect(gameDisplay, WHITE, [self.x, self.y, self.width, self.height])
    def move(self, xmove,ymove):
        self.y+=ymove
        self.x+=xmove

    def isColliding(self,corners):
        x1=self.x
        y1=self.y
        w1=self.width
        h1=self.height
        x2=corners[0]
        y2=corners[1]
        w2=corners[2]
        h2=corners[3]
        if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        else:

            return False

