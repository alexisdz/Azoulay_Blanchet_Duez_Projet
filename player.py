import pygame
import os
from animation import Animation

class Player(pygame.sprite.Sprite):
    # Initialisation du joueur
    def __init__(self, x, y):
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', 'player')

        # Chargement de l'image par défaut
        self.image = pygame.image.load(os.path.join(dir_file, 'player_0.png'))

        # Chargement de toutes les frames pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]

        # Création de l'animation
        self.animations = Animation(frames, 0.20)

        # Position et taille du joueur
        self.rect = self.image.get_rect(x=x, y=y)

        # Vitesse et direction du déplacement
        self.speed = 5
        self.velocity = [0, 0]

    # Déplacement du joueur
    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, 
                          self.velocity[1] * self.speed)

    # Mise à jour de l'animation
    def animate(self):
        self.animations.update()
        self.image = self.animations.get_image()

    # Affichage du joueur
    def draw(self, screen):
        screen.blit(self.image, self.rect)