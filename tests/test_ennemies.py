import unittest
import pygame
from game import Game
from laser import Laser # Assurez-vous que Laser peut être importé
from enemy import Extra # Assurez-vous que Extra peut être importé

pygame.init()

class TestGameEnemies(unittest.TestCase):
    def setUp(self):
        """Cette méthode est appelée avant chaque test."""
        self.game = Game(800, 600)

    def test_enemy_creation(self):
        """Vérifie que le nombre correct d'ennemis est créé au départ."""
        self.assertEqual(len(self.game.enemies), 6 * 8)  # 48 ennemis créés

    def test_enemy_direction_change_right_wall(self):
        """Teste si la direction des ennemis change lorsqu'un ennemi touche le bord droit."""
        # On simule un ennemi qui touche le bord droit
        enemy = list(self.game.enemies)[0]
        enemy.rect.right = self.game.screen_width # On le place directement sur le bord
        self.game.enemy_position_checker()
        self.assertEqual(self.game.enemy_direction, -1, "La direction devrait être -1 (gauche)")

    def test_enemy_direction_change_left_wall(self):
        """Teste si la direction des ennemis change lorsqu'un ennemi touche le bord gauche."""
        self.game.enemy_direction = -1 # Simule le mouvement vers la gauche
        enemy = list(self.game.enemies)[0]
        enemy.rect.left = 0 # On le place sur le bord gauche
        self.game.enemy_position_checker()
        self.assertEqual(self.game.enemy_direction, 1, "La direction devrait être 1 (droite)")

    def test_enemies_move_down_on_hit(self):
        """Vérifie que tous les ennemis descendent quand un bord est touché."""
        initial_y_positions = [enemy.rect.y for enemy in self.game.enemies]
        
        # On simule un ennemi qui touche le bord droit
        enemy_touching_wall = list(self.game.enemies)[0]
        enemy_touching_wall.rect.right = self.game.screen_width
        
        # Appel de la fonction qui doit déclencher la descente
        self.game.enemy_position_checker()
        
        # Vérification
        for i, enemy in enumerate(self.game.enemies):
            # Chaque ennemi doit avoir descendu de 2 pixels
            self.assertEqual(enemy.rect.y, initial_y_positions[i] + 2)

    def test_laser_enemy_collision(self):
        """Teste la collision entre un laser du joueur et un ennemi."""
        # On prend un ennemi comme cible
        target_enemy = list(self.game.enemies)[0]
        
        # On crée un laser à la position de l'ennemi
        laser = Laser(target_enemy.rect.center, -8, self.game.screen_height)
        self.game.player.sprite.lasers.add(laser)
        
        # On vérifie l'état avant la collision
        self.assertEqual(len(self.game.enemies), 48)
        self.assertEqual(len(self.game.player.sprite.lasers), 1)

        # On exécute la vérification des collisions
        self.game.collision_checks()

        # On vérifie que l'ennemi et le laser ont été détruits
        self.assertEqual(len(self.game.enemies), 47)
        self.assertEqual(len(self.game.player.sprite.lasers), 0)

    def test_extra_enemy_spawn(self):
        """Vérifie que l'ennemi 'extra' apparaît lorsque son timer arrive à zéro."""
        self.assertEqual(len(self.game.extra), 0) # Au début, il n'y a pas d'ennemi extra
        
        # On force le timer à 1 pour qu'il se déclenche au prochain appel
        self.game.extra_spawn_time = 1
        self.game.extra_enemy_timer() # Appel de la fonction de spawn

        self.assertEqual(len(self.game.extra), 1, "Un ennemi extra aurait dû apparaître")

    def test_laser_extra_collision(self):
        """Teste la collision entre un laser et l'ennemi 'extra'."""
        # On fait apparaître un ennemi extra manuellement
        extra_enemy = Extra('left', self.game.screen_width)
        self.game.extra.add(extra_enemy)
        
        # On crée un laser à sa position
        laser = Laser(extra_enemy.rect.center, -8, self.game.screen_height)
        self.game.player.sprite.lasers.add(laser)

        self.assertEqual(len(self.game.extra), 1)
        self.assertEqual(len(self.game.player.sprite.lasers), 1)

        self.game.collision_checks()

        self.assertEqual(len(self.game.extra), 0, "L'ennemi extra aurait dû être détruit")
        self.assertEqual(len(self.game.player.sprite.lasers), 0, "Le laser aurait dû être détruit")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)