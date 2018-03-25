from SceneBase import SceneBase
from PauseScene import PauseScene
import Player, Particle, Goal, Wall, pygame


class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        # creates the Player character in the location 20, 20
        self.player = Player.Player(30, 30)

        # Defines the starting positions of the first two Particles for level 1 of the game
        self.particle1 = Particle.Particle(100, 100, False, None)
        self.particle2 = Particle.Particle(100, 200, True, self.particle1)  # Particle 2 is entangled to Particle one

        # Defines the position for the first goal for level 1 of the game
        self.goal = Goal.Goal(400, 400)

        # NOTE: Negative numbers in wall declarations ruin collision detection
        self.leftWall = Wall.Wall(0, 0, 20, 600)
        self.rightWall = Wall.Wall(780, 0, 20, 600)
        self.topWall = Wall.Wall(0, 0, 800, 20)
        self.bottomWall = Wall.Wall(0, 580, 800, 20)

        # Defines the objects that the Player character cannot pass through
        self.collidableObjects = [self.particle1, self.particle2, self.leftWall, self.rightWall, self.topWall, self.bottomWall]

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
        player.move()
        for object in self.collidableObjects:

            # If the collidable object is also movable, move the collidable object in the same direction
            # that the Player is moving
            if (player.isColliding(object.getCollider()) and object.movable):
                if player.up == True:
                    object.move(0, -player.speed)
                elif player.down == True:
                    object.move(0, player.speed)
                if player.left == True:
                    object.move(-player.speed, 0)
                elif player.right == True:
                    object.move(player.speed, 0)

            # If the collidable object is not movable, the player attempts to move, but the collidable
            # object will not move
            elif (player.isColliding(object.getCollider())):
                if player.up == True:
                    player.move(0, player.speed)
                elif player.down == True:
                    player.move(0, -player.speed)
                if player.left == True:
                    player.move(player.speed, 0)
                elif player.right == True:
                    player.move(-player.speed, 0)
            # end inner for loop
        # end outer for loop

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
