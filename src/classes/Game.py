import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Wild Wild West')

    @staticmethod
    def should_quit():
        quit_flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_flag = True
        return quit_flag

    def render(self):
        self.screen.fill((25, 0, 50))

    @staticmethod
    def update():
        pygame.display.flip()
