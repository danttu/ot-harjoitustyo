import os
import pygame

dirname = dirname = os.path.dirname(__file__)


class Map:
    def __init__(self):
        self.sprites = self.import_sprites()
        self.map = self.new_map()

    def import_sprites(self):
        pngs = []
        for name in ["grass", "flower", "flowers", "dirt"]:
            try:
                pngs.append(pygame.image.load(
                    os.path.join(dirname, "assets", name + ".png")))
            except FileNotFoundError:
                print("You are missing: " + name + ".png")
        return pngs

    def new_map(self):
        map = [[0, 0, 3, 0, 0, 0, 2, 0, 1, 0],
               [0, 1, 3, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 3, 3, 3, 3, 3, 3, 3, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
               [3, 3, 3, 3, 3, 3, 3, 0, 3, 0],
               [0, 0, 0, 0, 0, 0, 3, 0, 3, 1],
               [0, 2, 1, 0, 3, 3, 3, 1, 3, 0],
               [0, 0, 0, 0, 3, 0, 0, 0, 3, 0],
               [0, 0, 2, 0, 3, 3, 3, 3, 3, 2],
               [1, 0, 0, 0, 0, 0, 2, 0, 2, 0]]
        return map

    def draw_map(self, window):
        scale = self.get_scale(window)
        x = (window.get_width()/2)-scale[0]*5  # pylint: disable=invalid-name
        y = (window.get_height()/2)-scale[1]*5  # pylint: disable=invalid-name
        i = 0
        j = 0
        while True:
            if j > 9:
                break
            if i > 9:
                i = 0
                j += 1
                x = (window.get_width()/2) - \
                    scale[0]*5  # pylint: disable=invalid-name
                y += scale[1]  # pylint: disable=invalid-name
                continue
            tile = self.map[j][i]
            scaled_tile = self.sprites[tile]
            scaled_tile = pygame.transform.scale(scaled_tile, scale)
            window.blit(scaled_tile, (x, y))
            x += scale[0] # pylint: disable=invalid-name
            i += 1
        pygame.display.update()

    def get_scale(self, window):
        width = window.get_width()
        height = window.get_height()
        # 4:3 aspect ratio
        if width == 640 or width == 800 or width == 1024 or width == 1152 or (width == 1280 and height == 960):
            return ((width/40)*2, (height/30)*2)
        # 16:9 aspect ratio
        if (width == 1280 and height == 720) or width == 1366 or width == 1600 or width == 1920:
            return ((width/160)*8, (height/90)*8)
        # 16:10 aspect ratio
        return ((width/160)*8, (height/100)*8)
