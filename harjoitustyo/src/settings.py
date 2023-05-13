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

    def set_volume(self, music: float, sound: float):
        """Sets sound and music volume"""
        music = min(music, 1.0)
        music = max(music, 0.0)
        sound = min(sound, 1.0)
        sound = max(sound, 0.0)
        self.music_vol = music
        self.sound_vol = sound

    def set_framerate(self, fps: int):
        """Sets framerate"""
        if fps < 0:
            fps = 24
        self.framerate = fps

    def set_resolution(self, res: tuple):
        """Sets window resolution"""
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
