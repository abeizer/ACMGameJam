from SceneBase import SceneBase
from PauseScene import PauseScene
from WinScene import WinScene
import Player, Particle, Goal, Wall, pygame,Door
blueParticle=pygame.image.load("Images/particle_blue.png")
redParticle=pygame.image.load("Images/particle_red.png")
playerimage=pygame.image.load("Images/player.png")
playerimage=pygame.transform.scale(playerimage,(30,30))

class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        # creates the Player character in the location 20, 20
        self.player = Player.Player(30, 30,playerimage)

        # Defines the starting positions of the first two Particles for level 1 of the game
        self.particle1 = Particle.Particle(100, 100, False, None,redParticle,False)
        self.particle2 = Particle.Particle(100, 200, True, self.particle1,blueParticle,False)  # Particle 2 is entangled to Particle one

        # Defines the position for the first goal for level 1 of the game
        self.goal = Goal.Goal(400, 400)

        # NOTE: Negative numbers in wall declarations ruin collision detection
        self.leftWall = Wall.Wall(0, 0, 20, 600)
        self.rightWall = Wall.Wall(780, 0, 20, 600)
        self.topWall = Wall.Wall(0, 0, 800, 20)
        self.bottomWall = Wall.Wall(0, 580, 800, 20)
        self.door = Door.Door(760, 300, 20, 100)

        # Defines the objects that the Player character cannot pass through
        self.entities = [self.player,self.particle1, self.particle2, self.leftWall, self.rightWall, self.topWall, self.bottomWall]
        self.particles=[self.particle1,self.particle2]

        pygame.mixer.music.load('A Strange Charm.wav')
        pygame.mixer.music.play(0)

    def ProcessInput(self, events, pressed_keys):
        player = self.player
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.down()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.down()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.up()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.right()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.left()


            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # pause when the user pressed escape
                self.SwitchToScene(PauseScene(self))

    def Update(self):
        player=self.player
        playerxvel = player.xVelocity
        playeryvel = player.yVelocity
        # Behavior for when a player collides with a non-wall object
        for e1 in range(len(self.entities)):
            e2 = e1 + 1
            while e2 < len(self.entities):
                if (self.entities[e1].isColliding(self.entities[e2].getCollider())):
                    e1xv = self.entities[e1].xVelocity
                    e1yv = self.entities[e1].yVelocity
                    e2xv = self.entities[e2].xVelocity
                    e2yv = self.entities[e2].yVelocity
                    xvel = e1xv + e2xv
                    yvel = e1yv + e2yv
                    self.entities[e1].changeVelocity(-xvel * 2, -yvel * 2)
                    self.entities[e2].changeVelocity(xvel * 2, yvel * 2)
                    if (not self.entities[e2].movable):
                        self.entities[e1].changeVelocity(-xvel * 2, -yvel * 2)
                    elif (not self.entities[e1].movable):
                        self.entities[e2].changeVelocity(xvel * 2, yvel * 2)

                e2 += 1

        for entity in range(0, len(self.entities)):
            self.entities[entity].move()
        player.changeVelocity(playerxvel, playeryvel)
        for particle in self.particles:
            particle.changeVelocity(0, 0)

        # When the goal and target Particle have collided, the player has passed the level
        # so display a win message
        if self.goal.isColliding(self.particle1.getCollider()) and player.isColliding(self.door.getCollider()):
            self.SwitchToScene(WinScene())
            
        


    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        self.goal.draw(screen)
        self.player.draw(screen)
        self.particle1.draw(screen)
        self.particle2.draw(screen)

        self.leftWall.draw(screen)
        self.rightWall.draw(screen)
        self.topWall.draw(screen)
        self.bottomWall.draw(screen)
        self.door.draw(screen)
