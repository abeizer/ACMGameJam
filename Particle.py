#Particles are movable by the player and must be directed to a goal
#Some particles are tied to others so that when one Particle is acted upon, another may be affected

import pygame

#define colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Particle:
    #creates a Particle at the given coordinates and whether it is movable
    #and ties it to a partner Particle if one exists
    def __init__(self, xpos, ypos, movable, partner,img,isReversed):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = 20
        self.movable = movable
        self.partner = partner
        self.yVelocity = 0
        self.xVelocity = 0
        self.img=img
        self.isReversed=isReversed

    #attempts to move the Particle
    #also moves the partnered Particle if one exists
    #NOTE: Assumes a one-way partnership. Two-way partnerships will cause an infinite loop
    def move(self):
        if self.movable:
            self.xpos += self.xVelocity
            self.ypos += self.yVelocity
            if self.partner:
                self.partner.changeVelocity(self.xVelocity, self.yVelocity)
                self.partner.forceMove()
    def forceMove(self):
        if self.isReversed:
            self.xpos -= self.xVelocity
            self.ypos -= self.yVelocity
        else:
            self.xpos += self.xVelocity
            self.ypos += self.yVelocity

    #Straight up just changes the velocity
    def changeVelocity(self, xV, yV):
        self.xVelocity = xV
        self.yVelocity = yV


    #If the Particle is movable, redraws the Particle at its current location after it has moved
    def draw(self, gameDisplay):
        gameDisplay.blit(self.img,(int(self.xpos-self.radius),int(self.ypos-self.radius)))

    ##returns the two corners of the collider box
    def getCollider(self):
        return (self.xpos - self.radius, self.ypos - self.radius, self.radius*2, self.radius*2)

    #sets the partner Particle for this Particle
    def setPartner(self, partner):
        self.partner = partner
    def isColliding(self, corners):
        x1 = self.xpos
        y1 = self.ypos
        w1 = self.radius
        h1 = self.radius

        #foriegn object
        x2 = corners[0]
        y2 = corners[1]
        w2 = corners[2]
        h2 = corners[3]

        #Collision occuring on this object's left side
        if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        #Collision occuring on this object's right side
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):

            return True

        #Collision occuring on this object's top side
        elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        #Collision occuring on this object's bottom side
        elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

            return True

        else:

            return False