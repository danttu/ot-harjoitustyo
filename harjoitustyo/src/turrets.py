import os
import pygame
import math
from map import Map

dirname = os.path.dirname(__file__)


class Turret:
    """Turret object.

    Attributes:
        map: Game's map. Used for get_scale().
        name: Turret name.
        ammo_sprite: Name for ammo sprite file.
        reload_time: Turret's reload time.
        range: Turret's range.
        damage: Turrent's damage
        cost: Turret price.
        scale: Scale for matching sprite size with window and map.
        placed: Defines if turret has been placed on the map.
        shoot_sound: Sound file for turret shooting.
        x_pos: Turret's x position.
        y_pos: Turret's y position.
        new_rotation: New rotation angle for rotating turret.
        first_shot: Defines if it's turret's first shot.
        time_elapsed_after_shot: Time between turret shot and current tick.
        first_enemy: Used for checking if enemy in radius
        is first to be in range.
    """
    def __init__(self, name, sound_vol, window):
        """Turret initialization.

        Args:
            name: Turret name.
            sound_vol: Game's sound volume value.
            window: Game's window.
        """
        map = Map()
        self.name = name
        self.turret_sprite = self.import_sprite(self.name)
        self.ammo_sprite = self.import_sprite(self.name + "_ammo")
        self.reload_time = 0
        self.range = 0
        self.damage = 0
        self.cost = 0
        self.scale = map.get_scale(window)
        self.placed = False
        self.shoot_sound = self.import_sound(self.name)
        self.shoot_sound.set_volume(sound_vol)
        self.x_pos = 0
        self.y_pos = 0
        self.new_rotation = 0
        self.first_shot = 0
        self.time_elapsed_after_shot = 0
        self.first_enemy = -1
        # Give reload time, range, damage and cost based on turret type
        self.give_specs(self.name, self.scale)

    def import_sprite(self, name):
        """Imports sprite.

        Args:
            name: Turret name

        Returns:
            Sprite if found.
        """
        png = []
        try:
            png = pygame.image.load(os.path.join(
                dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def import_sound(self, name):
        """Imports sound file.

        Args:
            name: Sound file name.

        Returns:
            Sound file if found.
        """
        shoot_sound = 0
        try:
            shoot_sound = pygame.mixer.Sound(
            os.path.join(dirname, "assets", name + "_shoot.wav"))
        except FileNotFoundError:
            print("You are missing: " + name + "_shoot.wav")
        return shoot_sound

    def give_specs(self, type, scale):
        """Give turret attributes based on turret type.

        Args:
            type: Turret type.
            scale: Scale for matching sprite size with window and map.
        """
        if type == "cannon":
            self.reload_time = 5
            self.range = scale[0]/64*5
            self.damage = 75
            self.cost = 125
        if type == "minigun":
            self.reload_time = 0.5
            self.range = scale[0]/64*8
            self.damage = 10
            self.cost = 325
    def reload_turret(self):
        """Calculates time elapsed after shot.

        Used for drawing reload time bar for turrets.
        """
        if self.first_shot == 0:
            self.time_elapsed_after_shot = self.reload_time*1000
        else:
            self.time_elapsed_after_shot = abs(self.first_shot - pygame.time.get_ticks())
            if self.time_elapsed_after_shot >= self.reload_time*1000:
                self.time_elapsed_after_shot = self.reload_time*1000

    def shoot_turret(self):
        """Shoots if reloaded.

        Returns:
            True if was able to shoot. Else returns false.
        """
        if self.first_shot == 0:
            self.first_shot = pygame.time.get_ticks()
            self.time_elapsed_after_shot = 0
            pygame.mixer.Sound.play(self.shoot_sound)
            return True
        if abs(self.first_shot - pygame.time.get_ticks()) >= self.reload_time*1000:
            self.first_shot = pygame.time.get_ticks()
            self.time_elapsed_after_shot = 0
            pygame.mixer.Sound.play(self.shoot_sound)
            return True
        return False

    def draw_turret(self, window, mouse_pos, map):
        """Draws turret, reload bar, and range radius.

        Args:
            window: Game's window.
            mouse_pos: Mouse cursor position.
            map: Game's map
        """
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
        self.reload_turret()
        difference = 100*((self.reload_time*1000)-
                          self.time_elapsed_after_shot)/(self.reload_time*1000)
        reload_rect_border = pygame.Rect(self.x_pos+scale[0]/4,
                                          self.y_pos+scale[1]*0.8+scale[1]/8,
                                          scale[0]*0.6, scale[1]*0.1)
        reload_time_rect = pygame.Rect(self.x_pos+scale[0]/4,
                                          self.y_pos+scale[1]*0.8+scale[1]/8,
                                          scale[0]*0.6*(1.0-(difference/100)), scale[1]*0.1)
        pygame.draw.rect(window, (0, 0, 0), reload_rect_border, 1)
        pygame.draw.rect(window, (255, 255, 255), reload_time_rect)

        scaled_sprite_rect = scaled_sprite.get_rect()
        rotated_sprite = pygame.transform.rotate(scaled_sprite, self.new_rotation)
        rotated_rect = scaled_sprite_rect.copy()
        rotated_rect.center = rotated_sprite.get_rect().center
        rotated_sprite = rotated_sprite.subsurface(rotated_rect).copy()
        window.blit(rotated_sprite, (self.x_pos, self.y_pos))
        pygame.draw.circle(window, circle_color,
                            (self.x_pos+scaled_sprite.get_size()[1]/2, self.y_pos+
                             scaled_sprite.get_size()[1]/2), self.range*25, 1)

    def check_if_enemy_in_range(self, enemy):
        """Checks whether enemy is in range or not.

        Args:
            enemy: Enemy that is being checked.

        Returns:
            True if turret was able to shoot. Else returns false.
        """
        x_pos = enemy.x_pos
        y_pos = enemy.y_pos
        distance = math.hypot(x_pos - self.x_pos, y_pos - self.y_pos)

        # returns turret shot status
        if distance <= self.range*25:
            # Check if first enemy in radius
            # If first enemy in radius
            if self.first_enemy == -1:
                self.first_enemy = enemy.id
            # If id is same as first enemy's id
            if enemy.id == self.first_enemy:
                self.new_rotation = (180/ math.pi) * +math.atan2(self.y_pos
                                                                  - y_pos, x_pos - self.x_pos)-90
                if self.shoot_turret():
                    return True
                return False
        return False

    def get_scale(self, window):
        """Gives scale to match resolution and map.

        Args:
            window: Game's window.

        Returns:
            Scale based on resolution and aspect ratio.
        """
        width = window.get_width()
        height = window.get_height()
        if (width == 640 or width == 800 or width == 1024 or
            width == 1152 or (width == 1280 and height == 960)):
            return ((width/40)*2, (height/30)*2)
        if (width == 1280 and height == 720) or width == 1366 or width == 1600 or width == 1920:
            return ((width/160)*8, (height/90)*8)
        return ((width/160)*8, (height/100)*8)


class Turrets:
    """Turrets object that stores player owned turrets in list.

    Attributes:
        turrets: List of player owned turrets.
    """
    def __init__(self):
        """Turrets initialization."""
        self.turrets = []

    def add_turret(self, turret):
        """Adds turret to list.

        Args:
            turret: Turret object.
        """
        self.turrets.append(turret)

    def get_turrets(self):
        """Gives all turrets in list.

        Returns:
            List of player owned turrets.
        """
        return self.turrets
