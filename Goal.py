#The goal is where the player must direct the main particle to in order to win the level

import pygame
GREEN = (  0, 255,   0)


class Goal:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = 20

    ##returns the two corners of the collider box
    def getCollider(self):
        return (self.xpos-self.radius/2,self.ypos-self.radius/2,self.radius,self.radius)

    #TODO: explain please
    def isColliding(self, corners):
        x1 = self.xpos
        y1 = self.ypos
        w1 = self.radius
        h1 = self.radius
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

    #sraws the goal at the specified position on the game display
    def draw(self, gameDisplay):
        pygame.draw.circle(gameDisplay, GREEN, (int(self.xpos), int(self.ypos)), self.radius)