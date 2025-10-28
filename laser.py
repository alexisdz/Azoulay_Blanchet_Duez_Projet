import pygame 

class Laser(pygame.sprite.Sprite):
    """
    Classe représentant un laser tiré par le joueur ou les ennemis.
    Hérite de pygame.sprite.Sprite pour pouvoir être géré facilement dans un groupe de sprites.
    """

    def __init__(self, pos, speed, screen_height):
        """
        Initialise un laser.
        :param pos: position initiale (x, y) du centre du laser
        :param speed: vitesse verticale (positive vers le bas, négative vers le haut)
        :param screen_height: hauteur de l'écran pour savoir quand détruire le laser
        """
        super().__init__()
        # Surface représentant le laser (rectangle blanc)
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        # Rectangle pour la position et les collisions
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def destroy(self):
        """
        Supprime le laser s'il sort de l'écran (hors de la zone visible).
        """
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()  # supprime le sprite du groupe et libère la mémoire

    def update(self):
        """
        Déplace le laser verticalement à chaque frame et vérifie s'il doit être détruit.
        """
        self.rect.y += self.speed  # déplace le laser
        self.destroy()  # destruction si hors écran
