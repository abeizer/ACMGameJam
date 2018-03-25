from SceneBase import SceneBase
import pygame


class WinScene(SceneBase):
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("arial", 72)
        text = font.render("Win", True, (0, 128, 0))
        screen.blit(text, ((800 - text.get_width()) // 2, (600 - text.get_height()) // 2))

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)