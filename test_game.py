import unittest
import pygame
from game import Game
from enemy import Enemy
from laser import Laser

class TestGame(unittest.TestCase):
    def setUp(self):
        """Initialisation du jeu pour chaque test"""
        pygame.init()
        self.game = Game(800, 600)

    def tearDown(self):
        pygame.quit()

    def test_initial_values(self):
        """Test des valeurs initiales du jeu"""
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.lives, 3)
        self.assertTrue(self.game.running)

    def test_enemy_hit_increases_score(self):
        """Test : le score augmente quand un ennemi est détruit"""
        # On vide les ennemis initiaux
        self.game.enemies.empty()

        # Création d'un ennemi et d'un laser sur sa position
        enemy = Enemy((100, 100), self.game.screen_width, "bruh")
        self.game.enemies.add(enemy)
        laser = Laser(enemy.rect.center, -6, self.game.screen_height)
        self.game.player.sprite.lasers.add(laser)

        self.game.collision_checks()

        # Vérifie que le score a augmenté et que le groupe est vide
        self.assertEqual(self.game.score, 100)
        self.assertEqual(len(self.game.enemies), 0)

    def test_extra_hit_increases_score_more(self):
        """Test : le score augmente davantage avec un ennemi extra"""
        # On vide les ennemis normaux
        self.game.enemies.empty()
        self.game.extra.empty()

        extra_enemy = Enemy((150, 100), self.game.screen_width, "extra")
        self.game.extra.add(extra_enemy)
        laser = Laser(extra_enemy.rect.center, -6, self.game.screen_height)
        self.game.player.sprite.lasers.add(laser)

        self.game.collision_checks()

        self.assertEqual(self.game.score, 1000)
        self.assertEqual(len(self.game.extra), 0)

    def test_player_hit_reduces_life(self):
        """Test : une collision laser-joueur réduit les vies"""
        laser = Laser(self.game.player.sprite.rect.center, 6, self.game.screen_height)
        self.game.enemy_lasers.add(laser)

        self.game.collision_checks()

        self.assertEqual(self.game.lives, 2)

    def test_game_over_when_no_lives_left(self):
        """Test : le jeu s'arrête quand les vies tombent à 0"""
        self.game.lives = 1
        laser = Laser(self.game.player.sprite.rect.center, 6, self.game.screen_height)
        self.game.enemy_lasers.add(laser)

        self.game.collision_checks()

        self.assertFalse(self.game.running)

if __name__ == "__main__":
    unittest.main()
