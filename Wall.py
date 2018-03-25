import pygame, Direction


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

        #foriegn object
        x2 = corners[0]
        y2 = corners[1]
        w2 = corners[2]
        h2 = corners[3]

        #Collision occuring on this object's left side
        if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):

            return Direction.LEFT

        #Collision occuring on this object's right side
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):

            return Direction.RIGHT

        #Collision occuring on this object's top side
        elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return Direction.TOP

        #Collision occuring on this object's bottom side
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return Direction.BOTTOM

        else:

            return Direction.NULL

    #Handles the behavior of objects colliding with the Wall
    def collide(self, entity, direction):
        #Stop the entity
        entity.changeVelocity(0, 0)

        #Bounce the entity off of the wall in the appropriate direction
        if(direction is Direction.LEFT):
            entity.changeVelocity(-.5, 0)
            entity.move()
        elif(direction is Direction.RIGHT):
            entity.changeVelocity(.5, 0)
            entity.move()
        elif(direction is Direction.TOP):
            entity.changeVelocity(0, -.5)
            entity.move()
        elif(direction is Direction.BOTTOM):
            entity.changeVelocity(0, .5)
            entity.move()


    #draws the goal at the specified position on the game display
    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, GREY, [self.xpos, self.ypos, self.width, self.height])
