import os
import pygame


dirname = dirname = os.path.dirname(__file__)


class Turret:
    def __init__(self, name):
        self.name = name
        self.turret_sprite = self.import_sprite(self.name)
        self.ammo_sprite = self.import_sprite(self.name + "_ammo")
        self.reload_time = 0
        self.range = 0
        self.damage = 0
        self.cost = 0
        # Give reload time, range, damage and cost based on turret type
        self.give_rt_r_d_c(self.name)

    def import_sprite(self, name):
        png = []
        try:
            png = pygame.image.load(os.path.join(
                dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def give_rt_r_d_c(self, type):
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

    def add_turret(self, turret):
        self.turrets.append(turret)

    def remove_turret(self, turret):
        self.turrets.remove(turret)
