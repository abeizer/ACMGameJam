import pygame, Particle, Player,Goal
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
pygame.init()
gameDisplay=pygame.display.set_mode((800, 600))
player=Player.Player(20,20)
particle1=Particle.Particle(100,100,False,None)
particle2=Particle.Particle(100,200,True,particle1)
goal=Goal.Goal(400,400)
collidableObjects=[particle1,particle2]
gameExit=False
while not gameExit:
    gameDisplay.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.up = True
            elif event.key == pygame.K_s:
                player.down = True
            if event.key == pygame.K_a:
                player.left = True
            elif event.key == pygame.K_d:
                player.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.up = False
            elif event.key == pygame.K_s:
                player.down = False
            if event.key == pygame.K_a:
                player.left = False
            elif event.key == pygame.K_d:
                player.right = False
    if player.up == True:
        player.move(0,-player.speed)
    elif player.down == True:
        player.move(0,player.speed)
    if player.left == True:
        player.move(-player.speed,0)
    elif player.right == True:
        player.move(player.speed,0)
    for object in collidableObjects:
        if(player.isColliding(object.getCollider()) and object.movable):
            if player.up == True:
                object.move(0, -player.speed)
            elif player.down == True:
                object.move(0, player.speed)
            if player.left == True:
                object.move(-player.speed, 0)
            elif player.right == True:
                object.move(player.speed, 0)
        elif(player.isColliding(object.getCollider())):
            if player.up == True:
                player.move(0, player.speed)
            elif player.down == True:
                player.move(0, -player.speed)
            if player.left == True:
                player.move(player.speed, 0)
            elif player.right == True:
                player.move(-player.speed, 0)
    if goal.isColliding(particle1.getCollider()):
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Win", True, (0, 128, 0))
        gameDisplay.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    goal.draw(gameDisplay)
    player.draw(gameDisplay)
    particle1.draw(gameDisplay)
    particle2.draw(gameDisplay)


    pygame.display.update()

pygame.quit()
quit()