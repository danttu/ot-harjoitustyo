
class Settings:
    def __init__(self):
        self.music_vol: 1.0
        self.sound_vol: 1.0
        self.framerate: 60
        self.resolutionX: 1280
        self.resolutionY: 720
    
    # Set music and sound volume. Takes floats between 0.0 (0 %) and 1.0 (100%)
    def setVolume(self, music: float, sound: float):
        if music > 1.0:
            music = 1.0
        if music < 0.0:
            music = 0.0
        if sound > 1.0:
            sound = 1.0
        if sound < 0.0:
            sound = 0.0
        self.music_vol = music
        self.sound_vol = sound

    # Set framerate
    def setFramerate(self, fps: int):
        if fps < 0:
            fps = 24
        self.framerate = fps

    # Set window resolution
    def setResolution(self, x: int, y: int):
        if x < 640:
            x = 640
        if y < 480:
            y = 480
        self.resolutionX = x
        self.resolutionY = y
