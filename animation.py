class Animation:
    # Initialisation de l'animation
    def __init__(self, frames, speed=0.15, loop=True):
        self.frames = frames       # Liste des images
        self.speed = speed         # Vitesse de lecture
        self.loop = loop           # Définit si l'animation boucle
        self.index = 0             # Position actuelle
        self.image = frames[0]     # Image affichée

    # Mise à jour de l'animation
    def update(self):
        self.index += self.speed
        if self.index >= len(self.frames):
            if self.loop:                   # Retour au début
                self.index = 0
            else:                           # Reste sur la dernière frame
                self.index = len(self.frames) - 1
        self.image = self.frames[int(self.index)]

    # Accès à l'image courante
    def get_image(self):
        return self.image

    # Réinitialisation sur la première frame
    def reset(self):
        return self.frames[0]