import pygame
import os
from animation import Animation

class Wall(pygame.sprite.Sprite):
    # Initialisation du mur
    def __init__(self, x, y):
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', 'walls')

        # Chargement de l'image par défaut
        self.image = pygame.image.load(os.path.join(dir_file, 'walls_0.png')).convert_alpha()

        # Récupération du rectangle
        self.rect = self.image.get_rect(topleft=(x,y))

        # Nombre de vies du mur
        self.life = 5

        # Chargement de toutes les frames pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]
        
        # Création de l'animation
        self.animations = Animation(frames, 1, loop=False)

    # Mise à jour de l'animation
    def animate(self):
        self.animations.update()
        self.image = self.animations.get_image()

    # Affichage du mur
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        self.animate()