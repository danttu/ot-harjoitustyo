from turrets import Turrets
from turrets import Turret


class Player:
    def __init__(self):
        self.health = 250  
        self.money = 1000  # pylint: disable=invalid-name
        # Current round limit is 250,
        # after that enemies have too much speed that they get stuck
        self.current_round = 1
        self.destroyed_enemies = 0
        self.turrets = Turrets()

    def add_money(self, amount):
        # If negative, change to zero
        amount = max(amount, 0)
        self.money += amount

    def remove_money(self, amount):
        # If negative, change to zero
        amount = max(amount, 0)
        # If amount is bigger than amount that player has, do not allow to take money
        # (in this case do not allow player to buy turrets or upgrades)
        if self.money < amount:
            return False
        self.money -= amount
        return True

    def buy_turret(self, turret_name, sound_vol, window):
        turret = Turret(turret_name, sound_vol, window)
        #if money removal is successful add turret to player owned turrets and return True
        if self.remove_money(turret.cost):
            self.turrets.add_turret(turret)
            return True
        return False

    def take_hit(self, hitpoints):
        # If negative, change to zero
        hitpoints = max(hitpoints, 0)
        # If damage is bigger than or same as player's health, make player's health to zero
        # and return True for gameOver check
        if self.health <= hitpoints:
            self.health = 0  
            return True
        self.health -= hitpoints
        return False

    def get_current_round(self):
        return self.current_round
    
    def get_money(self):
        return self.money
    
    def get_health(self):
        return self.health
    
    def add_destroyed_enemy(self):
        self.destroyed_enemies += 1

    def get_destroyed_enemies(self):
        return self.destroyed_enemies

    def next_round(self):
        self.current_round += 1
