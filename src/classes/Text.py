import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, text, font, size, x, y):
        super().__init__()
        self.text = text
        self.font = pygame.font.Font(font, size)
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_text(self, new_text):
        self.text = new_text
        self.image = self.font.render(self.text, True, (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class FadingText(Text):
    def __init__(self, text, font, size, x, y, fade_speed=2):
        super().__init__(text, font, size, x, y)
        self.fade_speed = fade_speed
        self.alpha = 255  # 255 = visible, 0 = hidden

    def update(self):
        self.rect.y -= 1  # slide up...

        if self.alpha > 0:  # ... and fade away
            self.alpha -= self.fade_speed
            if self.alpha < 0:
                self.alpha = 0

        self.image.set_alpha(self.alpha)