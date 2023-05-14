class Settings:
    """Game settings.
    
    Contains sound and music volume, framrate and window resolution.
    
    Args:
        music_vol: Music volume. Takes floats between 0.0 (0 %) and 1.0 (100%).
        sound_vol: Sound volume. Takes floats between 0.0 (0 %) and 1.0 (100%).
        framerate: Frames per second.
        resolution_x: Window width.
        resolution_y: Window height.
    """
    def __init__(self):
        """Settings initialization."""
        self.music_vol = 1.0
        self.sound_vol = 1.0
        self.framerate = 60
        self.resolution_x = 1280
        self.resolution_y = 720
        self.check_if_file_exists()
        self.read_settings()

    def check_if_file_exists(self):
        """Checks if settings.ini is found."""
        try:
            with open("settings.ini") as settings:
                settings.close()
        except FileNotFoundError:
            with open("settings.ini", "w") as settings:
                settings.write(f"music_vol: {self.music_vol}\n")
                settings.write(f"sound_vol: {self.sound_vol}\n")
                settings.write(f"framerate: {self.framerate}\n")
                settings.write(f"resolution_x: {self.resolution_x}\n")
                settings.write(f"resolution_y: {self.resolution_y}\n")
                settings.close()
    
    def change_file_values(self):
        """Changes values in settings.ini."""
        with open("settings.ini", "w") as settings:
            settings.write(f"music_vol: {self.music_vol}\n")
            settings.write(f"sound_vol: {self.sound_vol}\n")
            settings.write(f"framerate: {self.framerate}\n")
            settings.write(f"resolution_x: {self.resolution_x}\n")
            settings.write(f"resolution_y: {self.resolution_y}\n")
            settings.close()

    def read_settings(self):
        """Reads and applies values from settings.ini to attributes."""
        music_vol = 0
        sound_vol = 0
        framerate = 0
        resolution_x = 0
        resolution_y = 0
        with open("settings.ini", "r") as settings:
            for row in settings:
                row = row.replace("\n", "")
                value = self.read_row(row)
                if value[0] == "music_vol":
                    music_vol = float(value[1])
                if value[0] == "sound_vol":
                    sound_vol = float(value[1])
                if value[0] == "framerate":
                    framerate = int(value[1])
                if value[0] == "resolution_x":
                    resolution_x = int(value[1])
                if value[0] == "resolution_y":
                    resolution_y = int(value[1])
            settings.close()
        self.set_volume(music_vol, sound_vol)
        self.set_framerate(framerate)
        self.set_resolution((resolution_x, resolution_y))

    def read_row(self, row):
        """Reads row and returns it for applying values to attributes.

        Args:
            row: Settings.ini row.

        Returns:
            Attribute and its value.
        """
        print(row)
        attribute = ""
        value = ""
        i = 0
        word = ""
        for sign in row:
            if sign == ":":
                if i == 0:
                    attribute = word
                    i += 1
                    word = ""
                    continue
            word += sign
        value = word
        value.replace(" ", "")
        return (attribute, value)

    def set_volume(self, music: float, sound: float):
        """Sets sound and music volume.
        
        Attributes:
            music: Music volume.
            sound: Sound volume.
        """
        music = min(music, 1.0)
        music = max(music, 0.0)
        sound = min(sound, 1.0)
        sound = max(sound, 0.0)
        self.music_vol = music
        self.sound_vol = sound

    def set_framerate(self, fps: int):
        """Sets framerate.
        
        Attributes:
            fps: Frames per second.
        """
        if fps < 0:
            fps = 24
        self.framerate = fps

    def set_resolution(self, res: tuple):
        """Sets window resolution.
        
        Attributes:
            res: Window resolution in tuple form.
        """
        x = res[0]  # pylint: disable=invalid-name
        y = res[1]  # pylint: disable=invalid-name
        x = max(x, 640)  # pylint: disable=invalid-name
        y = max(y, 480)  # pylint: disable=invalid-name
        self.resolution_x = x  # pylint: disable=invalid-name
        self.resolution_y = y  # pylint: disable=invalid-name

    def get_volume(self):
        """Gives values for music volume and sound volume in tuple form."""
        return (self.music_vol, self.sound_vol)

    def get_framerate(self):
        """Gives value for framerate."""
        return self.framerate

    def get_resolution(self):
        """Gives value for resoluion in tuple form."""
        return (self.resolution_x, self.resolution_y)
