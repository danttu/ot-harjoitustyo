import pygame
import os

dirname = os.path.dirname(__file__)

class Menu:
    def __init__(self, width, height, settings, firstInit, sound_vol):
        self.font = pygame.font.SysFont("Arial", 20)
        self.object = []
        #Main Menu objects
        self.object.append((Button((width/2)-50, height/2, 100, 50, "Aloita Peli", self.font, sound_vol), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+75, 100, 50, "Asetukset", self.font, sound_vol), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+150, 100, 50, "Poistu pelistä", self.font, sound_vol), "mainMenu"))
        self.object.append((Label((width/2)-125, (height/2)-200, "Tower Defence", 48), "mainMenu"))

        #Settings Menu objects
        self.object.append((Button((width/2)-100, (height/2)+150, 100, 50, "Takaisin", self.font, sound_vol), "settingsMenu"))
        self.object.append((Button((width/2)+100, (height/2)+150, 100, 50, "Käytä", self.font, sound_vol), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)-160, 200, 10, "music", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append((Label((width/2)-55, (height/2)-200, "Musiikki", 20), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)-60, 200, 10, "sound", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append((Label((width/2)-50, (height/2)-100, "Ääni", 20), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)+40, 200, 10, "resolution", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append((Label((width/2)-50, (height/2), "Resoluutio", 20), "settingsMenu"))

        self.alreadyPressed = False

class Label:
    def __init__(self, x_pos, y_pos, text, font_size):
        self.x = x_pos
        self.y = y_pos
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = (255, 255, 255)

        self.text = self.font.render(text, True, self.color)

    def display(self, window, mouse, mouseStatus):
        window.blit(self.text, (self.x, self.y))
    
    def getType(self):
        return "Label"

class Button:
    def __init__(self, x_pos, y_pos, width, height, text, font, sound_vol):
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.isBeingHovered = False
        self.isPressed = False
        
        self.buttonHoverSound = pygame.mixer.Sound(os.path.join(dirname, "assets", "button.wav"))
        self.buttonPressedSound = pygame.mixer.Sound(os.path.join(dirname, "assets", "buttonPressed.wav"))
        self.buttonHoverSound.set_volume(sound_vol)
        self.buttonPressedSound.set_volume(sound_vol)

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonText = self.font.render(text, True, (25, 25, 25))

        self.buttonColors = {
            "unpressed" : "#ff0000",
            "hovered" : "#d66d6d"
        }
    
    def display(self, window, mouse, mouseStatus):
        if not mouseStatus:
            Menu.alreadyPressed = False
        self.buttonSurface.fill(self.buttonColors["unpressed"])
        if self.buttonRect.collidepoint(mouse):
            self.buttonSurface.fill(self.buttonColors["hovered"])
            if not self.isBeingHovered:
                self.isBeingHovered = True
                pygame.mixer.Sound.play(self.buttonHoverSound)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.isPressed and not Menu.alreadyPressed:
                    Menu.alreadyPressed = True
                    if self.text == "Asetukset":
                        window.fill((0, 0, 0))
                        pygame.draw.rect(window, (10, 10, 10), (50, 50, window.get_width()-100, window.get_height()-100))
                    if self.text == "Takaisin":
                        window.fill((0, 0, 0))
                    self.isPressed = True
                    pygame.mixer.Sound.play(self.buttonPressedSound)
                    return self.text
            else:
                self.isPressed = False
        else:
            self.isBeingHovered = False

        
        self.buttonSurface.blit(self.buttonText, [self.buttonRect.width/2 - self.buttonText.get_rect().width/2, self.buttonRect.height/2 - self.buttonText.get_rect().height/2])
        window.blit(self.buttonSurface, self.buttonRect)

    def getType(self):
        return "Button"

class Slider:
    def __init__(self, x_pos, y_pos, width, height, type, settings, firstInit, sound_vol):
        self.x = x_pos
        self.y = y_pos
        self.x_circle = self.x
        self.width = width
        self.height = height
        self.type = type
        self.value = 1.0
        if firstInit:
            self.value = 1.0
        else:
            if self.type == "sound":
                self.value = settings.getVolume()[1]
            if self.type == "music":
                self.value = settings.getVolume()[0]
            if self.type == "resolution":
                res = settings.getResolution()
                if res[0] == 640:
                    self.value = 0.0
                if res[0] == 800:
                    self.value = 0.1
                if res[0] == 1024:
                    self.value = 0.2
                if res[0] == 1152:
                    self.value = 0.3
                if res[0] == 1280 and res[1] == 720:
                    self.value = 0.4
                if res[0] == 1280 and res[1] == 960:
                    self.value = 0.5
                if res[0] == 1366:
                    self.value = 0.6
                if res[0] == 1440:
                    self.value = 0.7
                if res[0] == 1660:
                    self.value = 0.8
                if res[0] == 1680:
                    self.value = 0.9
                if res[0] == 1920:
                    self.value = 1.0
        self.rect_slider = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_circle = pygame.Rect(self.x, self.y-5, 20, 20)
        self.font = pygame.font.SysFont("Arial", 20)
        self.moved = False
        self.sliderMoved = pygame.mixer.Sound(os.path.join(dirname, "assets", "button.wav"))
        self.sliderMoved.set_volume(sound_vol)

    #Handles displaying and interaction of sliders
    def display(self, window, mouse, mouseStatus):
        newValue = False
        collide = self.rect_slider.collidepoint(mouse)
        if collide and not mouse[0] < self.x and not mouse[0] > self.x+200:
            if mouseStatus:
                self.x_circle = mouse[0]
                if not self.moved:
                    self.moved = True
                    pygame.mixer.Sound.play(self.sliderMoved)
                    #print(self.x_circle)
            else:
                if self.moved:
                    self.moved = False
                    pygame.mixer.Sound.play(self.sliderMoved)
                    newValue = True
                    #print(self.x_circle)
            self.value = abs(self.x-self.x_circle)
            self.value = round((self.value*100/self.width)/100, 1)
        
        self.x_circle = self.x+(20*(self.value*10))
        #print(self.value)
        if self.type == "sound" or self.type == "music":
            value = self.value
            text = self.font.render(str(self.value), True, (255, 255, 255))
        if self.type == "resolution":
            value = self.getValue()
            value = str(value[0]) + "x" + str(value[1])
            text = self.font.render(str(value), True, (255, 255, 255))

        window.blit(text, (self.x+250, self.y))
        pygame.draw.rect(window, (255, 255, 0), self.rect_slider)
        pygame.draw.circle(window, (255, 255, 255), (self.x_circle, self.y+5), 10)
        i = 0
        while i < 220:
            pygame.draw.rect(window,(100, 100, 100), (self.x-2.5+i, self.y-10, 5, 30))
            i += 20

        if newValue:
            newValue = False
            return (self.type)

    #Returns slider value
    def getValue(self):
        if self.type == "sound" or self.type == "music":
            return self.value
        if self.type == "resolution":
            if self.value == 0.0:
                return (640, 480)
            if self.value == 0.1:
                return (800, 600)
            if self.value == 0.2:
                return (1024, 768)
            if self.value == 0.3:
                return (1152, 864)
            if self.value == 0.4:
                return (1280, 720)
            if self.value == 0.5:
                return (1280, 960)
            if self.value == 0.6:
                return (1366, 768)
            if self.value == 0.7:
                return (1440, 900)
            if self.value == 0.8:
                return (1600, 900)
            if self.value == 0.9:
                return (1680, 1050)
            if self.value == 1.0:
                return (1920, 1080)
    
    def getType(self):
        return "Slider"