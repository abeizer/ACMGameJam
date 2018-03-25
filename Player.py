import pygame

#define colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class Player():

    # defines the starting position and size of the Player character
    def __init__(self, x, y):
        self.speed = .5
        self.xVelocity = 0
        self.yVelocity = 0
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    # draws the player character at its current position using
    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, WHITE, [self.x, self.y, self.width, self.height])

    #Moves the player based on its velocity
    def move(self):
        self.y += self.yVelocity
        self.x += self.xVelocity

    #Straight up just changes the velocity
    def changeVelocity(self, xV, yV):
        self.xVelocity = xV
        self.yVelocity = yV

    #This set of methods changes the Player velocity to move in a direction
    def up(self):
        self.changeVelocity(self.xVelocity, self.yVelocity - self.speed)

    def down(self):
        self.changeVelocity(self.xVelocity, self.yVelocity + self.speed)

    def right(self):
        self.changeVelocity(self.xVelocity + self.speed, self.yVelocity)

    def left(self):
        self.changeVelocity(self.xVelocity - self.speed, self.yVelocity)

    def stop_x_movement(self):
        self.changeVelocity(0, self.yVelocity)

    def stop_y_movement(self):
        self.changeVelocity(self.xVelocity, 0)

    # TODO: Please explain
    def isColliding(self, corners):
        x1 = self.x
        y1 = self.y
        w1 = self.width
        h1 = self.height
        x2 = corners[0]
        y2 = corners[1]
        w2 = corners[2]
        h2 = corners[3]
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

    def getCollider(self):
        return (self.x, self.y, self.width, self.height)


