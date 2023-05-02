import unittest
from settings import Settings

class TestMain(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
    
    def test_init(self):
        #Test __init__()
        music = self.settings.music_vol
        sound = self.settings.sound_vol
        fps = self.settings.framerate
        res_x = self.settings.resolution_x
        res_y = self.settings.resolution_y

        self.assertEqual(music, 1.0)
        self.assertEqual(sound, 1.0)
        self.assertEqual(fps, 60)
        self.assertEqual(res_x, 1280)
        self.assertEqual(res_y, 720)

    def test_set_volume(self):
        self.settings.set_volume(0.5, 0.4)
        self.assertEqual(self.settings.music_vol, 0.5)
        self.assertEqual(self.settings.sound_vol, 0.4)
        self.settings.set_volume(2.5, 3.4)
        self.assertEqual(self.settings.music_vol, 1.0)
        self.assertEqual(self.settings.sound_vol, 1.0)
        self.settings.set_volume(-2.5, -3.4)
        self.assertEqual(self.settings.music_vol, 0.0)
        self.assertEqual(self.settings.sound_vol, 0.0)
        
    def test_set_framerate(self):
        self.settings.set_framerate(70)
        self.assertEqual(self.settings.framerate, 70)
        self.settings.set_framerate(-1)
        self.assertEqual(self.settings.framerate, 24)
    def test_set_resolution(self):
        self.settings.set_resolution((1920, 1080))
        self.assertEqual(self.settings.resolution_x, 1920)
        self.assertEqual(self.settings.resolution_y, 1080)
    def test_get_volume(self):
        volume = self.settings.get_volume()
        self.assertEqual(volume, (1.0, 1.0))
    def test_get_framerate(self):
        fps = self.settings.get_framerate()
        self.assertEqual(fps, 60)
    def test_get_resolutuion(self):
        resolution = self.settings.get_resolution()
        self.assertEqual(resolution, (1280, 720))