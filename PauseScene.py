import pygame


class PauseScene:
    def __init__(self, gameScene):
        self.next = self
        self.game = gameScene

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.next = self.game
                self.SwitchToScene(self.game)
                # bug: doesnt transfer released key events

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0,240,0))
        font = pygame.font.SysFont("arial", 72)
        text = font.render("Pause", True, (0, 0, 0))
        screen.blit(text, ((800 - text.get_width()) // 2, (600 - text.get_height()) // 2))
        font = pygame.font.SysFont("arial", 72)
        text = font.render("A Strange Charm", True, (0, 200, 0))
        screen.blit(text, (800 - text.get_width() , 600 - text.get_height()))

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
