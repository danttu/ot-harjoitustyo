import os
import sys
import pygame
from menu import Menu
from settings import Settings
from map import Map
from player import Player

dirname = os.path.dirname(__file__)


class Main:
    def __init__(self):

        # Read and check settings
        self.settings = Settings()
        self.mixer = pygame.mixer.init()
        self.fps = self.settings.get_framerate()
        self.clock = pygame.time.Clock()
        self.resolution = self.settings.get_resolution()

        self.mouse_button_held_down = False
        self.changed = False
        # Main menu: mainMenu, Settings: settingsMenu, Game: gameView
        self.current_screen = "mainMenu"

        pygame.init()
        # Init menu and window
        self.window = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Tower Defence")
        self.menu = Menu(self.resolution[0], self.resolution[1],
                         self.settings, True, self.settings.get_volume()[1])
        self.menu_objects = self.menu.object

        # Init player
        self.player = Player()
        # Init map
        self.map = Map()
        self.construct_mode = True

        pygame.display.update()
        # Starting gameloop
        self.run_game()

    def change_resolution(self):
        self.resolution = self.settings.get_resolution()
        pygame.display.quit()
        self.window = pygame.display.set_mode(self.resolution)
        self.menu = Menu(self.resolution[0], self.resolution[1],
                         self.settings, False, self.settings.get_volume()[1])
        self.menu_objects = self.menu.object

    def run_game(self):
        while True:
            self.event_handler()
            self.draw_screen()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_held_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_held_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.current_screen == "gameViewC":
                    self.current_screen = "mainMenu"
                    self.window.fill((0, 0, 0))
            if self.changed:
                self.changed = False
                self.change_resolution()

    def draw_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        # Menu
        if self.current_screen in ("gameViewC","gameview"):
            self.map.draw_map(self.window)
        if self.current_screen == "settingsMenu":
            pygame.draw.rect(self.window, (10, 10, 10), (50, 50, self.window.get_width(
            )-100, self.window.get_height()-100))
        for object in self.menu_objects:
            if object[1] == self.current_screen:
                command = object[0].display(
                    self.window, mouse_pos, self.mouse_button_held_down, self.player)
                if command == "Asetukset":
                    self.current_screen = "settingsMenu"
                if command == "Aloita Peli":
                    self.current_screen = "gameViewC"
                if command == "Poistu pelistä":
                    sys.exit(0)
                if command == "Takaisin":
                    self.current_screen = "mainMenu"
                if command == "Valmis":
                    self.current_screen = "gameView"
                if command == "Osta":
                    pass
                if command == "Käytä":
                    for obj in self.menu_objects:
                        if obj[0].getType() == "Slider":
                            if obj[0].type == "sound":
                                sound_vol = obj[0].value
                                continue
                            if obj[0].type == "music":
                                music_vol = obj[0].value
                                continue
                            if obj[0].type == "resolution":
                                value = obj[0].getValue()
                                self.settings.set_resolution(value)
                                self.changed = True
                    self.settings.set_volume(music_vol, sound_vol)
        pygame.display.update()
        self.clock.tick(self.fps)


if __name__ == "__main__":
    Main()
