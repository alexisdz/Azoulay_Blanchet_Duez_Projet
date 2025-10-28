class Animation:
    # Classe représentant une animation composée de plusieurs images (frames)

    def __init__(self, frames, speed=0.15, loop=True):
        """
        Initialise l'animation.
        :param frames: liste d'images constituant l'animation
        :param speed: vitesse de défilement des images (frames)
        :param loop: si True, l'animation recommence à la fin
        """
        self.frames = frames       # Stocke toutes les images de l'animation
        self.speed = speed         # Vitesse à laquelle les images défilent
        self.loop = loop           # Détermine si l'animation doit boucler
        self.index = 0             # Position actuelle dans la liste des frames (peut être flottante pour gérer la vitesse)
        self.image = frames[0]     # Image actuellement affichée

    def update(self):
        """
        Met à jour l'animation en avançant à la prochaine image selon la vitesse.
        Gère la boucle ou la fin selon le paramètre 'loop'.
        """
        self.index += self.speed                # Avance l'index de la vitesse définie
        if self.index >= len(self.frames):     # Si on dépasse le nombre de frames
            if self.loop:                      # Si l'animation doit boucler
                self.index = 0                 # Retour à la première frame
            else:                              # Sinon
                self.index = len(self.frames) - 1  # Reste sur la dernière frame
        self.image = self.frames[int(self.index)] # Met à jour l'image affichée

    def get_image(self):
        """
        Retourne l'image actuelle de l'animation.
        """
        return self.image

    def reset(self):
        """
        Réinitialise l'animation et retourne la première image.
        """
        self.index = 0             # Remet l'index au début
        self.image = self.frames[0] # Affiche la première image
        return self.image
    