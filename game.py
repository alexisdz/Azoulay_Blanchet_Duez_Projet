import pygame
from player import Player
from enemy import Enemy

class Game:
    # Initialisation du jeu
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))               # Surface d'affichage
        self.running = True                # État du jeu
        self.clock = pygame.time.Clock()   # Gestion du temps
        self.player = Player( (screen_width / 2,screen_height), screen_width)         # Création du joueur
        self.enemies = pygame.sprite.Group()
        self.enemy_setup(rows = 6, cols = 8,screen_width = screen_width)

    # Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():  
            # Fermeture de la fenêtre
            if event.type == pygame.QUIT: 
                self.running = False  


    # Mise à jour du jeu
    def update(self):
        self.player.update()
        self.enemies.update()

    # Affichage du jeu
    def display(self):
        self.screen.fill("black")          # Nettoyage de l'écran
        self.player.draw(self.screen)      # Dessin du joueur
        self.enemies.draw(self.screen)      # Dessin des ennemis
        pygame.display.flip()              # Rafraîchissement

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update()                 
            self.display()                
            self.clock.tick(60)
            
    def enemy_setup(self,rows,cols,screen_width,x_distance=60,y_distance=48,x_offset=70,y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                
                if row_index == 0: enemy_sprite = Enemy((x,y), screen_width, 'piruru')
                else : enemy_sprite = Enemy((x,y), screen_width, 'blublu')
                self.enemies.add(enemy_sprite)
                
                
                
                
                
