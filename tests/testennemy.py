import unittest
import pygame
from enemy import Enemy

pygame.init()

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.screen_width = 800
        self.enemy = Enemy((100, 100), self.screen_width, 'blublu')

    def test_initial_position(self):
        self.assertEqual(self.enemy.rect.topleft, (100, 100))

    def test_move_right(self):
        start_x = self.enemy.rect.x
        self.enemy.update(1)  # direction vers la droite
        self.assertGreater(self.enemy.rect.x, start_x)

    def test_move_left(self):
        start_x = self.enemy.rect.x
        self.enemy.update(-1)  # direction vers la gauche
        self.assertLess(self.enemy.rect.x, start_x)

if __name__ == "__main__":
    unittest.main()
