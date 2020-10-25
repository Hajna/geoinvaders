import pygame

class Zupi:

    def __init__(self, settings, screen):
        self.screen = screen
        #self.image = pygame.image.load(r"slike\zupc2.bmp")
        self.image = pygame.transform.scale(pygame.image.load(r"slike\stepo2.bmp"), (90, 130))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.settings = settings

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.speed_factor

        self.rect.centerx = self.center

    def center_zupi(self):
        self.center = self.screen_rect.centerx