from Physics import PhysicsEntity
import pygame
class Toy(PhysicsEntity):
    def __init__(self,x,y,w,h,mass):
        PhysicsEntity.__init__(self,x,y,mass)
        self.width=w
        self.height=h

    def draw(self,screen):
        pygame.draw.rect(screen, (255,255,255), [self.xpos, self.ypos, self.width, self.height])


