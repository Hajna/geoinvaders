import sys
import pygame
from bullet import Bullet
from Alien import Alien
from time import sleep
import random



def check_events(settings, screen, zupi, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, zupi, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, zupi)

def update_screen(screen, zupi, stepos, bullets, background):
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    zupi.blitme()
    stepos.draw(screen)
    pygame.display.flip()


def check_keydown_events(event, settings, screen, zupi, bullets):
    if event.key == pygame.K_RIGHT:
        zupi.moving_right = True
    elif event.key == pygame.K_LEFT:
        zupi.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings, screen, zupi, bullets)

def check_keyup_events(event, zupi):
    if event.key == pygame.K_RIGHT:
        zupi.moving_right = False
    elif event.key == pygame.K_LEFT:
        zupi.moving_left = False

def update_bullets(bullets, stepos, settings, screen, zupi):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collisions(settings,screen,zupi,stepos,bullets)

def check_collisions(settings,screen, zupi, stepos, bullets):
    collisions = pygame.sprite.groupcollide(bullets, stepos, True, True)
    if len(stepos) == 0:
        bullets.empty()
        create_fleet(settings, screen, zupi, stepos)

def fire_bullets(settings, screen, zupi, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, zupi)
        bullets.add(new_bullet)

def create_fleet(settings, screen, zupi, stepos):
    stepo = Alien(settings, screen)
    num_rows = get_number_rows(settings, zupi.rect.height, stepo.rect.height)
    for vrsta in range(num_rows):
        for stepc in range(get_number_stepos(settings,stepo.rect.width)):
            r = random.randrange(10000)
            create_stepo(settings, screen, stepos, stepc, vrsta, r)


def get_number_stepos(settings, stepo_width):
    available_space_x = settings.width - 2 * stepo_width
    return int(available_space_x / (2 * stepo_width)) - 5

def create_stepo(settings, screen, stepos, i, row_num, r):

    razmik_faktor = 5

    stepo = Alien(settings, screen)
    stepo_width = stepo.rect.width
    stepo.x = 130 + stepo_width + razmik_faktor * stepo_width * i
    stepo.y = stepo.rect.height / 5 + 1.2 * stepo.rect.height * row_num
    stepo.rect.x = stepo.x
    stepo.rect.y = stepo.y
    stepo.seed = r
    stepos.add(stepo)

def get_number_rows(settings, zupi_height, stepo_height):
    avaliable_space_y = (settings.height - 3 * stepo_height - zupi_height)
    return int(avaliable_space_y / (1.2 * stepo_height))

def update_stepos(settings, stats, stepos, zupi, screen, bullets):
    check_fleet_edges(settings, stepos)
    for i in range(len(stepos)):
        stepos.sprites()[i].update()
    grupa_ki_ubije = stepos.copy() #logika da locimo tiste ki jih poberes in tiste ki jih ne , v zepos grejo tisti ki te ubijejo
    grupa_ki_ubije.empty()
    for s in stepos.sprites():
        if s.type == 0: # type 0 je ta ki ubije (navaden)
            grupa_ki_ubije.add(s)

    if pygame.sprite.spritecollideany(zupi, grupa_ki_ubije):
        zupi_hit(settings, stats, screen, zupi, stepos, bullets)
    check_stepos_bottom(settings, stats, screen, zupi, grupa_ki_ubije, bullets)

def check_fleet_edges(settings, stepos):
    for stepo in stepos.sprites():
        if stepo.check_edges():
            change_fleet_direction(settings, stepos)
            break

def check_stepos_bottom(settings, stats, screen, zupi, stepos, bullets):
    screen_rect = screen.get_rect()
    for stepo in stepos.sprites():
        if stepo.rect.bottom >= screen_rect.bottom:
            zupi_hit(settings, stats, screen, zupi, stepos, bullets)
            break

def change_fleet_direction(settings, stepos):
    for stepo in stepos.sprites():
        stepo.rect.y += settings.alien_drop_speed
    settings.alien_direction *= -1

def zupi_hit(settings, stats, screen, zupi, stepos, bullets):
    if stats.lives_left > 0:
        stats.lives_left -= 1
        stepos.empty()
        bullets.empty()
        zupi.center_zupi()
        settings.alien_direction = 1
        create_fleet(settings, screen, zupi, stepos)
        sleep(1)

    else:
        stats.game_active = False

#def bonus_hit

#def spremeni settinge

def vrni_stevilo_stepotov(stepos):
    return len(stepos)