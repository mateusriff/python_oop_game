import pygame
from classes import Game

clock = pygame.time.Clock()


def main():
    game = Game()

    while True:  # main game loop
        global clock
        clock.tick(60)

        if game.should_quit():
            pygame.quit()
            break

        game.render()
        
        game.update()


if __name__ == "__main__":
    main()
