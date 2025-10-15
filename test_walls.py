import unittest
import pygame
from walls import Wall

pygame.init()
pygame.display.set_mode((1, 1))

class TestWall(unittest.TestCase):
    def setUp(self):
        self.wall = Wall(100, 200)

    def test_initial_state(self):
        """Vérifie la position et la vie initiale du mur"""
        self.assertEqual(self.wall.rect.topleft, (100, 200))
        self.assertEqual(self.wall.life, 5)

    def test_update_reduces_life(self):
        """Vérifie que la méthode update() réduit la vie du mur"""
        old_life = self.wall.life
        self.wall.update()
        self.assertEqual(self.wall.life, old_life - 1)

    def test_wall_destroyed_when_life_zero(self):
        """Vérifie que le mur est détruit quand la vie atteint zéro"""
        self.wall.life = 1
        self.wall.update()
        self.assertFalse(self.wall.alive())

    def test_draw_no_crash(self):
        """Vérifie que draw() fonctionne sans erreur"""
        screen = pygame.Surface((800, 600))
        try:
            self.wall.draw(screen)
        except Exception as e:
            self.fail(f"draw() a levé une exception : {e}")

if __name__ == "__main__":
    unittest.main()
