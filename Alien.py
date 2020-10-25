import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):

    def __init__(self, settings, screen):
        super().__init__()
        self.type = 0
        self.random_type()

        self.screen = screen
        self.settings = settings
        self.image = pygame.transform.scale(pygame.image.load(self.random_slika()), (60, 95))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.menjaj_random_x = self.random_zacetna() #stanje menjave strani, imam tudi absolutno stanje za robove screena
        self.random_stevec_x = 300 # stevec koliko casa najmanj nesmejo menjat smeri
        self.menjaj_random_y = 1
        self.random_stevec_y = 0
        self.random_stevec_y2 = 0
        self.cas_trajanja = 0




    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.random_stevec_x += 1
        self.random_stevec_y += 1
        if self.random_stevec_x > random.randrange(300, 1000):
            rand = random.randrange(0, 100)
            if rand == 0:
                self.menjaj_random_x *= -1
                self.random_stevec_x = 0
        self.x += self.settings.alien_speed_factor * self.settings.alien_direction * self.menjaj_random_x
        self.rect.x = self.x

        if self.random_stevec_y > 500:
            random_vkljucitev_y = random.randrange(5000) # to je vse treba dat v nastavitve !!!
            if random_vkljucitev_y == 0 and self.menjaj_random_y == 1:
                self.cas_trajanja_dvigovanja()
                self.menjaj_random_y = -1

            if self.menjaj_random_y == -1:
                self.random_stevec_y2 += 1
                if self.random_stevec_y2 > self.cas_trajanja:
                    self.menjaj_random_y = 1
                    self.random_stevec_y2 = 0


        self.y += self.settings.alien_drop_speed * self.menjaj_random_y
        self.rect.y = self.y


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 1:
            return True

    def random_zacetna(self):
        rand = random.randrange(0, 2)
        if rand == 0:
            return 1
        else:
            return -1

    def random_slika(self):
        if self.type == 0:
            return random.choice([r"slike\boki.bmp", r"slike\cigi.bmp", r'slike\dare.bmp', r'slike\deki.bmp', # to more v settinge
                                  r'slike\kuske.bmp',r'slike\repca.bmp',r'slike\ogi.bmp'])
        else:
            return r"slike\sliva.bmp"

    def cas_trajanja_dvigovanja(self):
        self.cas_trajanja = random.randrange(200,400)

    def random_type(self):
        rand = random.randrange(10)
        if rand == 0:
            self.type = 1