import pygame    
from game import Game

# Initialisation de Pygame (nécessaire pour tout ce qui concerne l'affichage et le son)
pygame.init()

# Dimensions de la fenêtre de jeu
screen_width = 800
screen_height = 800

# Création de l'objet Game qui gère tout le jeu
game = Game(screen_width, screen_height)

# Lecture de l'intro sonore au lancement
game.play_intro()

# Affichage du menu principal (options "Jouer" ou "Quitter")
game.show_menu()

# Lancement de la boucle principale du jeu
game.run()

# Fermeture propre de Pygame après la fin du jeu
pygame.quit()
