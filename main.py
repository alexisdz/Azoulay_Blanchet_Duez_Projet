import pygame             # Pygame pour créer le jeu
from game import Game     # Import de la classe Game

pygame.init() # Initialise Pygame

screen = pygame.display.set_mode((800, 600)) # Crée la fenêtre du jeu
game = Game(screen) # Crée une instance du jeu       

game.run() # Lance la boucle principale

pygame.quit() # Ferme Pygame à la fin
