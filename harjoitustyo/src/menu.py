import os
import pygame
from turrets import Turret

dirname = os.path.dirname(__file__)


class Menu:
    """Game UI.
    
    Attributes:
        font: Font for text in buttons and labels.
        object: List of UI objects
        buy_button_created: Defines if "buy" button has been created.
        already_pressed: Defines if button was already pressed.
    """
    def __init__(self, width, height, settings, first_init, sound_vol, player):
        """UI initialization.
        
        Args:
            width: Window width.
            height: Window height.
            settings: Game settings.
            first_init: Defines if it's first time initializing object.
            sound_vol: Game's sound volume value.
            player: Player object.
        """
        self.font = pygame.font.SysFont("Arial", 20)
        self.object = []
        self.selected_turret = ""
        self.buy_button_created = False

        self.object.append((Button((width/2)-50, height/2, 100,
                           50, "Aloita Peli", self.font, sound_vol), "main_menu"))
        self.object.append((Button((width/2)-50, (height/2)+75,
                           100, 50, "Asetukset", self.font, sound_vol), "main_menu"))
        self.object.append((Button((width/2)-50, (height/2)+150, 100,
                           50, "Poistu pelistä", self.font, sound_vol), "main_menu"))
        self.object.append(
            (Label((width/2)-125, (height/2)-200, "Tower Defence", 48), "main_menu"))

        self.object.append((Button((width/2)-100, (height/2)+150, 100,
                           50, "Takaisin", self.font, sound_vol), "settings_menu"))
        self.object.append((Button((width/2)+100, (height/2)+150,
                           100, 50, "Käytä", self.font, sound_vol), "settings_menu"))
        self.object.append((Slider((width/2)-100, (height/2)-160, 200,
                           10, "music", settings, first_init, sound_vol), "settings_menu"))
        self.object.append(
            (Label((width/2)-55, (height/2)-200, "Musiikki", 20), "settings_menu"))
        self.object.append((Slider((width/2)-100, (height/2)-60, 200,
                           10, "sound", settings, first_init, sound_vol), "settings_menu"))
        self.object.append(
            (Label((width/2)-50, (height/2)-100, "Ääni", 20), "settings_menu"))
        self.object.append((Slider((width/2)-100, (height/2)+40, 200, 10,
                           "resolution", settings, first_init, sound_vol), "settings_menu"))
        self.object.append(
            (Label((width/2)-50, (height/2), "Resoluutio", 20), "settings_menu"))

        self.object.append((Button(width-150, height-150, 100,
                           50, "Valmis", self.font, sound_vol), "construction_view"))
        self.object.append((Icon(False, False, "cannon"), "construction_view"))
        self.object.append((Icon(True, False, "minigun"), "construction_view"))
        self.object.append(
            (Label(width-150, 20, "Rahaa: " + str(player.get_money()), 20), "construction_view"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "construction_view"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "construction_view"))
        
        self.object.append(
            (Label(width-150, 20, "Rahaa: " + str(player.get_money()), 20), "game_view"))
        self.object.append(
            (Label(100, 20, "Elämät: " + str(player.get_health()), 20), "game_view"))
        self.object.append(
            (Label(width/2, 20, "Kierros: " + str(player.get_current_round()), 20), "game_view"))
        self.already_pressed = False

        self.object.append(
            (Label(width/2-50, 125,
                    "Peli päättyi!", 32), "results_view"))
        self.object.append(
            (Label(width/2-50, 175,
                    "Pääsit kierrokselle " + str(player.get_current_round()), 20), "results_view"))
        self.object.append(
            (Label(width/2-50, 200,
                    "Rahamäärä: " + str(player.get_money()), 20), "results_view"))
        self.object.append(
            (Label(width/2-50, 225,
                    "Vihollisia tuhottu yhteensä: " + str(player.get_destroyed_enemies()), 20), "results_view"))
        self.object.append((Button((width/2)-50, height/2+50, 150,
                           35, "Aloita uusi peli", self.font, sound_vol), "results_view"))
        self.object.append((Button((width/2)-50, (height/2)+100, 150,
                           35, "Poistu päävalikkoon", self.font, sound_vol), "results_view"))

    def allow_buy(self, window, sound_vol):
        width = window.get_width()
        height = window.get_height()
        if self.selected_turret in ("cannon", "minigun"):
            if not self.buy_button_created:
                self.object.append((Button(width-150, height-250, 100,
                           50, "Osta", self.font, sound_vol), "construction_view"))
                self.buy_button_created = True

