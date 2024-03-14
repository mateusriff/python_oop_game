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