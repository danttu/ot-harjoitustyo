import pygame
import os
from menu import Menu
from settings import Settings
from map import Map

dirname = os.path.dirname(__file__)

class Main:
    def __init__(self):

        #Read and check settings
        self.settings = Settings()
        self.mixer = pygame.mixer.init()
        self.fps = self.settings.getFramerate()
        self.clock = pygame.time.Clock()
        self.resolution = self.settings.getResolution()

        self.mouseButtonHeldDown = False
        self.changed = False
        #Main menu: mainMenu, Settings: settingsMenu, Game: gameView
        self.currentScreen = "mainMenu"

        pygame.init()
        #Init menu and window
        self.window = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Tower Defence")
        self.menu = Menu(self.resolution[0], self.resolution[1], self.settings, True, self.settings.getVolume()[1])
        self.menu_objects = self.menu.object

        #Init map
        self.map = Map()

        pygame.display.update()
        
        #Starting gameloop
        self.runGame()

    def changeResolution(self):
        self.resolution = self.settings.getResolution()
        pygame.display.quit()
        self.window = pygame.display.set_mode(self.resolution)
        self.menu = Menu(self.resolution[0], self.resolution[1], self.settings, False, self.settings.getVolume()[1])
        self.menu_objects = self.menu.object

    def runGame(self):
        while True:
            self.eventHandler()
            self.drawScreen() 

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseButtonHeldDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseButtonHeldDown = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.currentScreen == "gameView":
                    self.currentScreen = "mainMenu"
            if self.changed:
                self.changed = False
                self.changeResolution()
                

    def drawScreen(self):
        mousePos = pygame.mouse.get_pos()
        #Menu
        self.window.fill((0, 0, 0))
        if self.currentScreen == "gameView":
            self.map.drawMap(self.window)
        for object in self.menu_objects:
            if object[1] == self.currentScreen:
                komento = object[0].display(self.window, mousePos, self.mouseButtonHeldDown)
                if komento == "Asetukset":
                    self.currentScreen = "settingsMenu"
                if komento == "Aloita Peli":
                    self.currentScreen = "gameView"
                    pass
                if komento == "Poistu pelistä":                    
                    exit()
                if komento == "Takaisin":
                    self.currentScreen = "mainMenu"
                if komento == "Käytä":
                    for o in self.menu_objects:
                        if o[0].getType() == "Slider":
                            if o[0].type == "sound":
                                sound_vol = o[0].value
                                continue
                            if o[0].type == "music":
                                music_vol = o[0].value
                                continue
                            if o[0].type == "resolution":
                                value = o[0].getValue()
                                print(value)
                                self.settings.setResolution(value)
                                self.changed = True
                    self.settings.setVolume(music_vol, sound_vol)                                 
        pygame.display.update()
        self.clock.tick(self.fps)

    def checkSettings(self, settings):
        settings_list = {}
        attribute = ""
        value = ""
        attribute_read = False
        for row in settings:
            row = row.replace("\n", "")     
            #Skip row if comment or empty
            if len(row) == 0 or row[0] == "#":
                continue
            #Read attribute and value
            attribute = ""
            value = ""
            attribute_read = False
            for letter in row:
                if letter == ":":
                    attribute_read = True
                    continue
                elif attribute_read == False:  
                    attribute += letter
                else:
                    value += letter
            #Remove unwanted spaces in value
            value = value.replace(" ", "")
            settings_list[attribute] = value
        return settings_list

if __name__ == "__main__":
    Main()