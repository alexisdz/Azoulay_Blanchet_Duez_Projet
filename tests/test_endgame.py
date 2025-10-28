import unittest
from unittest.mock import patch
import pygame
from game import Game
from enemy import Enemy

class TestEndScreen(unittest.TestCase):
    def setUp(self):
        pygame.init()          # initialise tous les modules (incluant font)
        pygame.font.init()     # optionnel mais sûr pour la font
        self.game = Game(800, 600)

    def tearDown(self):
        pygame.quit()

    @patch.object(Game, 'end_screen')
    def test_victory(self, mock_end_screen):
        self.game.enemies.empty()  # plus d'ennemis
        self.game.check_game_over()
        mock_end_screen.assert_called_once_with(victory=True)

    @patch.object(Game, 'end_screen')
    def test_game_over_lives(self, mock_end_screen):
        self.game.lives = 0
        self.game.check_game_over()
        mock_end_screen.assert_called_once_with(victory=False)

    @patch.object(Game, 'end_screen')
    def test_game_over_enemy_hit_player(self, mock_end_screen):
        # Placer un ennemi sur le joueur
        enemy = Enemy((self.game.player.sprite.rect.x, self.game.player.sprite.rect.y), self.game.screen_width, 'bruh')
        self.game.enemies.add(enemy)
        self.game.check_game_over()
        mock_end_screen.assert_called_once_with(victory=False)

if __name__ == "__main__":
    unittest.main()
