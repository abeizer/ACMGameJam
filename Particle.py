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
    def __init__(self, xpos, ypos, movable, partner):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = 20
        self.movable = movable
        self.partner = partner
        self.yVelocity = 0
        self.xVelocity = 0

    #attempts to move the Particle
    #also moves the partnered Particle if one exists
    #NOTE: Assumes a one-way partnership. Two-way partnerships will cause an infinite loop
    def move(self):
        self.xpos += self.xVelocity
        self.ypos += self.yVelocity
        if self.partner:
            self.partner.changeVelocity(self.xVelocity, self.yVelocity)
            self.partner.move()

    #Straight up just changes the velocity
    def changeVelocity(self, xV, yV):
        self.xVelocity = xV
        self.yVelocity = yV


    #If the Particle is movable, redraws the Particle at its current location after it has moved
    def draw(self, gameDisplay):
        if(self.movable):
            pygame.draw.circle(gameDisplay, BLUE, (int(self.xpos), int(self.ypos)), self.radius)
        else:
            pygame.draw.circle(gameDisplay, RED, (int(self.xpos), int(self.ypos)), self.radius)

    ##returns the two corners of the collider box
    def getCollider(self):
        return (self.xpos-self.radius, self.ypos-self.radius, self.radius*2, self.radius*2)

    #sets the partner Particle for this Particle
    def setPartner(self, partner):
        self.partner = partner