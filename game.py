import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen              # Surface de jeu
        self.running = True               # Contrôle de la boucle principale
        self.clock = pygame.time.Clock()  # Pour gérer le framerate

    def handling_events(self):
        for event in pygame.event.get():  # Parcourt tous les événements
            if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                self.running = False      # On arrête la boucle de jeu

    def update(self):
        pass  # Ici on mettra la logique du jeu (déplacements, collisions…)

    def display(self):
        pass  # Ici on dessine tout sur l'écran

    def run(self):
        while self.running:               # Boucle principale
            self.handling_events()        # Gestion des événements
            self.update()                 # Mise à jour du jeu
            self.display()                # Affichage
            self.clock.tick(60)           # Limite à 60 FPS
