import pygame
import os

dirname = dirname = os.path.dirname(__file__)

class Turret:
    def __init__(self, name):
        self.name = name
        self.sprite = self.importSprite(self.name)
        self.reload_time = 0
        self.range = 0
        self.damage = 0
        self.cost = 0
        #Give reload time, range, damage and cost based on turret type
        self.giveRtRDC(self.name)

    def importSprites(self):
        pngs = []
        for name in ["cannon", "cannon_ammo", "minigun", "minigun_ammo"]:
            try:
                pngs.append(pygame.image.load(os.path.join(dirname, "assets", name + ".png")))
            except FileNotFoundError:
                print("You are missing: " + name + ".png")
        return pngs
    
    def giveRtRDC(self, type):
        if type == "cannon":
            self.reload_time = 5
            self.range = 5
            self.damage = 75
            self.cost = 100
        if type == "minigun":
            self.reload_time = 1
            self.range = 10
            self.damage = 10
            self.cost = 250

class Turrets:
    def __init__(self):
        self.turrets = []
    
    def addTurret(self, turret):
        self.turrets.append(turret)

    def removeTurret(self, turret):
        self.turrets.remove(turret)
    