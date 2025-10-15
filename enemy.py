import pygame
import os
from animation import Animation

class Enemy(pygame.sprite.Sprite):
    # Initialisation du joueur
    def __init__(self, pos, constraint, enemy='sgriiipapa'):
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', enemy)

        # Chargement de l'image par défaut
        self.image = pygame.image.load(os.path.join(dir_file, enemy+'_0.png'))

        self.speed = 3
        self.max_x_constraint = constraint

        # Chargement de toutes les frames pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]

        # Création de l'animation
        self.animations = Animation(frames, 0.20)

        # Position et taille de l'ennemi
        self.rect = self.image.get_rect(topleft = pos)

    #gestion des collisions avec les limites de l'écran
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    # Mise à jour de l'animation
    def animate(self):
        self.animations.update()
        self.image = self.animations.get_image()

    # Affichage du joueur et du laser
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self, direction):
        self.animate()
        self.constraint()
        self.rect.x += self.speed * direction

class Extra(Enemy): #class de l'ennemi bonus
    def __init__(self, side, screen_width):

        if side == 'right': #si l'ennemi apparait à droite ou à gauche
            x = screen_width + 50
            self.speed = -3  
        else:
            x = -50
            self.speed = 3   
        
        start_pos = (x, 50)

        super().__init__(pos=start_pos, constraint=screen_width, enemy='extra')

    def update(self):
        self.animate() 
        self.rect.x += self.speed