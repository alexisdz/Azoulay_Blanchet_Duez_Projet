import pygame            
from game import Game    

pygame.init() 

# Instanciation d'une fenêtre et du jeu
screen = pygame.display.set_mode((800, 600)) 
game = Game(screen)     

# Lancement du jeu
game.run() 

# Fermeture propre
pygame.quit()
