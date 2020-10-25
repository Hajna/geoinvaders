import pygame
class Settings:

    def __init__(self):

        # SCREEN SETTINGI
        self.width = 1200
        self.height = 800
        self.color = (1, 20, 40)


        # ZUPI SETTINGI
        self.speed_factor = 1.8
        self.lives_limit = 2

        # BULLET SETTINGI
        self.bullet_speed_factor = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bulet_color = 200,200,0
        self.bullets_allowed = 3

        # ALIEN SETTING
        self.alien_speed_factor = 0.3
        self.alien_drop_speed = 0.13
        self.alien_direction = 1  # 1 je desno -1 je levo


        # KOLIKO POČAKAŠ PRI HITU
        self.cas = 0


