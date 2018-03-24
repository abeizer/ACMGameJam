import pygame
import Player

global gameScene

class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                #if event.key == pygame.K_ESCAPE:
                #    quit_attempt = True
                if event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    def Update(self):
        pass

    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))


class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.player = Player.Player(20, 20)

    def ProcessInput(self, events, pressed_keys):
        player = self.player
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.up = True
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.down = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.left = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.up = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.left = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.right = False


            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # pause when the user pressed escape
                self.SwitchToScene(PauseScene(self))

    def Update(self):
        player = self.player
        if player.up == True:
            player.move(0, -player.speed)
        elif player.down == True:
            player.move(0, player.speed)
        if player.left == True:
            player.move(-player.speed, 0)
        elif player.right == True:
            player.move(player.speed, 0)

    def Render(self, screen):
        player = self.player
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
        player.draw(screen)

class PauseScene:
    def __init__(self, gameScene):
        self.next = self
        self.game = gameScene

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.game.next = self.game
                self.SwitchToScene(self.game)
                # bug: doesnt transfer released key events

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0,255,0))

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

run_game(400, 300, 60, TitleScene())

