import unittest
import pygame
from player import Player

pygame.init()

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.screen_width = 800
        self.screen_height = 600
        # On utilise les mêmes valeurs que dans Game
        self.player = Player((self.screen_width / 2, self.screen_height), self.screen_width)

    def test_initial_position(self):
        self.assertEqual(self.player.rect.midbottom, (self.screen_width / 2, self.screen_height))

    def test_constraint_left(self):
        self.player.rect.x = -10
        self.player.constraint()
        self.assertEqual(self.player.rect.left, 0)

    def test_constraint_right(self):
        self.player.rect.x = 810
        self.player.constraint()
        self.assertEqual(self.player.rect.right, self.screen_width)

if __name__ == "__main__":
    unittest.main()
