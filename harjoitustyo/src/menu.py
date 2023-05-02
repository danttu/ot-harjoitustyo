import os
import pygame
from turrets import Turret
from map import Map

dirname = os.path.dirname(__file__)


class Menu:
    def __init__(self, width, height, settings, firstInit, sound_vol, player):
        self.font = pygame.font.SysFont("Arial", 20)
        self.object = []
        self.selected_turret = ""
        self.buy_button_created = False
        # Main Menu objects
        self.object.append((Button((width/2)-50, height/2, 100,
                           50, "Aloita Peli", self.font, sound_vol), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+75,
                           100, 50, "Asetukset", self.font, sound_vol), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+150, 100,
                           50, "Poistu pelistä", self.font, sound_vol), "mainMenu"))
        self.object.append(
            (Label((width/2)-125, (height/2)-200, "Tower Defence", 48), "mainMenu"))

        # Settings Menu objects
        self.object.append((Button((width/2)-100, (height/2)+150, 100,
                           50, "Takaisin", self.font, sound_vol), "settingsMenu"))
        self.object.append((Button((width/2)+100, (height/2)+150,
                           100, 50, "Käytä", self.font, sound_vol), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)-160, 200,
                           10, "music", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append(
            (Label((width/2)-55, (height/2)-200, "Musiikki", 20), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)-60, 200,
                           10, "sound", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append(
            (Label((width/2)-50, (height/2)-100, "Ääni", 20), "settingsMenu"))
        self.object.append((Slider((width/2)-100, (height/2)+40, 200, 10,
                           "resolution", settings, firstInit, sound_vol), "settingsMenu"))
        self.object.append(
            (Label((width/2)-50, (height/2), "Resoluutio", 20), "settingsMenu"))

        # Game objects when game started and construct mode is true
        self.object.append((Button(width-150, height-150, 100,
                           50, "Valmis", self.font, sound_vol), "gameViewC"))
        self.object.append((Icon(False, False, "cannon"), "gameViewC"))
        self.object.append((Icon(True, False, "minigun"), "gameViewC"))
        self.object.append(
            (Label(width-100, 20, "Rahaa: " + str(player.get_money()), 20), "gameViewC"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "gameViewC"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "gameViewC"))
        
        # Game objects when game started and construct mode is false
        self.object.append(
            (Label(width-100, 20, "Rahaa: " + str(player.get_money()), 20), "gameView"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "gameView"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "gameView"))
        self.already_pressed = False
        
    def allow_buy(self, window, sound_vol):
        width = window.get_width()
        height = window.get_height()
        if self.selected_turret in ("cannon", "minigun"):
            if not self.buy_button_created:
                self.object.append((Button(width-150, height-250, 100,
                           50, "Osta", self.font, sound_vol), "gameViewC"))
                self.buy_button_created = True

    def update_game_objects(self, window, sound_vol, player):
        width = window.get_width()
        height = window.get_height()
        window.fill((0, 0, 0))
        for object in self.object:
            if object[1] in ("gameViewC", "gameView"):
                self.object.remove(object)
        # Game objects when game started and construct mode is true
        self.object.append((Button(width-150, height-150, 100,
                           50, "Valmis", self.font, sound_vol), "gameViewC"))
        self.object.append((Icon(False, False, "cannon"), "gameViewC"))
        self.object.append((Icon(True, False, "minigun"), "gameViewC"))
        self.object.append(
            (Label(width-100, 20, "Rahaa: " + str(player.get_money()), 20), "gameViewC"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "gameViewC"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "gameViewC"))
        
        # Game objects when game started and construct mode is false
        self.object.append(
            (Label(width-100, 20, "Rahaa: " + str(player.get_money()), 20), "gameView"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "gameView"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "gameView"))

class Label:
    def __init__(self, x_pos, y_pos, text, font_size):
        self.x = x_pos
        self.y = y_pos
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = (255, 255, 255)

        self.text = self.font.render(text, True, self.color)

    def display(self, window, mouse, mouseStatus, player):
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

        self.buttonHoverSound = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "button.wav"))
        self.buttonPressedSound = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "buttonPressed.wav"))
        self.buttonHoverSound.set_volume(sound_vol)
        self.buttonPressedSound.set_volume(sound_vol)

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonText = self.font.render(text, True, (25, 25, 25))

        self.buttonColors = {
            "unpressed": "#ff0000",
            "hovered": "#d66d6d"
        }

    def display(self, window, mouse, mouseStatus, player):
        if not mouseStatus:
            Menu.already_pressed = False
        self.buttonSurface.fill(self.buttonColors["unpressed"])
        if self.buttonRect.collidepoint(mouse):
            self.buttonSurface.fill(self.buttonColors["hovered"])
            if not self.isBeingHovered:
                self.isBeingHovered = True
                pygame.mixer.Sound.play(self.buttonHoverSound)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.isPressed and not Menu.already_pressed:
                    Menu.already_pressed = True
                    if self.text == "Asetukset":
                        window.fill((0, 0, 0))
                    if self.text == "Takaisin":
                        window.fill((0, 0, 0))
                    self.isPressed = True
                    pygame.mixer.Sound.play(self.buttonPressedSound)
                    return self.text
                else:
                    return ""
            else:
                self.isPressed = False
        else:
            self.isBeingHovered = False

        self.buttonSurface.blit(self.buttonText, [self.buttonRect.width/2 - self.buttonText.get_rect(
        ).width/2, self.buttonRect.height/2 - self.buttonText.get_rect().height/2])
        window.blit(self.buttonSurface, self.buttonRect)
        return ""

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
                self.value = settings.get_volume()[1]
            if self.type == "music":
                self.value = settings.get_volume()[0]
            if self.type == "resolution":
                res = settings.get_resolution()
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
        self.sliderMoved = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "button.wav"))
        self.sliderMoved.set_volume(sound_vol)

    # Handles displaying and interaction of sliders
    def display(self, window, mouse, mouseStatus, player):
        newValue = False
        collide = self.rect_slider.collidepoint(mouse)
        if collide and not mouse[0] < self.x and not mouse[0] > self.x+200:
            if mouseStatus:
                self.x_circle = mouse[0]
                if not self.moved:
                    self.moved = True
                    pygame.mixer.Sound.play(self.sliderMoved)
            else:
                if self.moved:
                    self.moved = False
                    pygame.mixer.Sound.play(self.sliderMoved)
                    newValue = True
            self.value = abs(self.x-self.x_circle)
            self.value = round((self.value*100/self.width)/100, 1)

        self.x_circle = self.x+(20*(self.value*10))
        if self.type == "sound" or self.type == "music":
            value = self.value
            text = self.font.render(str(self.value), True, (255, 255, 255))
        if self.type == "resolution":
            value = self.getValue()
            value = str(value[0]) + "x" + str(value[1])
            text = self.font.render(str(value), True, (255, 255, 255))

        window.blit(text, (self.x+250, self.y))
        pygame.draw.rect(window, (255, 255, 0), self.rect_slider)
        pygame.draw.circle(window, (255, 255, 255),
                           (self.x_circle, self.y+5), 10)
        i = 0
        while i < 220:
            pygame.draw.rect(window, (100, 100, 100),
                             (self.x-2.5+i, self.y-10, 5, 30))
            i += 20

        if newValue:
            newValue = False
            return (self.type)

    # Returns slider value
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


