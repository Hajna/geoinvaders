import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, settings, screen, zupi):

        super().__init__()
        self.screen = screen

        # naredi bulletov rect na 0,0, nastelaj kasnej
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = zupi.rect.centerx
        self.rect.top = zupi.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bulet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)