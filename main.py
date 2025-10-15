import pygame            
from game import Game  
from player import Player  

pygame.init() 

# Instanciation d'une fenêtre et du jeu
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height)) 
game = Game(screen_width, screen_height)     

# Lancement du jeu
game.run() 

# Fermeture propre
pygame.quit()
