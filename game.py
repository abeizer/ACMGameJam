import pygame, Particle, Player, Goal, Wall, Direction, os,Door
#define colors vusing RGB values
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
blueParticle=pygame.image.load("Images/particle_blue.png")
redParticle=pygame.image.load("Images/particle_red.png")
playerimage=pygame.image.load("Images/player.png")
playerimage=pygame.transform.scale(playerimage,(30,30))
os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the application window in the middle of the screen on startup
pygame.init()

#initialize the screen to size 800 x 600
gameDisplay = pygame.display.set_mode((1000, 1000))

#creates the Player character in the location 20, 20
player = Player.Player(30, 30,playerimage)

#Defines the starting positions of the first two Particles for level 1 of the game
particle1 = Particle.Particle(100, 100, False, None,redParticle,False)
particle2 = Particle.Particle(100, 200, True, particle1,blueParticle,False) #Particle 2 is entangled to Particle one

#Defines the position for the first goal for level 1 of the game
goal = Goal.Goal(400, 400)
door=Door.Door(760,300,20,100)

#NOTE: Negative numbers in wall declarations ruin collision detection
leftWall = Wall.Wall(0, 0, 20, 600)
rightWall = Wall.Wall(780, 0, 20, 600)
topWall = Wall.Wall(0, 0, 800, 20)
bottomWall = Wall.Wall(0, 580, 800, 20)



#Defines the objects that the Player character cannot pass through

entities = [player,particle1, particle2, leftWall, rightWall, topWall, bottomWall]
particles=[particle1,particle2]
#rank by what you want to appear on what reversed
drawable=[goal,player,particle1,particle2,door,leftWall,rightWall,topWall,bottomWall]


gameExit = False
while not gameExit:
    gameDisplay.fill(BLACK) #The background color is black

    for event in pygame.event.get():    #returns true if a keypress occurs

        #Sets the condition for quitting the game (Clicking the x in top right corner of application)
        if event.type == pygame.QUIT:
            gameExit = True

        #Sets behaviors for when keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.down()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.right()

        #Sets behaviors for when keys are no longer pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.down()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.up()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.right()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.left()
    #end for loop

    playerxvel=player.xVelocity
    playeryvel=player.yVelocity
    #Behavior for when a player collides with a non-wall object
    for e1 in range(len(entities)):
        e2=e1+1
        while e2<len(entities):
            if(entities[e1].isColliding(entities[e2].getCollider())):
                e1xv=entities[e1].xVelocity
                e1yv=entities[e1].yVelocity
                e2xv = entities[e2].xVelocity
                e2yv = entities[e2].yVelocity
                xvel=e1xv+e2xv
                yvel=e1yv+e2yv
                entities[e1].changeVelocity(-xvel*2, -yvel*2)
                entities[e2].changeVelocity(xvel*2, yvel*2)
                if(not entities[e2].movable):
                    entities[e1].changeVelocity(-xvel * 50, -yvel * 50)
                elif(not entities[e1].movable):
                    entities[e2].changeVelocity(xvel * 50, yvel * 50)








            e2 += 1

    for entity in range(0,len(entities)):
        entities[entity].move()
    player.changeVelocity(playerxvel,playeryvel)
    for particle in particles:
        particle.changeVelocity(0,0)




    #When the goal and target Particle have collided, the player has passed the level
    #so display a win message
    if goal.isColliding(particle1.getCollider()) and player.isColliding(door.getCollider()):
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Win", True, (0, 128, 0))
        gameDisplay.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    #render any changes to the display
    for draw in drawable:
        draw.draw(gameDisplay)

    pygame.display.update()
#end while loop
pygame.quit()
quit()
