import pygame
import os
from animation import Animation
from laser import Laser

class Player(pygame.sprite.Sprite):
    # Initialisation du joueur
    def __init__(self, pos, constraint):
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', 'player')

        # Chargement de l'image par défaut
        self.image = pygame.image.load(os.path.join(dir_file, 'player_0.png'))

        self.speed = 5
        self.max_x_constraint = constraint

        # Chargement de toutes les frames pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]

        # Création de l'animation
        self.animations = Animation(frames, 0.20)

        # Position et taille du joueur
        self.rect = self.image.get_rect(midbottom = pos)

        #Création de laser
        self.lasers = pygame.sprite.Group()

    #gestion des mouvements de gauche à droite
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        # Tir uniquement si aucun laser actif
        if keys[pygame.K_SPACE] and len(self.lasers) == 0:
            self.shoot_laser()

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
        self.lasers.draw(screen)           

    def shoot_laser(self):
        # Tire un laser depuis la position actuelle du joueur
        self.lasers.add(Laser(self.rect.center, -8, self.rect.bottom))


    def update(self):
        self.animate()
        self.get_input()
        self.constraint()
        self.lasers.update()