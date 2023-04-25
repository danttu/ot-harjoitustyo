from turrets import Turrets


class Player:
    def __init__(self):
        self.hp = 250  # pylint: disable=invalid-name
        self.money = 100  # pylint: disable=invalid-name
        self.current_round = 1
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

    def take_hit(self, hitpoints):
        # If negative, change to zero
        hitpoints = max(hitpoints, 0)
        # If damage is bigger than players hp, make player's hp to zero
        # and return True for gameOver check
        if self.hp < hitpoints:
            self.hp = 0  # pylint: disable=invalid-name
            return True
        self.hp -= hitpoints
        return False

    def get_current_round(self):
        return self.current_round

    def next_round(self):
        self.current_round += 1
