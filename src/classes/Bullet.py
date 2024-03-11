import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, screen_width):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()
