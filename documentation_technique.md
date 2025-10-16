# Documentation Technique – Space Invaders Personnalisé

## I. Introduction

### A. Présentation du jeu
Le projet consiste à développer une version personnalisée du jeu vidéo classique **Space Invaders**, créé en 1978. Il s’agit d’un Shoot ’Em Up dans lequel le joueur contrôle un vaisseau spatial situé en bas de l’écran et doit éliminer des vagues d’ennemis qui descendent progressivement.

### B. Objectifs de la documentation technique
Cette documentation a pour objectifs de :
- Décrire l’architecture technique du jeu.
- Expliquer la conception du gameplay et les interactions.
- Détaillez la gestion des graphismes, animations et sons.
- Fournir des informations sur l’optimisation, le code et la maintenance.
- Servir de référence pour les développeurs et futurs contributeurs.

---

## II. Architecture du jeu

### A. Moteur de jeu
Le jeu est développé en **Python** en utilisant **Pygame** comme moteur de jeu principal pour la gestion de l’affichage, des événements et des ressources.

### B. Système de rendu
- Le rendu est **2D**.
- Les entités du jeu (vaisseaux, ennemis, projectiles) utilisent des **sprites animés**.
- Les animations sont constituées de plusieurs frames stockées dans des fichiers `.png` dans des dossiers spécifiques.

### C. Gestion des ressources
- Les ressources sont organisées dans un dossier `assets` :
  - `/player` : sprites du joueur
  - `/enemy` : sprites des ennemis
  - `/walls` : sprites des murs
  - `/sounds` : effets sonores (tir, explosion)
- La musique et les sons sont intégrés via **Pygame**.
- Possibilité de rajouter des sons supplémentaires si nécessaire.

---

## III. Conception du gameplay

### A. Mécaniques de jeu
- Déplacement horizontal du joueur.
- Tir de projectiles vers le haut.
- Formation d’ennemis se déplaçant de gauche à droite et descendant progressivement.
- Ennemi spécial rapportant plus de points.
- Murs protecteurs qui se dégradent après 5 tirs (ennemis ou joueur).

### B. Systèmes de contrôle
- Contrôle clavier :
  - Flèches gauche/droite pour déplacer le vaisseau.
  - Barre espace pour tirer.

### C. Interactions joueur-environnement
- Le déplacement du joueur influence la trajectoire des tirs.
- Les projectiles détruisent les ennemis et augmentent le score.
- Les ennemis interagissent avec le joueur ou la limite inférieure → condition de défaite.
- Les murs protègent le joueur et se détruisent progressivement.

---

## IV. Graphismes et Animation

### A. Modélisation 2D
- Le jeu est **entièrement en 2D**.
- Les entités utilisent des sprites animés.

### B. Textures et sprites
- Utilisation d’images `.png` pour toutes les entités.
- Pas de shaders particuliers, juste des images pour chaque frame d’animation.

### C. Animation des personnages et objets
- Animation simple par changement de frame.
- Les ennemis et le joueur ont des cycles d’animation basiques.

---

## V. Son et Musique

### A. Effets sonores
- Tir du joueur
- Explosion des ennemis
- Ennemi spécial

### B. Musique d’ambiance
- Musique de fond pendant le jeu.

### C. Intégration sonore dans le gameplay
- Son et musique intégrés via **Pygame**.
- Effets déclenchés par les actions du joueur et des ennemis.

---

## VI. Optimisation et Performance

### A. Gestion des ressources système
- Limitation à **60 ticks par seconde**.
- Chargement des sprites et sons à l’initialisation.

### B. Optimisation du code
- Gestion efficace des collisions.
- Suppression des entités hors écran pour libérer la mémoire.

### C. Tests de performance
- Vérification du framerate constant à 60 FPS.
- Contrôle des performances lors des vagues d’ennemis nombreuses.

---

## VII. Documentation du Code

### A. Structure du code source
- `main.py` : point d’entrée du jeu.
- `assets/` :
  - `player/` : sprites du joueur
  - `enemy/` : sprites des ennemis
  - `walls/` : sprites des murs
  - `sounds/` : fichiers audio

### B. Commentaires et documentation interne
- Commentaires pour chaque classe et fonction critique.
- Suivi des modifications via **GitHub**.

### C. Bonnes pratiques de codage
- Séparation stricte logique du jeu / affichage.
- Fonctions modulaires et lisibles.
- Pull-requests et revues de code pour toute intégration.

---

## VIII. Déploiement et Maintenance

### A. Configuration requise
- **OS** : Windows, macOS, Linux
- **Python** : 3.10 ou supérieur
- **Pygame** : dernière version stable

### B. Procédure d’installation
1. Cloner le dépôt GitHub.
2. Installer les dépendances : `pip install -r requirements.txt`
3. Exécuter le jeu : `python main.py`

### C. Gestion des mises à jour et correctifs
- Les mises à jour passent par GitHub (branches, pull-requests).
- Corrections appliquées après validation via tests unitaires et fonctionnels.