import pygame

class Game:
    # Initialisation des composants
    def __init__(self, screen):
        self.screen = screen              
        self.running = True               
        self.clock = pygame.time.Clock()  

    # Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():  
            # Gestion évènement de fermeture
            if event.type == pygame.QUIT: 
                self.running = False    

    def update(self):
        pass  # Ici on mettra la logique du jeu (déplacements, collisions…)

    def display(self):
        pass  # Ici on dessine tout sur l'écran

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update()                 
            self.display()                
            self.clock.tick(60)           
