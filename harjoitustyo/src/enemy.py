import os
import pygame

dirname = os.path.dirname(__file__)


class Enemy:
    def __init__(self, name, hp, speed, scale, start_tile, window):  # pylint: disable=invalid-name
        self.name = name
        self.hp = hp  # pylint: disable=invalid-name
        self.sprite = self.import_sprite(self.name)
        self.start_tile = start_tile
        self.scale = scale
        self.speed = speed
        self.x_pos = (window.get_width()/2)-scale[0]*(start_tile[0]+1)
        self.y_pos = (window.get_height()/2)-scale[1]*5
        self.scaled_sprite = pygame.transform.scale(self.sprite, (self.scale[0]*0.8, self.scale[1]*0.8))
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.scale[0]*0.8, self.scale[1]*0.8)
        self.current_rot = 0
        self.already_turned = True

        self.move_down = True
        self.move_right = False
        self.move_left = False
        self.move_up = False

    def import_sprite(self, name):
        png = []
        try:
            png = pygame.image.load(os.path.join(
                dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def take_hit(self, hitpoints):
        # If negative, change to zero
        hitpoints = max(hitpoints, 0)
        # If damage is bigger than enemy's health, make enemys's health to zero
        # and return True for enemy hp check
        if self.hp < hitpoints:
            self.hp = 0  
            return True
        self.hp -= hitpoints
        return False

    def draw_enemy(self, window):
        # Image rotation
        rotation = 0
        if not self.already_turned:
            if self.move_down:
                if self.current_rot == 180:
                    rotation = 180
                if self.current_rot == 90:
                    rotation = -90
                if self.current_rot == -90:
                    rotation = 90
                self.current_rot = 0
            if self.move_up:
                if self.current_rot == 0:
                    rotation = 180
                if self.current_rot == 90:
                    rotation = 90
                if self.current_rot == -90:
                    rotation = 270
                self.current_rot = 180
            if self.move_right:
                if self.current_rot == 180:
                    rotation = -90
                if self.current_rot == 0:
                    rotation = 90
                if self.current_rot == -90:
                    rotation = 180
                self.current_rot = 90
            if self.move_left:
                if self.current_rot == 180:
                    rotation = -270
                if self.current_rot == 90:
                    rotation = -180
                if self.current_rot == 0:
                    rotation = -90
                self.current_rot = -90
            self.already_turned = True
        self.scaled_sprite = pygame.transform.rotate(self.scaled_sprite, rotation)
        window.blit(self.scaled_sprite, (self.x_pos, self.y_pos))
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.scale[0]*0.8, self.scale[1]*0.8)
        pygame.draw.rect(window, (255, 255, 255), self.rect, 1)
    
    def move_enemy(self):
        if self.move_down:
            self.y_pos += self.speed
        if self.move_up:
            self.y_pos -= self.speed
        if self.move_right:
            self.x_pos += self.speed
        if self.move_left:
            self.x_pos -= self.speed

class Enemies:
    def __init__(self):
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def check_enemy_hp(self):
        for enemy in self.enemies:
            if enemy.check_enemy_hp(enemy) is True:
                self.remove_enemy(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)