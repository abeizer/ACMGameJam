from SceneBase import SceneBase
from PauseScene import PauseScene
from WinScene import WinScene
import Player, Particle, Goal, Wall, Door, pygame
import time

greenParticle = pygame.image.load("Images/particle_green.png")

class LevelThree(SceneBase):

    def __init__(self, player, clock):
        SceneBase.__init__(self)
        # creates the Player character in the location 20, 20
        self.player = player
        player.x = 30
        player.y = 30

        # Defines the starting positions of the first two Particles for level 3 of the game
        self.particle1 = Particle.Particle(90, 360, False, None, greenParticle, False)
        self.particle2 = Particle.Particle(90, 80, True, self.particle1, greenParticle, False)  # Particle 2 is entangled to Particle one

        # Defines the position for the first goal for level 3 of the game
        self.goal = Goal.Goal(720, 530)
        self.door = Door.Door(760, 100, 20, 100)
        # NOTE: Negative numbers in wall declarations ruin collision detection
        self.leftWall = Wall.Wall(0, 0, 20, 600)
        self.rightWall = Wall.Wall(780, 0, 20, 600)
        self.topWall = Wall.Wall(0, 0, 800, 20)
        self.bottomWall = Wall.Wall(0, 580, 800, 20)

        self.centerWallObstacle = Wall.Wall(20, 290, 780, 30)
        self.lowerWallObstacle = Wall.Wall(20, 390, 280, 20)
        self.middleWallObstacle = Wall.Wall(380, 300, 20, 180)
        self.rightWallObstacleOne = Wall.Wall(500, 450, 20, 130)
        self.rightWallObstacleTwo = Wall.Wall(580, 360, 200, 20)
        self.walls = [self.leftWall, self.rightWall, self.bottomWall, self.topWall, self.centerWallObstacle, self.lowerWallObstacle, self.middleWallObstacle, self.rightWallObstacleOne, self.rightWallObstacleTwo]

        # Defines the objects that the Player character cannot pass through
        self.entities = [self.player, self.particle1, self.particle2, self.leftWall, self.rightWall, self.topWall,
                         self.bottomWall, self.centerWallObstacle, self.lowerWallObstacle, self.middleWallObstacle, self.rightWallObstacleOne, self.rightWallObstacleTwo]
        self.particles = [self.particle1, self.particle2]
        self.startTime = clock
        #pygame.mixer.music.load('A Strange Charm.wav')
        #pygame.mixer.music.play(0)

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
        player = self.player
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
                    self.entities[e1].changeVelocity(-e1xv * .5, -e1yv * .5)
                    self.entities[e2].changeVelocity(e1xv * 2, e1yv * 2)
                    if (not self.entities[e2].movable):
                        self.entities[e1].changeVelocity(-xvel * 2, -yvel * 2)
                    elif (not self.entities[e1].movable):
                        self.entities[e2].changeVelocity(xvel * 2, yvel * 2)

                e2 += 1
        for wall in self.walls:
            if self.particle1.isColliding(wall.getCollider()):
                player.changeVelocity(-player.xVelocity * 2, -player.yVelocity * 2)
                player.move()
                self.particle2.changeVelocity(player.xVelocity * 2, player.yVelocity * 2)
                self.particle2.move()

        for entity in range(0, len(self.entities)):
            self.entities[entity].move()
        player.changeVelocity(playerxvel, playeryvel)
        for particle in self.particles:
            particle.changeVelocity(0, 0)
        if self.goal.isColliding(self.particle1.getCollider()):
            self.door.isOpen=True
        else:
            self.door.isOpen=False
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
        self.door.draw(screen)

        self.leftWall.draw(screen)
        self.rightWall.draw(screen)
        self.topWall.draw(screen)
        self.bottomWall.draw(screen)

        self.centerWallObstacle.draw(screen)
        self.lowerWallObstacle.draw(screen)
        self.middleWallObstacle.draw(screen)
        self.rightWallObstacleOne.draw(screen)
        self.rightWallObstacleTwo.draw(screen)
        font = pygame.font.SysFont("comicsansms", 48)
        text = font.render(str(int(time.time() - self.startTime)), True, (255, 255, 255))
        screen.blit(text, (700 - text.get_width() // 2, 50 - text.get_height() // 2))
