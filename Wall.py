import pygame

GREY = (69, 69, 69)

class Wall:
    def __init__(self, xpos, ypos, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.movable = False



    def getCollider(self):
        return (self.xpos, self.ypos, self.width, self.height)

    # TODO: explain please
    def isColliding(self, corners):
        x1 = self.xpos
        y1 = self.ypos
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

    # draws the goal at the specified position on the game display
    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, GREY, [self.xpos, self.ypos, self.width, self.height])