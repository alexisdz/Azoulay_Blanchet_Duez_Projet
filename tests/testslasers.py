import unittest
import pygame
from laser import Laser

pygame.init()

class TestLaser(unittest.TestCase):
    def setUp(self):
        # Position initiale (x=100, y=100), vitesse -8, écran de 600px de haut
        self.laser = Laser((100, 100), -8, 600)

    def test_initial_position(self):
        # Vérifie la position initiale et la vitesse
        self.assertEqual(self.laser.rect.center, (100, 100))
        self.assertEqual(self.laser.speed, -8)

    def test_update_movement(self):
        # Déplace le laser avec update() et vérifie la nouvelle position
        old_y = self.laser.rect.y
        self.laser.update()
        self.assertEqual(self.laser.rect.y, old_y + self.laser.speed)

    def test_destroy_above_screen(self):
        # Place le laser au-dessus de l'écran pour tester destroy
        self.laser.rect.y = -60
        self.laser.update()
        self.assertFalse(self.laser.alive())  # le laser doit être supprimé

    def test_destroy_below_screen(self):
        # Place le laser en dessous de l'écran pour tester destroy
        self.laser.rect.y = 660  # 600 + 50
        self.laser.update()
        self.assertFalse(self.laser.alive())

if __name__ == "__main__":
    unittest.main()
