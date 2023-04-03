import pygame
from menu import Menu

class Main:
    def __init__(self):

        #Read and check settings
        with open("settings.txt", "r") as settings:
            settings_list = self.checkSettings(settings)
        self.fps = int(settings_list["framerate"])
        self.clock = pygame.time.Clock()
        try:
            self.resX = int(settings_list["resolutionX"])
            self.resY = int(settings_list["resolutionY"])
        except ValueError:
            print("Wrong resolution, using default values...")
            self.resX = 640
            self.resY = 480

        pygame.init()
        #Init menu and window
        self.window = pygame.display.set_mode((self.resX, self.resY))
        self.menu = Menu(self.resX, self.resY)
        self.menu_objects = self.menu.object

        pygame.display.update()
        
        #Starting gameloop
        self.runGame()

    def runGame(self):
        while True:
            self.eventHandler()
            self.drawScreen() 

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 

    def drawScreen(self):
        #Menu
        for object in self.menu_objects:
            if object[1] == "mainMenu":
                komento = object[0].display(self.window)
                if komento == "Asetukset":
                    #TBA
                    pass
                if komento == "Aloita Peli":
                    #TBA
                    pass
                if komento == "Poistu pelistä":
                    
                    exit()
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