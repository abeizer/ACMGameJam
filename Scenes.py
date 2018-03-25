from SceneBase import SceneBase
from GameScene import GameScene
import pygame, os
from LevelTwo import LevelTwo

#define colors using RGB values
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)

os.environ['SDL_VIDEO_CENTERED'] = '1'




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
                self.SwitchToScene(LevelTwo())

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("arial", 72)
        text = font.render("A Strange Charm", True, (0, 128, 0))
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
        text2 = font.render("Press Enter", True, (20, 20, 20))
        screen.blit(text2, (800 - text2.get_width() - 5, 600 - text2.get_height()))

run_game(800, 600, 60, TitleScene())

