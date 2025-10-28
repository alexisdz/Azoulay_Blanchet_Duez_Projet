import pygame
import os
from animation import Animation
from laser import Laser

class Player(pygame.sprite.Sprite):
    """
    Classe représentant le joueur.
    Hérite de pygame.sprite.Sprite pour pouvoir être géré dans des groupes de sprites.
    """

    def __init__(self, pos, constraint, shoot_sound):
        """
        Initialise le joueur.
        :param pos: position initiale (x, y) du joueur (milieu bas)
        :param constraint: limite horizontale pour empêcher le joueur de sortir de l'écran
        :param shoot_sound: son joué lors d'un tir
        """
        super().__init__()
        dir_file = os.path.join(os.path.dirname(__file__), 'assets', 'player')

        # Chargement de l'image initiale
        self.image = pygame.image.load(os.path.join(dir_file, 'player_0.png'))

        # Son du tir
        self.shoot_sound = shoot_sound

        self.speed = 5                       # vitesse de déplacement horizontal
        self.max_x_constraint = constraint   # limite de l'écran

        # Chargement de toutes les images pour l'animation
        frames = [pygame.image.load(os.path.join(dir_file, img_file)) 
                  for img_file in sorted(os.listdir(dir_file))]

        # Création de l'objet Animation pour gérer les frames
        self.animations = Animation(frames, 0.20)

        # Rectangle pour position et collisions
        self.rect = self.image.get_rect(midbottom=pos)

        # Groupe de lasers tirés par le joueur
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        """
        Récupère les touches pressées pour gérer les mouvements et le tir.
        Flèche gauche/droite pour se déplacer, espace pour tirer.
        """
        keys = pygame.key.get_pressed()

        # Déplacement horizontal
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        # Tir d'un laser seulement si aucun laser actif à l'écran
        if keys[pygame.K_SPACE] and len(self.lasers) == 0:
            self.shoot_laser()

    def constraint(self):
        """
        Empêche le joueur de sortir de l'écran.
        Ajuste sa position si elle dépasse les bords gauche/droite.
        """
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def animate(self):
        """
        Met à jour l'animation du joueur.
        """
        self.animations.update()
        self.image = self.animations.get_image()

    def draw(self, screen):
        """
        Affiche le joueur et ses lasers sur l'écran.
        :param screen: surface Pygame où dessiner
        """
        screen.blit(self.image, self.rect)
        self.lasers.draw(screen)

    def shoot_laser(self):
        """
        Crée un laser au niveau du haut du joueur et le joue le son de tir.
        """
        self.lasers.add(Laser(self.rect.midtop, -8, self.rect.bottom))
        self.shoot_sound.play()

    def update(self):
        """
        Mise à jour du joueur à chaque frame :
        - Animation
        - Mouvement selon les touches
        - Respect des limites de l'écran
        - Mise à jour des lasers
        """
        self.animate()
        self.get_input()
        self.constraint()
        self.lasers.update()
