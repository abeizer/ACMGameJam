from ACMGameJam.Entity import Entity


class PhysicsEntity(Entity):

    def __init__(self,x,y,mass):
        Entity.__init__(self,x,y)
        self.xvel=0
        self.yvel=0
        self.xacc=0
        self.yacc=0
        self.mass=mass
        self.friction=0

    def act(self):
        self.xpos+=self.xvel
        self.ypos+=self.yvel
        self.xvel+=self.xacc
        self.yvel+=self.yacc

        if self.yvel>0:
            self.yvel-=self.friction
        elif self.yvel<0:
            self.yvel+=self.friction
        if self.xvel>0:
            self.xvel-=self.friction
        elif self.xvel<0:
            self.xvel+=self.friction



        if self.yacc>0:
            self.yacc-=self.friction
        elif self.yacc<0:
            self.yacc+=self.friction
        if self.xacc>0:
            self.xacc-=self.friction
        elif self.xacc<0:
            self.xacc+=self.friction
        if abs(self.xvel)<.00001:
            self.xvel=0
        if abs(self.yvel)<.00001:
            self.yvel=0
        if abs(self.xacc)<.00001:
            self.xacc=0
        if abs(self.yacc)<.00001:
            self.yacc=0





