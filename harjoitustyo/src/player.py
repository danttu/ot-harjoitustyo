from turrets import Turrets
from turrets import Turret


class Player:
    """Information about player.
    
    Args:
        health: Amount of hitpoints that player's base has.
        money: Amount of money that player has.
        current_round: Current round of game.
        destroyed_enemies: Amount of enemies destroyed.
        turrets: List of turrets that player owns.
    """
    def __init__(self):
        """Player initialization."""
        self.health = 250  
        self.money = 1000  # pylint: disable=invalid-name
        self.current_round = 1
        self.destroyed_enemies = 0
        self.turrets = Turrets()

    def add_money(self, amount):
        """Adds given amount to player's money if valid amount.
        
        Args:
            amount: Amount of money to be given.
        """
        amount = max(amount, 0)
        self.money += amount

    def remove_money(self, amount):
        """Removes given amount from player's money if valid amount.
        
        Args:
            amount: Amount of money to be taken.
            
        Returns:
            True if amount is not bigger than player's money amount. Else returns false.
            Used for checking if player was able to purchase turret.
        """
        amount = max(amount, 0)
        if self.money < amount:
            return False
        self.money -= amount
        return True

    def buy_turret(self, turret_name, sound_vol, window):
        """Attempt to buy turret with player's money.
        
        Args:
            turret_name: Name of turret that is being bought.
            sound_vol: Game's sound volume value.
            window: Game's window.
        
        Returns:
            True if remove_money() with cost of turret returned true. Else returns false. 
        """
        turret = Turret(turret_name, sound_vol, window)
        if self.remove_money(turret.cost):
            self.turrets.add_turret(turret)
            return True
        return False

    def take_hit(self, hitpoints):
        """Subtract player health.
        
        Args:
            hitpoints: Amount of hitpoints.
        
        Returns:
            True if hitpoints are bigger that player's current health. Else returns false.
            Used for game over check.
        """
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
        """Gives game's current round."""
        return self.current_round
    
    def get_money(self):
        """Gives player's current amount of money."""
        return self.money
    
    def get_health(self):
        """Gives player's current amount of health"""
        return self.health
    
    def add_destroyed_enemy(self):
        """Adds one to destroyed enemies counter."""
        self.destroyed_enemies += 1

    def get_destroyed_enemies(self):
        """Gives current amount of destroyed enemies."""
        return self.destroyed_enemies

    def next_round(self):
        """Advances by one round."""
        self.current_round += 1
