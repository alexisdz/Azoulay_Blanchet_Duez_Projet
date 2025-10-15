import pygame
from player import Player
from walls import Wall

class Game:
    # Initialisation du jeu
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height)) # Surface d'affichage
        self.running = True # État du jeu
        self.clock = pygame.time.Clock() # Gestion du temps
        self.player = Player((screen_width/2, screen_height), screen_width) # Création du joueur
        
        # Création des murs
        self.walls = pygame.sprite.Group()

        # Murs de gauche
        self.walls.add(Wall(120, screen_height * 3/4))
        self.walls.add(Wall(120, screen_height * 3/4 + 32))
        self.walls.add(Wall(152, screen_height * 3/4))
        self.walls.add(Wall(184, screen_height * 3/4))
        self.walls.add(Wall(184, screen_height * 3/4 + 32))

        # Murs du milieu
        self.walls.add(Wall(screen_width/2 - 48, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 - 48, screen_height * 3/4 + 32))
        self.walls.add(Wall(screen_width/2 - 16, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 + 16, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 + 16, screen_height * 3/4 + 32))

        # Murs de droite
        self.walls.add(Wall(screen_width - 152, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 152, screen_height * 3/4 + 32))
        self.walls.add(Wall(screen_width - 184, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 216, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 216, screen_height * 3/4 + 32))

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
        self.walls.draw(self.screen)       # Dessin des murs
        pygame.display.flip()              # Rafraîchissement

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update() 
            self.laser_hits_wall()                
            self.display()                
            self.clock.tick(60)    
       
    def laser_hits_wall(self):
        # Vérifier collision entre lasers et murs
        collisions = pygame.sprite.groupcollide(
            self.player.lasers,  # groupe de lasers
            self.walls,          # groupe de murs
            True,                # supprime le laser après collision
            False                # ne supprime pas le mur automatiquement
        )

        # Mise à jour des murs lors d'une collision
        for _, hit_walls in collisions.items():
            for wall in hit_walls:
                wall.update()