class Label:
    """Text object.
    
    Attributes:
        x: Text's x position.
        y: Text's y position.
        font: Text font.
        color: Text color.
        text: String of text.
    """
    def __init__(self, x_pos, y_pos, text, font_size):
        """Label initialization.
        
        Args:
            x_pos: X position for label.
            y_pos: Y posiion for label.
            text: String of text for label.
            font_size: Label size.
        """
        self.x = x_pos
        self.y = y_pos
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = (255, 255, 255)

        self.text = self.font.render(text, True, self.color)

    def display(self, window, mouse, mouse_status, player):
        """Handles label draw.
        
        Args:
            window: Game's window.
            mouse: Not used here.
            mouse_status: Not used here.
            player: Not used here.
        """
        window.blit(self.text, (self.x, self.y))

    def get_type(self):
        """Returns type of object.
        
        Returns:
            Returns name of object.
        """
        return "Label"


class Button:
    """Button object.
    
    Attributes:
        x: Button x position.
        y: Button y position.
        width: Button width.
        height: Button height.
        text: Button's text.
        font: Button's text font.
        is_being_hovered: Defines if mouse hovers over button.
        is_pressed: Defines if button is pressed.
        button_hover_sound: Sound for when mouse hovers over button.
        button_pressed_sound: Sound for when button is pressed.
        button_surface: Surface for button.
        button_rect: Button rectangle.
        button_text: Text for button.
        button_color: A dict list of color values for different button states. 
    """
    def __init__(self, x_pos, y_pos, width, height, text, font, sound_vol):
        """Button initialization.
        
        Args:
            x_pos: X position for button.
            y_pos: Y position for button.
            width: Width value for button.
            height: Height value for button.
            text: Text string for button.
            font: Text font for button.
            sound_vol: Game's sound volume value for button sounds.
        """
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.is_being_hovered = False
        self.is_pressed = False

        self.button_hover_sound = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "button.wav"))
        self.button_pressed_sound = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "buttonPressed.wav"))
        self.button_hover_sound.set_volume(sound_vol)
        self.button_pressed_sound.set_volume(sound_vol)

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_text = self.font.render(text, True, (25, 25, 25))

        self.button_color = {
            "unpressed": "#ff0000",
            "hovered": "#d66d6d"
        }

    def display(self, window, mouse, mouse_status, player):
        """Handles drawing button and button events.
        
        Args:
            window: Game's window.
            mouse: Mouse position.
            mouse_status: Defines if mouse button is held down.
            player: Not used here.
        
        Returns:
            Button text if button was pressed. Else it will return empty string.
        """
        if not mouse_status:
            Menu.already_pressed = False
        self.button_surface.fill(self.button_color["unpressed"])
        if self.button_rect.collidepoint(mouse):
            self.button_surface.fill(self.button_color["hovered"])
            if not self.is_being_hovered:
                self.is_being_hovered = True
                pygame.mixer.Sound.play(self.button_hover_sound)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.is_pressed and not Menu.already_pressed:
                    Menu.already_pressed = True
                    if self.text == "Asetukset":
                        window.fill((0, 0, 0))
                    if self.text == "Takaisin":
                        window.fill((0, 0, 0))
                    self.is_pressed = True
                    pygame.mixer.Sound.play(self.button_pressed_sound)
                    return self.text
                else:
                    return ""
            else:
                self.is_pressed = False
        else:
            self.is_being_hovered = False

        self.button_surface.blit(self.button_text, [self.button_rect.width/2 - self.button_text.get_rect(
        ).width/2, self.button_rect.height/2 - self.button_text.get_rect().height/2])
        window.blit(self.button_surface, self.button_rect)
        return ""

    def get_type(self):
        """Returns type of object.
        
        Returns:
            Returns name of object.
        """
        return "Button"


