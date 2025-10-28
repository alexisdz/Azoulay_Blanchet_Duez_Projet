import pygame    
from game import Game

pygame.init()

# Instanciation d'une fenêtre et du jeu
screen_width = 800
screen_height = 800
game = Game(screen_width, screen_height)

# Son d'intro
game.play_intro()

# Affichage de l'écran d'accueil
game.show_menu()

# Lancement du jeu
game.run()

# Fermeture propre
pygame.quit()
