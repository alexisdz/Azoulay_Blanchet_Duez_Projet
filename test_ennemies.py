import unittest
import pygame
from game import Game

pygame.init()

class TestGameEnemies(unittest.TestCase):
    def setUp(self):
        self.game = Game(800, 600)

    def test_enemy_creation(self):
        self.assertEqual(len(self.game.enemies), 6 * 8)  # 48 ennemis créés

    def test_enemy_direction_change(self):
        # on simule un ennemi qui touche le bord droit
        enemy = list(self.game.enemies)[0]
        enemy.rect.right = self.game.screen_width - 5
        self.game.enemy_position_checker()
        self.assertEqual(self.game.enemy_direction, -1)

if __name__ == "__main__":
    unittest.main()
