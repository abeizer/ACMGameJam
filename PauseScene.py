import pygame


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
