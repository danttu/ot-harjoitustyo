import os
import pygame


dirname = dirname = os.path.dirname(__file__)


class Enemy:
    def __init__(self, name, hp):  # pylint: disable=invalid-name
        self.name = name
        self.hp = hp  # pylint: disable=invalid-name
        self.sprite = self.import_sprite(self.name)

    def import_sprite(self, name):
        png = []
        try:
            png = pygame.image.load(os.path.join(
                dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def check_enemy_hp(self):
        if self.hp <= 0:
            return True
        return False


class Enemies:
    def __init__(self):
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def check_enemy_hp(self):
        for enemy in self.enemies:
            if enemy.check_enemy_hp(enemy) == True:
                self.remove_enemy(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)


# Debug
enemies = Enemies()
print(enemies.enemies)
enemy = Enemy("cannon", 100)
enemies.add_enemy(enemy)
