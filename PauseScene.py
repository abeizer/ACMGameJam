import pygame
import GameScene

class PauseScene:
    def __init__(self, gameScene):
        self.next = self
        self.game = gameScene


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                self.game.next = self.game
                self.SwitchToScene(self.game)
                # bug: doesnt transfer released key events

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 240, 0))
        font = pygame.font.SysFont("arial", 72)
        text = font.render("Pause", True, (0, 0, 0))
        screen.blit(text, ((800 - text.get_width()) // 2, (600 - text.get_height()) // 2))

        text = font.render("A Strange Charm", True, (0, 200, 0))
        screen.blit(text, (800 - text.get_width(), 600 - text.get_height()))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        buttonX = 50
        buttonY = 450
        buttonFont = pygame.font.SysFont("arial", 36)
        buttonText = buttonFont.render("Restart", True, (0, 0, 0))
        if buttonX + buttonText.get_width() + 7 > mouse[0] > buttonX - 7 and buttonY + buttonText.get_height() + 7 > mouse[1] > buttonY - 7:
            pygame.draw.rect(screen, (30, 30, 30),
                             (buttonX - 7, buttonY - 7, buttonText.get_width() + 14, buttonText.get_height() + 14))
            buttonX = buttonX - 3
            buttonY = buttonY - 3
            pygame.draw.rect(screen, (0, 0, 0),
                             (buttonX - 7, buttonY - 7, buttonText.get_width() + 14, buttonText.get_height() + 14))
            pygame.draw.rect(screen, (0, 180, 0),
                             (buttonX - 5, buttonY - 5, buttonText.get_width() + 10, buttonText.get_height() + 10))
            screen.blit(buttonText, (buttonX, buttonY))
            if click[0] == 1:
                from GameScene import GameScene
                self.SwitchToScene(GameScene())
        else:
            pygame.draw.rect(screen, (0, 0, 0),
                             (buttonX - 7, buttonY - 7, buttonText.get_width() + 14, buttonText.get_height() + 14))
            pygame.draw.rect(screen, (0, 180, 0),
                             (buttonX - 5, buttonY - 5, buttonText.get_width() + 10, buttonText.get_height() + 10))
            screen.blit(buttonText, (buttonX, buttonY))



    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
