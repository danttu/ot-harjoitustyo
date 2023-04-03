import pygame
import os

dirname = os.path.dirname(__file__)

class Menu:
    def __init__(self, width, height):
        self.font = pygame.font.SysFont("Arial", 20)
        self.object = []
        
        #MainMenu objects
        self.object.append((Button((width/2)-50, height/2, 100, 50, "Aloita Peli", self.font), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+75, 100, 50, "Asetukset", self.font), "mainMenu"))
        self.object.append((Button((width/2)-50, (height/2)+150, 100, 50, "Poistu pelistä", self.font), "mainMenu"))
        self.object.append((Label((width/2)-125, (height/2)-200, "Tower Defence", 48), "mainMenu"))

class Label:
    def __init__(self, x_pos, y_pos, text, font_size):
        self.x = x_pos
        self.y = y_pos
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = (255, 255, 255)

        self.text = self.font.render(text, True, self.color)

    def display(self, window):
        window.blit(self.text, (self.x, self.y))

class Button:
    def __init__(self, x_pos, y_pos, width, height, text, font):
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

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonText = self.font.render(text, True, (25, 25, 25))

        self.buttonColors = {
            "unpressed" : "#ff0000",
            "hovered" : "#d66d6d"
        }
    
    def display(self, window):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.buttonColors["unpressed"])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.buttonColors["hovered"])
            if not self.isBeingHovered:
                self.isBeingHovered = True
                pygame.mixer.Sound.play(self.buttonHoverSound)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.isPressed:
                    self.isPressed = True
                    pygame.mixer.Sound.play(self.buttonPressedSound)
                    return self.text
            else:
                self.isPressed = False
        else:
            self.isBeingHovered = False

        self.buttonSurface.blit(self.buttonText, [self.buttonRect.width/2 - self.buttonText.get_rect().width/2, self.buttonRect.height/2 - self.buttonText.get_rect().height/2])
        window.blit(self.buttonSurface, self.buttonRect)

class Slider:
    #TBA
    pass