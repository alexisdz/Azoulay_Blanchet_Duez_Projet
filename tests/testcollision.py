import unittest
import pygame
from player import Player
from enemy import Enemy
from laser import Laser

pygame.init()

class TestCollision(unittest.TestCase):
    def setUp(self):
        self.screen_width = 800
        self.screen_height = 600
        self.player = Player((self.screen_width / 2, self.screen_height), self.screen_width)
        self.enemy = Enemy((400, 300), self.screen_width, 'blublu')
        self.laser = Laser((400, 300), 5, self.screen_height)

    def test_laser_enemy_collision(self):
        # simulate collision
        collision = pygame.sprite.collide_rect(self.laser, self.enemy)
        self.assertTrue(collision)

    def test_laser_no_collision(self):
        self.laser.rect.y = 0
        self.enemy.rect.y = 500
        collision = pygame.sprite.collide_rect(self.laser, self.enemy)
        self.assertFalse(collision)

if __name__ == "__main__":
    unittest.main()
