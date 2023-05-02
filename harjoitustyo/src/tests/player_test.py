import unittest
from player import Player

class TestMain(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        
    def test_player_class_works(self):
        # Check if when creating player it has correct values
        player = Player()
        health = player.health
        money = player.money
        current_round = player.current_round
        amount_of_turrets = len(player.turrets.turrets)
        self.assertEqual(health, 250)
        self.assertEqual(money, 1000)
        self.assertEqual(current_round, 1)
        self.assertEqual(amount_of_turrets, 0)

    def test_turret_add(self):
        pass
    def test_add_money(self):
        # Test with positive value
        self.player.add_money(100)
        self.assertEqual(self.player.money, 1100)
        # Test with negative value (converts negative to zero)
        self.player.add_money(-100)
        self.assertEqual(self.player.money, 1100)
    def test_remove_money(self):
        # Test with positive value
        self.player.remove_money(100)
        self.assertEqual(self.player.money, 900)
        self.assertTrue(self.player.remove_money(100))
        # Test with negative value (converts negative to zero)
        self.player.add_money(-100)
        self.assertEqual(self.player.money, 800)
        self.assertFalse(self.player.remove_money(1000))
    def test_buy_turret(self):
        for _ in range(0, 3):
            self.player.buy_turret("minigun")
        self.assertTrue(self.player.buy_turret("minigun"))
        # Try to buy when not enough money
        self.assertFalse(self.player.buy_turret("minigun"))
    def test_take_hit(self):
        # Test with negative value (converts negative to zero)
        self.player.take_hit(-100)
        self.assertEqual(self.player.health, 250)
        # Test with positive value
        self.player.take_hit(100)
        self.assertEqual(self.player.health, 150)
        self.assertFalse(self.player.take_hit(100))
        self.assertTrue(self.player.take_hit(50))
    def test_get_current_round(self):
        current_round = self.player.get_current_round()
        self.assertEqual(current_round, 1)
    def test_get_money(self):
        money = self.player.get_money()
        self.assertEqual(money, 1000)
    def test_get_health(self):
        health = self.player.get_health()
        self.assertEqual(health, 250)
    def test_next_round(self):
        self.player.next_round()
        self.assertEqual(self.player.current_round, 2)