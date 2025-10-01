import pygame    
from game import Game

pygame.init()

# Instanciation d'une fenêtre et du jeu
screen_width = 800
screen_height = 600
game = Game(screen_width, screen_height)

# Lancement du jeu
game.run()

# Fermeture propre
pygame.quit()
