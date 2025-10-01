import pygame
from player import Player
from walls import Wall

class Game:
    # Initialisation du jeu
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))               # Surface d'affichage
        self.running = True                # État du jeu
        self.clock = pygame.time.Clock()   # Gestion du temps
        self.player = Player( (screen_width / 2,screen_height), screen_width)         # Création du joueur
        self.wall = Wall(100, 100)

    # Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():  
            # Fermeture de la fenêtre
            if event.type == pygame.QUIT: 
                self.running = False  


    # Mise à jour du jeu
    def update(self):
        self.player.update()

    # Affichage du jeu
    def display(self):
        self.screen.fill("black")          # Nettoyage de l'écran
        self.player.draw(self.screen)      # Dessin du joueur
        self.wall.draw(self.screen)
        pygame.display.flip()              # Rafraîchissement

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update()                 
            self.display()                
            self.clock.tick(60)    

           
