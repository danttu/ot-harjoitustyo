import os
import pygame
from enemy import Enemies
from enemy import Enemy

dirname = os.path.dirname(__file__)


class Map:
    def __init__(self):
        self.sprites = self.import_sprites()
        self.map = self.new_map()
        self.enemies = Enemies()
        self.start_tile = (self.find_start_tile(), 0)

    def add_enemies(self, current_round, window, i, sound_vol):
        enemy_hp = 100+20*current_round
        enemy_speed = 1+0.1*current_round
        enemy = Enemy("tank", enemy_hp, enemy_speed, self.get_scale(window),
                (self.start_tile[0], self.start_tile[1]-i), window, i, sound_vol)
        self.enemies.add_enemy(enemy)
        

    def import_sprites(self):
        pngs = []
        for name in ["grass", "flower", "flowers", "dirt", "base"]:
            try:
                pngs.append(pygame.image.load(
                    os.path.join(dirname, "assets", name + ".png")))
            except FileNotFoundError:
                print("You are missing: " + name + ".png")
        return pngs

    def new_map(self):
        map = [[0, 0, 3, 0, 0, 0, 2, 0, 1, 0],
               [0, 1, 3, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 3, 3, 3, 3, 3, 3, 3, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
               [4, 3, 3, 3, 3, 3, 3, 0, 3, 0],
               [0, 0, 0, 0, 0, 0, 3, 0, 3, 1],
               [0, 2, 1, 0, 3, 3, 3, 1, 3, 0],
               [0, 0, 0, 0, 3, 0, 0, 0, 3, 0],
               [0, 0, 2, 0, 3, 3, 3, 3, 3, 2],
               [1, 0, 0, 0, 0, 0, 2, 0, 2, 0]]
        return map

    def draw_map(self, window):
        scale = self.get_scale(window)
        x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
        y = (window.get_height()/2)-scale[1]*5  # pylint: disable=invalid-name
        i = 0
        j = 0
        while j <= 9:
            if i > 9:
                i = 0
                j += 1
                x = (window.get_width()/2) - \
                    scale[0]*5  # pylint: disable=invalid-name
                y += scale[1]  # pylint: disable=invalid-name
                continue
            tile = self.map[j][i]
            scaled_tile = self.sprites[tile]
            if tile == 4:
                scaled_tile = pygame.transform.scale(scaled_tile, scale)
            else:
                scaled_tile = pygame.transform.scale(scaled_tile, scale)
            window.blit(scaled_tile, (x, y))
            x += scale[0] # pylint: disable=invalid-name
            i += 1

    def turret_check_tile(self, window, mouse_pos):
        scale = self.get_scale(window)
        placable_tile = pygame.Rect(0, 0, 0, 0)
        x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
        y = (window.get_height()/2)-scale[1]*5  # pylint: disable=invalid-name
        i = 0
        j = 0
        while j <= 9:
            if i > 9:
                i = 0
                j += 1
                x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
                y += scale[1]  # pylint: disable=invalid-name
                continue
            tile = self.map[j][i]
            if tile in (0, 1, 2):
                placable_tile = pygame.Rect(x, y, scale[0], scale[1])
            if placable_tile.collidepoint(mouse_pos):
                return True
            x += scale[0] # pylint: disable=invalid-name
            i += 1
        return False
    
    def enemy_check_tile(self, enemy, window):
        find_new = False
        scale = self.get_scale(window)
        placable_tile = pygame.Rect(0, 0, 0, 0)
        current_tile = (0, 0)
        x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
        y = (window.get_height()/2)-scale[1]*5  # pylint: disable=invalid-name
        i = 0
        j = 0
        while j <= 9:
            if i > 9:
                i = 0
                j += 1
                x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
                y += scale[1]  # pylint: disable=invalid-name
                continue
            tile = self.map[j][i]
            if tile in (0, 1, 2, 4):
                placable_tile = pygame.Rect(x, y, scale[0], scale[1])
            if placable_tile.colliderect(enemy.rect):
                # If enemy makes contact with base take damage every two second
                if tile == 4:
                    enemy.enemy_at_base = True
                    break
                find_new = True
                if enemy.move_down:
                    current_tile = (i, j-1)
                    enemy.y_pos -= enemy.speed
                if enemy.move_up:
                    current_tile = (i, j+1)
                    enemy.y_pos += enemy.speed
                if enemy.move_right:
                    current_tile = (i-1, j)
                    enemy.x_pos -= enemy.speed
                if enemy.move_left:
                    current_tile = (i+1, j)
                    enemy.x_pos += enemy.speed
                break
            x += scale[0] # pylint: disable=invalid-name
            i += 1
        
        # Find next road tile
        if find_new:
            try:
                up_tile = self.map[current_tile[1]-1][current_tile[0]]
            except IndexError:
                up_tile = 0
            try:
                down_tile = self.map[current_tile[1]+1][current_tile[0]]
            except IndexError:
                down_tile = 0
            try:
                right_tile = self.map[current_tile[1]][current_tile[0]+1]
            except IndexError:
                right_tile = 0
            try:
                left_tile = self.map[current_tile[1]][current_tile[0]-1]
            except IndexError:
                left_tile = 0
            if enemy.move_down:
                if right_tile == 3:
                    enemy.move_down = False
                    enemy.move_right = True
                if left_tile == 3:
                    enemy.move_down = False
                    enemy.move_left = True
                enemy.already_turned = False
            elif enemy.move_up:
                if right_tile == 3:
                    enemy.move_up = False
                    enemy.move_right = True
                if left_tile == 3:
                    enemy.move_up = False
                    enemy.move_left = True
                enemy.already_turned = False
            elif enemy.move_right:
                if up_tile == 3:
                    enemy.move_up = True
                    enemy.move_right = False
                if down_tile == 3:
                    enemy.move_down = True
                    enemy.move_right = False
                enemy.already_turned = False
            else: 
                if up_tile == 3:
                    enemy.move_up = True
                    enemy.move_left = False
                if down_tile == 3:
                    enemy.move_down = True
                    enemy.move_left = False 
                enemy.already_turned = False
    def find_start_tile(self):
        # First road tile is start_tile
        i = 0
        for tile in self.map[0]:
            if tile == 3:
                return i
            i += 1
        return 0

    def get_start_tile(self):
        return self.start_tile  

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
