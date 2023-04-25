class Settings:
    def __init__(self):
        self.music_vol = 1.0
        self.sound_vol = 1.0
        self.framerate = 60
        self.resolution_x = 1280
        self.resolution_y = 720
        # Set music and sound volume. Takes floats between 0.0 (0 %) and 1.0 (100%)

    def set_volume(self, music: float, sound: float):
        music = min(music, 1.0)
        music = max(music, 0.0)
        sound = min(sound, 1.0)
        sound = max(sound, 0.0)
        self.music_vol = music
        self.sound_vol = sound

    # Set framerate
    def set_framerate(self, fps: int):
        if fps < 0:
            fps = 24
        self.framerate = fps

    # Set window resolution
    def set_resolution(self, res: tuple):
        x = res[0]  # pylint: disable=invalid-name
        y = res[1]  # pylint: disable=invalid-name
        x = max(x, 640)  # pylint: disable=invalid-name
        y = max(y, 480)  # pylint: disable=invalid-name
        self.resolution_x = x  # pylint: disable=invalid-name
        self.resolution_y = y  # pylint: disable=invalid-name

    def get_volume(self):
        return (self.music_vol, self.sound_vol)

    def get_framerate(self):
        return self.framerate

    def get_resolution(self):
        return (self.resolution_x, self.resolution_y)
