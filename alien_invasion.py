import pygame
from Settings import Settings
from zupi import Zupi
import game_functions as gf
from pygame.sprite import Group
from GameStats import GameStats
import random


def run_game():
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.width, s.height))
    pygame.display.set_caption("Judje")
    background = pygame.transform.smoothscale(pygame.image.load(r'slike\ff3.bmp').convert_alpha(), (1200, 800))
    stats = GameStats(s)
    zupi = Zupi(s, screen)
    bullets = Group()
    stepos = Group()
    gf.create_fleet(s, screen, zupi, stepos)

    while True:
        gf.check_events(s, screen, zupi, bullets)
        if stats.game_active:
          #  print(len(stepos))
            zupi.update()
            gf.update_bullets(bullets, stepos, s, screen, zupi)
            gf.update_stepos(s, stats, stepos, zupi, screen, bullets)
        gf.update_screen(screen, zupi, stepos, bullets, background)
run_game()