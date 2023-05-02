import os
import pygame
import math
from map import Map

dirname = os.path.dirname(__file__)


class Turret:
    def __init__(self, name):
        self.name = name
        self.turret_sprite = self.import_sprite(self.name)
        self.ammo_sprite = self.import_sprite(self.name + "_ammo")
        self.reload_time = 0
        self.range = 0
        self.damage = 0
        self.cost = 0
        self.placed = False
        self.x_pos = 0
        self.y_pos = 0
        self.new_rotation = 0
        self.first_shot = 0
        # Give reload time, range, damage and cost based on turret type
        self.give_rt_r_d_c(self.name)

    def import_sprite(self, name):
        png = []
        try:
            png = pygame.image.load(os.path.join(
                dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def give_rt_r_d_c(self, type):
        if type == "cannon":
            self.reload_time = 5
            self.range = 5
            self.damage = 75
            self.cost = 100
        if type == "minigun":
            self.reload_time = 1
            self.range = 10
            self.damage = 5
            self.cost = 250
    
    def shoot_turret(self):
        if self.first_shot == 0:
            self.first_shot = pygame.time.get_ticks()
            return True
        if abs(self.first_shot - pygame.time.get_ticks()) >= self.reload_time*1000:
            self.first_shot == pygame.time.get_ticks()
            return True
        return False

    def draw_turret(self, window, mouse_pos):
        map = Map(window)
        circle_color = (255, 255, 255)
        scale = self.get_scale(window)
        scaled_sprite = pygame.transform.scale(self.turret_sprite, (scale[0]*0.8, scale[1]*0.8))
        if not self.placed:
            self.x_pos = mouse_pos[0]-scaled_sprite.get_size()[0]/2
            self.y_pos = mouse_pos[1]-scaled_sprite.get_size()[1]/2
            if Map.turret_check_tile(map, window, mouse_pos):
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.placed = True
            else:
                circle_color = (255, 0, 0)   
        scaled_sprite = pygame.transform.rotate(scaled_sprite, self.new_rotation)
        window.blit(scaled_sprite, (self.x_pos, self.y_pos))
        pygame.draw.circle(window, circle_color, (self.x_pos+scaled_sprite.get_size()[1]/2, self.y_pos+scaled_sprite.get_size()[1]/2), self.range*25, 1)

    def check_if_enemy_in_range(self, enemy):
        x_pos = enemy.x_pos
        y_pos = enemy.y_pos
        distance = math.hypot(x_pos - self.x_pos, y_pos - self.y_pos)

        # returns turret shot status
        if distance <= self.range*25:
            self.new_rotation = (180/ math.pi) * +math.atan2(self.y_pos - y_pos, x_pos - self.x_pos)-90
            if self.shoot_turret():
                return True
        return False

    def get_scale(self, window):
        width = window.get_width()
        height = window.get_height()
        # 4:3 aspect ratio
        if (width == 640 or width == 800 or width == 1024 or
            width == 1152 or (width == 1280 and height == 960)):
            return ((width/40)*2, (height/30)*2)
        # 16:9 aspect ratio
        if (width == 1280 and height == 720) or width == 1366 or width == 1600 or width == 1920:
            return ((width/160)*8, (height/90)*8)
        # 16:10 aspect ratio
        return ((width/160)*8, (height/100)*8)


class Turrets:
    def __init__(self):
        self.turrets = []

    def add_turret(self, turret):
        self.turrets.append(turret)

    def remove_turret(self, turret):
        self.turrets.remove(turret)
    
    def get_turrets(self):
        return self.turrets
