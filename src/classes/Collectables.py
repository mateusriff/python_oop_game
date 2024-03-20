import pygame


class Collectable(pygame.sprite.Sprite):
    def __init__(self, x, y, power):
        pygame.sprite.Sprite.__init__(self)

        color = (0, 0, 0)
        if power == 'bullet_speed':
            color = (255, 0, 255)
        if power == 'shoot_cooldown':
            color = (0, 255, 255)
        if power == 'player_speed':
            color = (255, 255, 0)

        self.image = pygame.Surface([25, 25])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.power = power