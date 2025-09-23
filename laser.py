import pygame 

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        # Crée une surface pour représenter le laser
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')  # couleur du laser
        self.rect = self.image.get_rect(center=pos)  # position initiale
        self.speed = speed  # vitesse verticale du laser
        self.height_y_constraint = screen_height  # limite de l'écran pour destruction

    def destroy(self):
        # Supprime le laser s'il sort de l'écran (haut ou bas)
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        # Déplace le laser verticalement
        self.rect.y += self.speed
        # Vérifie s'il doit être détruit
        self.destroy()
