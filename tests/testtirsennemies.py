import unittest
import pygame
from game import Game
from player import Player
from enemy import Enemy, Extra
from laser import Laser
from walls import Wall

pygame.init()

class TestLasers(unittest.TestCase):

    def setUp(self):
        self.screen_width = 800
        self.screen_height = 600
        self.game = Game(self.screen_width, self.screen_height)

        # Créer un mur de test
        self.wall = Wall(400, 300)
        self.game.walls.add(self.wall)

        # Créer un ennemi pour tester collision
        self.enemy = Enemy((200, 200), self.screen_width)
        self.game.enemies.add(self.enemy)

        # Créer un ennemi extra pour tester collision
        self.extra = Extra('left', self.screen_width)
        self.game.extra.add(self.extra)

        # Laser du joueur pour collision
        self.laser_player = Laser((200, 250), 5, self.screen_height)
        self.game.player.sprite.lasers.add(self.laser_player)

        # Laser ennemi pour collision
        if not hasattr(self.game, 'enemy_lasers'):
            self.game.enemy_lasers = pygame.sprite.Group()
        self.laser_enemy = Laser((400, 350), 5, self.screen_height)
        self.game.enemy_lasers.add(self.laser_enemy)

    def test_player_laser_hits_enemy(self):
        """Test que le laser du joueur détruit un ennemi"""
        self.game.collision_checks()
        self.assertNotIn(self.enemy, self.game.enemies)
        self.assertNotIn(self.laser_player, self.game.player.sprite.lasers)

    def test_player_laser_hits_extra(self):
        """Test que le laser du joueur détruit l'ennemi extra"""
        # Déplacer le laser sur l'Extra
        self.laser_player.rect.center = self.extra.rect.center
        self.game.collision_checks()
        self.assertNotIn(self.extra, self.game.extra)
        self.assertNotIn(self.laser_player, self.game.player.sprite.lasers)

    def test_player_laser_hits_wall(self):
        """Test que le laser du joueur abîme le mur"""
        # Déplacer le laser sur le mur
        self.laser_player.rect.center = self.wall.rect.center
        initial_health = getattr(self.wall, 'health', 1)
        self.game.collision_checks()
        self.assertNotIn(self.laser_player, self.game.player.sprite.lasers)
        self.assertTrue(getattr(self.wall, 'health', 0) < initial_health)

    def test_enemy_laser_hits_wall(self):
        """Test que le laser ennemi abîme le mur"""
        # Déplacer le laser sur le mur
        self.laser_enemy.rect.center = self.wall.rect.center
        initial_health = getattr(self.wall, 'health', 1)
        self.game.collision_checks()
        self.assertNotIn(self.laser_enemy, self.game.enemy_lasers)
        self.assertTrue(getattr(self.wall, 'health', 0) < initial_health)

    def test_enemy_laser_hits_player(self):
        """Test que le laser ennemi touche le joueur et met fin au jeu"""
        # Déplacer le laser sur le joueur
        self.laser_enemy.rect.center = self.game.player.sprite.rect.center
        self.game.collision_checks()
        self.assertNotIn(self.laser_enemy, self.game.enemy_lasers)
        self.assertFalse(self.game.running)

if __name__ == '__main__':
    unittest.main()