class Slider:
    """Slider object.
    
    Slider for changing settings.
    Attributes:
        x: Slider's x position.
        y: Slider's y position.
        x_circle: Slider's circle x position.
        width: Slider's width.
        height: Slider's height.
        type: Tells what is slider used for.
        value: Slider's value
        rect_slider: Slider's rectangle.
        rect_circle: Slider's circle.
        font: Slider's text font
        moved: Defines if slider's circle was moved.
        slider_moved: Sound for when slider's circle is moved.
    """
    def __init__(self, x_pos, y_pos, width, height, type, settings, first_init, sound_vol):
        """Slider initialization.
        
        Args:
            x_pos: X position for slider.
            y_pos: Y position for slder.
            width: Width value for slider.
            height: Height value for slider.
            type: Tells what slider is used for.
            settings: Game's settings
            first_init: Defines if this is slider's first initialization.
            sound_vol: Game's sound volume value.
        """
        self.x = x_pos
        self.y = y_pos
        self.x_circle = self.x
        self.width = width
        self.height = height
        self.type = type
        self.value = 1.0
        if first_init:
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
        self.slider_moved = pygame.mixer.Sound(
            os.path.join(dirname, "assets", "button.wav"))
        self.slider_moved.set_volume(sound_vol)

    def display(self, window, mouse, mouse_status, player):
        """Handles displaying and interaction of sliders.
        
        Args:
            window: Game's window.
            mouse: Mouse position.
            mouse_status: Defines if mouse button is held down.
            player: Not used here.
        """
        new_value = False
        collide = self.rect_slider.collidepoint(mouse)
        if collide and not mouse[0] < self.x and not mouse[0] > self.x+200:
            if mouse_status:
                self.x_circle = mouse[0]
                if not self.moved:
                    self.moved = True
                    pygame.mixer.Sound.play(self.slider_moved)
            else:
                if self.moved:
                    self.moved = False
                    pygame.mixer.Sound.play(self.slider_moved)
                    new_value = True
            self.value = abs(self.x-self.x_circle)
            self.value = round((self.value*100/self.width)/100, 1)

        self.x_circle = self.x+(20*(self.value*10))
        if self.type == "sound" or self.type == "music":
            value = self.value
            text = self.font.render(str(self.value), True, (255, 255, 255))
        if self.type == "resolution":
            value = self.get_value()
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

        if new_value:
            new_value = False
            return (self.type)

    def get_value(self):
        """Returns slider value."""
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

    def get_type(self):
        """Returns type of object.
        
        Returns:
            Returns name of object.
        """
        return "Slider"


class Icon:
    """Icon object.
    
    Used for displaying turrets that you can buy while
    being in construction mode.
    """
    def __init__(self, x_offset, y_offset, name):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.name = name
        self.font = pygame.font.SysFont("Arial", 20)

    def display(self, window, mouse, mouse_status, player):
        """Handles displaying and interaction of icons.
        
        Args:
            window: Game's window.
            mouse: Mouse position.
            mouse_status: Not used here.
            player: Player object.
            
        Returns:
            Icon name if icon was pressed.
        """
        command = ""
        scale = self.get_scale(window)
        x = (window.get_width()/2)+scale[0]*5+scale[0]
        y = (window.get_height()/2)-scale[1]*5
        if self.x_offset:
            x = (window.get_width()/2)+scale[0]*7+scale[0]
        if self.y_offset:
            y = (window.get_height()/2)-scale[1]*5+scale[1]
        rect = pygame.Rect(x, y, scale[0], scale[1])
        pygame.draw.rect(window, (255, 255, 255), (x, y, scale[0], scale[1]))
        turret = Turret(self.name, 1.0, window)
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

    def get_scale(self, window):
        """Gives scale based on window resolution and aspect ratio of resolution.
        
        Args:
            window: Game's window.
        """
        width = window.get_width()
        height = window.get_height()
        if width == 640 or width == 800 or width == 1024 or width == 1152 or (width == 1280 and height == 960):
            return ((width/40)*2, (height/30)*2)
        if (width == 1280 and height == 720) or width == 1366 or width == 1600 or width == 1920:
            return ((width/160)*8, (height/90)*8)
        else:
            return ((width/160)*8, (height/100)*8)

    def get_type(self):
        """Returns type of object.
        
        Returns:
            Returns name of object.
        """
        return "Icon"
