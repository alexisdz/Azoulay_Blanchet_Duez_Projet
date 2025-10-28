import pygame
import os
from animation import Animation

class Enemy(pygame.sprite.Sprite):
    # Classe représentant un ennemi à l'écran
    def __init__(self, pos, constraint, enemy='sgriiipapa'):
        """
        Initialise un ennemi.
        :param pos: position de départ (x, y)
        :param constraint: limite horizontale de déplacement
        :param enemy: nom du dossier contenant les images de l'ennemi
        """
        super().__init__()

        # Chemin vers le dossier contenant les images de l'ennemi
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', enemy)

        # Chargement de l'image initiale de l'ennemi
        self.image = pygame.image.load(os.path.join(dir_file, enemy+'_0.png'))

        self.speed = 3                       # Vitesse de déplacement horizontal
        self.max_x_constraint = constraint   # Limite horizontale pour les collisions

        # Chargement de toutes les images pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]

        # Création de l'animation à partir des frames
        self.animations = Animation(frames, 0.20)

        # Rectangle de position et taille de l'ennemi
        self.rect = self.image.get_rect(topleft=pos)

    def constraint(self):
        """
        Empêche l'ennemi de sortir de l'écran.
        Ajuste sa position si elle dépasse les limites horizontales.
        """
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def animate(self):
        """
        Met à jour l'animation de l'ennemi.
        """
        self.animations.update()
        self.image = self.animations.get_image()

    def draw(self, screen):
        """
        Affiche l'ennemi sur l'écran.
        :param screen: surface Pygame où dessiner
        """
        screen.blit(self.image, self.rect)

    def update(self, direction):
        """
        Met à jour l'ennemi à chaque frame.
        :param direction: sens du déplacement horizontal (-1=gauche, 1=droite)
        """
        self.animate()
        self.constraint()
        self.rect.x += self.speed * direction


class Extra(Enemy):
    # Classe pour un ennemi spécial (bonus)
    def __init__(self, side, screen_width):
        """
        Initialise un ennemi bonus qui apparaît sur un côté de l'écran.
        :param side: 'left' ou 'right'
        :param screen_width: largeur de l'écran pour définir les limites
        """
        if side == 'right':  # Si l'ennemi apparaît à droite
            x = screen_width + 50
            self.speed = -3   # Se déplace vers la gauche
        else:                # Si l'ennemi apparaît à gauche
            x = -50
            self.speed = 3    # Se déplace vers la droite
        
        start_pos = (x, 50)  # Position initiale de l'ennemi

        # Appel du constructeur de la classe parent
        super().__init__(pos=start_pos, constraint=screen_width, enemy='extra')

    def update(self):
        """
        Met à jour l'ennemi bonus à chaque frame.
        Déplace simplement l'ennemi selon sa vitesse.
        """
        self.animate()
        self.rect.x += self.speed