class Icon:
    def __init__(self, x_offset, y_offset, name):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.name = name
        self.font = pygame.font.SysFont("Arial", 20)

    def display(self, window, mouse, mouseStatus, player):
        command = ""
        scale = self.getScale(window)
        x = (window.get_width()/2)+scale[0]*5+scale[0]
        y = (window.get_height()/2)-scale[1]*5
        if self.x_offset:
            x = (window.get_width()/2)+scale[0]*7+scale[0]
        if self.y_offset:
            y = (window.get_height()/2)-scale[1]*5+scale[1]
        rect = pygame.Rect(x, y, scale[0], scale[1])
        pygame.draw.rect(window, (255, 255, 255), (x, y, scale[0], scale[1]))
        turret = Turret(self.name)
        if turret.cost > player.get_money():
            text = self.font.render(str(turret.cost) + " $", True, (255, 0, 0))
        else:
            text = self.font.render(str(turret.cost) + " $", True, (255, 255, 255))

        if rect.collidepoint(mouse):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                Menu.selected_turret = self.name
                command = self.name

        window.blit(text, (x+scale[0]/4, y+scale[1]))
        window.blit(pygame.transform.scale(
            turret.turret_sprite, scale), (x, y))
        return command

    def getScale(self, window):
        width = window.get_width()
        height = window.get_height()
        # 4:3 aspect ratio
        if width == 640 or width == 800 or width == 1024 or width == 1152 or (width == 1280 and height == 960):
            return ((width/40)*2, (height/30)*2)
        # 16:9 aspect ratio
        if (width == 1280 and height == 720) or width == 1366 or width == 1600 or width == 1920:
            return ((width/160)*8, (height/90)*8)
        # 16:10 aspect ratio
        else:
            return ((width/160)*8, (height/100)*8)

    def getType(self):
        return "Icon"
