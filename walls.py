import pygame
import os
from animation import Animation

class Wall(pygame.sprite.Sprite):
    """
    Classe représentant un mur de protection dans le jeu.
    Les murs peuvent être détruits par les lasers.
    """

    def __init__(self, x, y):
        """
        Initialise le mur.
        :param x: position horizontale du mur
        :param y: position verticale du mur
        """
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', 'walls')

        # Chargement de l'image initiale du mur
        self.image = pygame.image.load(os.path.join(dir_file, 'walls_0.png')).convert_alpha()

        # Rectangle pour la position et les collisions
        self.rect = self.image.get_rect(topleft=(x, y))

        # Points de vie du mur (combien de tirs il peut encaisser)
        self.life = 5

        # Chargement de toutes les images pour l'animation de destruction
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]
        
        # Création de l'animation (non bouclée)
        self.animations = Animation(frames, 1, loop=False)

    def animate(self):
        """
        Met à jour l'animation du mur en fonction des dégâts subis.
        """
        self.animations.update()
        self.image = self.animations.get_image()

    def draw(self, screen):
        """
        Affiche le mur à l'écran.
        :param screen: surface Pygame où dessiner
        """
        screen.blit(self.image, self.rect)
        
    def update(self):
        """
        Réduit la vie du mur lorsqu'il est touché,
        met à jour l'animation et détruit le mur si sa vie est épuisée.
        """
        self.life -= 1    # le mur perd 1 point de vie
        self.animate()     # mise à jour de l'animation
        if self.life <= 0:
            self.kill()   # supprime le mur du jeu si sa vie est nulle
