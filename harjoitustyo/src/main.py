import os
import sys
import pygame
from menu import Menu
from settings import Settings
from map import Map
from player import Player

dirname = os.path.dirname(__file__)

class Main:
    """Game's main class.
    
    Attributes:
        settings: Game settings.
        mixer: Audio mixer.
        fps: Game framerate.
        clock: Clock for running game loop at given clock cycle (in this case it's framerate).
        resolution: Window resolution.
        mouse_button_held_down: Boolean, true if mouse left button is held down. 
        changed: Boolean, true if in settings menu "apply" or in this case
        "Käytä" button has been pressed.
        allowed_enemies_on_screen: Counter for enemies to spawn.
        enemy_inerval: Interval between enemy spawning.
        enemy_added: Boolean, true if enem has been added and allowed_enemies_on_screen hasn't been
        changed after that.
        stop_spawning: Boolean, true if allowed_enemies_on_screen has hit spawn limit
        (in this case it's 10 + current round).
        current_screen: Tells what screen should be displayed.
        player: Player object that contains info about current round, money amount,
        owned turrets, desroyed enemies and base's hp.
        window: Game window.
        menu: Game UI.
        menu_objects: Objects of UI.
        map: Game map.
    """
    def __init__(self):
        """Game initialization."""
        self.settings = Settings()
        self.mixer = pygame.mixer.init()
        self.fps = self.settings.get_framerate()
        self.clock = pygame.time.Clock()
        self.resolution = self.settings.get_resolution()
        self.mouse_button_held_down = False
        self.changed = False
        self.allowed_enemies_on_screen = 0
        self.enemy_interval = 0
        self.enemy_added = False
        self.stop_spawning = False
        self.current_screen = "main_menu"
        self.player = Player()
        pygame.init()
        self.window = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Tower Defence")
        self.menu = Menu(self.resolution[0], self.resolution[1],
                         self.settings, True, self.settings.get_volume()[1], self.player)
        self.menu_objects = self.menu.object
        self.map = Map()
        self.run_game()

    def change_resolution(self):
        """Changes window resolution and resets UI objects, map and player values."""
        self.resolution = self.settings.get_resolution()
        pygame.display.quit()
        self.window = pygame.display.set_mode(self.resolution)
        self.map = Map()
        self.allowed_enemies_on_screen = 0
        self.player = Player()
        self.update_values()

    def run_game(self):
        """Game loop."""
        while True:
            self.window.fill((0, 0, 0))
            self.event_handler()
            self.draw_screen()

    def event_handler(self):
        """Handles keypresses and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_held_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_held_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.current_screen in (
                    "construction_view", "game_view"):
                    self.current_screen = "results_view"
                    self.window.fill((0, 0, 0))
        if self.changed:
            self.changed = False
            self.change_resolution()
        if self.current_screen == "game_view":
            if self.allowed_enemies_on_screen == 10 + self.player.get_current_round():
                self.stop_spawning = True
            if not self.stop_spawning:
                if abs(self.enemy_interval-pygame.time.get_ticks()) >= 2000:
                    self.enemy_interval = pygame.time.get_ticks()
                    self.allowed_enemies_on_screen += 1
                    self.enemy_added = False

            if self.allowed_enemies_on_screen <= (
                10 + self.player.get_current_round()) and not self.enemy_added:
                self.enemy_added = True
                self.map.add_enemies(self.player.get_current_round(),
                                      self.window, self.allowed_enemies_on_screen,
                                      self.settings.get_volume()[1])
            remove_enemy = False
            for turret in self.player.turrets.turrets:
                for enemy in self.map.enemies.enemies:
                    if turret.check_if_enemy_in_range(enemy):
                        if enemy.take_hit(turret.damage):
                            remove_enemy = True
                    if remove_enemy:
                        self.map.enemies.remove_enemy(enemy)
                        self.player.add_destroyed_enemy()
                        self.player.add_money(int(2+0.25*self.player.get_current_round()))
                        self.update_values()
                        remove_enemy = False
                        continue
                turret.first_enemy = -1
            for enemy in self.map.enemies.enemies:
                self.map.enemy_check_tile(enemy, self.window)
                enemy.move_enemy()
                if enemy.enemy_at_base:
                    if enemy.last_shot == 0:
                        enemy.last_shot = pygame.time.get_ticks()
                        self.player.take_hit(1)
                        if enemy.take_hit(15):
                            self.map.enemies.remove_enemy(enemy)
                            self.player.add_destroyed_enemy()
                            self.player.add_money(int(1+0.1*self.player.get_current_round()))
                    if abs(enemy.last_shot-pygame.time.get_ticks()) >= 2000:
                        enemy.last_shot = pygame.time.get_ticks()
                        self.player.take_hit(1)
                        if enemy.take_hit(10):
                            self.map.enemies.remove_enemy(enemy)
                            self.player.add_destroyed_enemy()
                            self.player.add_money(int(1+0.1*self.player.get_current_round()))
                        self.update_values()
        if self.player.get_health() == 0:
            self.current_screen = "results_view"
        if len(self.map.enemies.enemies) == 0 and self.stop_spawning:
            self.player.next_round()
            self.update_values()
            self.allowed_enemies_on_screen = 0
            self.stop_spawning = False
            self.current_screen = "construction_view"

    def update_values(self):
        """Updates UI objects with new values."""
        self.menu = Menu(self.resolution[0], self.resolution[1],
                         self.settings, False, self.settings.get_volume()[1], self.player)
        self.menu_objects = self.menu.object

    def reset_game(self):
        """Resets whole game."""
        self.player = Player()
        self.map = Map()
        self.allowed_enemies_on_screen = 0
        self.enemy_interval = 0
        self.enemy_added = False
        self.stop_spawning = False
        self.update_values()

    def draw_screen(self):
        """Handles screen drawing"""
        mouse_pos = pygame.mouse.get_pos()
        if self.current_screen in ("construction_view", "game_view"):
            self.map.draw_map(self.window)
        if self.current_screen == "results_view":
            pygame.draw.rect(self.window, (10, 10, 10), (100, 100, self.window.get_width(
            )-200, self.window.get_height()-200))
        if self.current_screen == "settings_menu":
            pygame.draw.rect(self.window, (10, 10, 10), (50, 50, self.window.get_width(
            )-100, self.window.get_height()-100))
        for object in self.menu_objects:
            if object[1] == self.current_screen:
                command = object[0].display(
                    self.window, mouse_pos, self.mouse_button_held_down, self.player)
                if command == "Aloita uusi peli":
                    self.reset_game()
                    self.current_screen = "construction_view"
                if command == "Poistu päävalikkoon":
                    self.reset_game()
                    self.current_screen = "main_menu"
                if command == "Asetukset":
                    self.current_screen = "settings_menu"
                if command == "Aloita Peli":
                    self.window.fill((0, 0, 0))
                    self.current_screen = "construction_view"
                if command == "Poistu pelistä":
                    sys.exit(0)
                if command == "Takaisin":
                    self.current_screen = "main_menu"
                if command == "Valmis":
                    self.window.fill((0, 0, 0))
                    self.current_screen = "game_view"
                    self.enemy_interval = pygame.time.get_ticks()
                    self.update_values()
                if command in ("cannon", "minigun"):
                    self.menu.selected_turret = command
                    self.menu.allow_buy(self.window, self.settings.get_volume()[1])
                if command == "Osta":
                    if self.player.buy_turret(self.menu.selected_turret,
                                               self.settings.get_volume()[1], self.window):
                        self.update_values()
                    else:
                        print("Sinulla ei ole tarpeeksi rahaa!")
                if command == "Käytä":
                    for obj in self.menu_objects:
                        if obj[0].get_type() == "Slider":
                            if obj[0].type == "sound":
                                sound_vol = obj[0].value
                                continue
                            if obj[0].type == "music":
                                music_vol = obj[0].value
                                continue
                            if obj[0].type == "resolution":
                                value = obj[0].get_value()
                                self.settings.set_resolution(value)
                                self.changed = True
                    self.settings.set_volume(music_vol, sound_vol)
        if self.current_screen in ("construction_view", "game_view"):
            for turret in self.player.turrets.get_turrets():
                turret.draw_turret(self.window, mouse_pos, self.map)
        if len(self.map.enemies.enemies) > 0:
            if self.current_screen == "game_view":
                for enemy in self.map.enemies.enemies:
                    enemy.draw_enemy(self.window)

        pygame.display.update()
        self.clock.tick(self.fps)
Main()
