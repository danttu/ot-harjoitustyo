import pygame
import os

dirname = dirname = os.path.dirname(__file__)

class Map:
    def __init__(self):
        self.sprites = self.importSprites()
        self.map = self.newMap()
    
    def importSprites(self):
        pngs = []
        for name in ["grass", "flower", "flowers", "dirt"]:
            try:
                pngs.append(pygame.image.load(os.path.join(dirname, "assets", name + ".png")))
            except FileNotFoundError:
                print("You are missing: " + name + ".png")
        return pngs
    def newMap(self):
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
    
    def drawMap(self, window):
        x = window.get_width()/4
        y = 40
        i = 0
        j = 0
        while True:
            if j > 9:
                break
            if i > 9:
                i = 0
                j += 1
                x = window.get_width()/4
                y += 64
                continue
            tile = self.map[j][i]
            scaled_tile = self.sprites[tile]
            scaled_tile = pygame.transform.scale(scaled_tile, (64, 64))
            window.blit(scaled_tile, (x, y))
            x += 64
            i += 1
        pygame.display.update()
