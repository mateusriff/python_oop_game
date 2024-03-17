import pygame
from .Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, color, side):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([50 * scale, 50 * scale])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 5
        self.alive = True

        self.key_up = pygame.K_w if side == 'left' else pygame.K_UP
        self.key_down = pygame.K_s if side == 'left' else pygame.K_DOWN
        self.key_shoot = pygame.K_d if side == 'left' else pygame.K_LEFT

        self.direction = 1 if side == 'left' else -1

        self.shoot_cooldown = 0
        self.bullet_speed = 10

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        keys = pygame.key.get_pressed()
        if keys[self.key_up] and self.rect.y > 50:
            self.rect.y -= self.speed
        elif keys[self.key_down] and self.rect.y < 718:
            self.rect.y += self.speed

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 30  # half a second at 60 ticks

            bullet_distance = self.rect.size[0] * 0.5 * self.direction

            bullet = Bullet(self.rect.centerx + bullet_distance, self.rect.centery, self.direction, self.bullet_speed)
            return bullet

    def power_up(self, power):
        if power == 'bullet_speed':
            self.bullet_speed += 2
        elif power == 'shoot_cooldown':
            if self.shoot_cooldown > 10:
                self.shoot_cooldown -= 2
        if power == 'player_speed':
            self.speed += 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def kill_player(self):
        self.alive = False
        self.kill()