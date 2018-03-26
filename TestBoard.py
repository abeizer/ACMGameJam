import pygame, Particle, Player, Goal, Wall, Direction, os,Door,Toy,time




os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the application window in the middle of the screen on startup
pygame.init()

#initialize the screen to size 800 x 600
gameDisplay = pygame.display.set_mode((800, 600))

BLACK=(0,0,0)
toy=Toy.Toy(100,100,50,50,1)
toy.xvel=5
toy.friction=.2
drawable=[toy]
actors=[toy]
gameExit = False
while not gameExit:
    gameDisplay.fill(BLACK) #The background color is black
    for event in pygame.event.get():    #returns true if a keypress occurs

        #Sets the condition for quitting the game (Clicking the x in top right corner of application)
        if event.type == pygame.QUIT:
            gameExit = True
    for actor in actors:
        actor.act()
    for draw in drawable:
        draw.draw(gameDisplay)
    time.sleep(.01)

    pygame.display.update()
#end while loop
pygame.quit()
quit()