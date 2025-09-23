import pygame
from player import Player

class Game:
    # Initialisation des composants
    def __init__(self, screen):
        self.screen = screen              
        self.running = True               
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0)

    # Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():  
            # Gestion évènement de fermeture
            if event.type == pygame.QUIT: 
                self.running = False  

        # Gestion des touches directionnelles
        keys = pygame.key.get_pressed()

        # Déplacement horizontal
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        # Déplacement vertical
        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0  

    def update(self):
        self.player.move()
        self.player.animate()

    def display(self):
        self.screen.fill("black")
        self.player.draw(self.screen)
        pygame.display.flip()

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update()                 
            self.display()                
            self.clock.tick(60)           
