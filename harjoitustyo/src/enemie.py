import pygame
import os

dirname = dirname = os.path.dirname(__file__)

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.sprite = self.importSprite(self.name)

    def importSprite(self, name):
        png = []
        try:
            png = pygame.image.load(os.path.join(dirname, "assets", name + ".png"))
        except FileNotFoundError:
            print("You are missing: " + name + ".png")
        return png

    def checkEnemyHp(self):
        if self.hp <= 0:
            return True
        else:
            return False

class Enemies:
    def __init__(self):
        self.enemies = []

    def addEnemie(self, enemie):
        self.enemies.append(enemie)

    def checkEnemyHp(self):
        for enemy in self.enemies:
            if Enemy.checkEnemyHp(enemy) == True:
                self.remove_enemy(enemy)
    
    def removeEnemy(self, enemy):
        self.enemies.remove(enemy)

#Debug
enemies = Enemies()
print(enemies.enemies)
enemy = Enemy("cannon", 100)
enemies.addEnemie(enemy)
