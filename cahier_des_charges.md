### Cahier des charges



##### I - Introduction



###### A. Présentation du projet



Le projet consiste à développer une version personnalisée du jeu vidéo classique Space Invaders, créé à l’origine en 1978. Ce jeu appartient à la catégorie des Shoot ’Em Up, dans lequel le joueur contrôle un vaisseau spatial situé en bas de l’écran et doit éliminer des vagues d’ennemis qui descendent progressivement vers lui.





###### B. Objectifs du cahier des charges



Ce cahier des charges a pour but de : 

* Définir clairement les objectifs du projet et les fonctionnalités attendues du jeu. 
* Établir une vision commune pour tous les membres du groupe afin  assurer une cohérence dans le développement. 
* Servir de référence technique et organisationnelle tout au long du projet. 
* Détailler les contraintes techniques et fonctionnelles afin de guider la conception et la programmation. 
* Faciliter la rédaction du plan de test et de la documentation technique finale.





##### II. Contexte du projet



###### A. Description du contexte



Le projet s’inscrit dans le cadre du BUT Informatique 2025-2026, dont l’objectif est de mettre en pratique les compétences en programmation, gestion de projet et collaboration en équipe. Le projet offre une opportunité pédagogique intéressante, car il combine plusieurs aspects du développement logiciel :

* La programmation orientée objet (gestion des entités du jeu : joueur, ennemis, projectiles, etc.)
* La gestion des événements (déplacements, tirs, collisions)
* La mise en place d’une interface graphique
* L’organisation collaborative avec GitHub et le respect des bonnes pratiques (tests unitaires, documentation, revue de code).





###### B. Analyse des besoins



Afin d’assurer la réussite du projet, plusieurs besoins doivent être pris en compte :



1\. Besoins fonctionnels

* Déplacement du vaisseau du joueur de gauche à droite.
* Possibilité de tirer des projectiles vers le haut.
* Apparition d’ennemis en formation qui descendent progressivement.
* Détection des collisions (tir du joueur ↔ ennemi, ennemi ↔ joueur, ennemi ↔ limite inférieure de l’écran).
* Système de score et affichage à l’écran.
* Progression en difficulté (augmentation de la vitesse, nombre d’ennemis).



2\. Besoins techniques

* Développement en langage Python
* Utilisation de la bibliothèque graphique Pygame
* Gestion du projet avec GitHub (fork, branches, pull-requests, revue de code).
* Mise en place de tests unitaires sur les fonctions critiques (déplacements, collisions, score).



3\. Besoins organisationnels

* Répartition claire des rôles (responsable interface, logique du jeu, gestion GitHub, rédaction documentation).
* Développement incrémental : chaque fonctionnalité est codée, testée, validée avant d’être fusionnée.
* Mise à jour régulière de la documentation et du plan de test.





##### III. Objectifs du projet



###### A. Objectifs généraux



Le projet a pour but de développer une version fonctionnelle et complète du jeu Space Invaders, respectant les règles principales du jeu original.

Il s’agit d’un projet pédagogique permettant aux étudiants de :

* Mettre en pratique les notions vues en cours (programmation orientée objet, structures de données, gestion de projet).
* S’initier au développement d’un jeu vidéo à travers un cas concret et motivant.
* Développer des compétences de travail en équipe avec l’utilisation d’outils collaboratifs (GitHub, pull-requests, revues de code).
* Appliquer une démarche de qualité logicielle (normes de codage, documentation technique, plan de tests, tests unitaires).





###### B. Objectifs spécifiques



De manière plus précise, le projet vise à atteindre les objectifs suivants :



1. Implémentation technique

* Concevoir une architecture claire et modulaire (séparation logique du jeu / affichage).
* Développer les fonctionnalités de base : déplacement, tirs, gestion des ennemis, détection de collisions.
* Mettre en place un système de score et de progression.



2\.  Qualité logicielle

* Respecter les bonnes pratiques de codage (lisibilité, commentaires, modularité).
* Réaliser une batterie de tests unitaires garantissant la fiabilité des fonctions critiques.
* Assurer la maintenabilité du code via la documentation et une organisation cohérente.



3\.  Organisation du projet

* Définir une méthode de travail collaborative (répartition des tâches, communication au sein du groupe).
* Utiliser GitHub pour la gestion des versions, le suivi du développement et les revues de code.
* Produire les livrables attendus : cahier des charges, plan de tests, documentation technique, code commenté.







##### IV. Fonctionnalités requises



###### A. Liste exhaustive des fonctionnalités



1\. Fonctionnalités principales

* Déplacement horizontal du vaisseau du joueur (gauche/droite).
* Tir de projectiles par le joueur.
* Apparition d’une formation d’ennemis qui se déplacent de gauche à droite puis descendent progressivement.
* Détection et gestion des collisions :
* Projectile ↔ Ennemi → Ennemi détruit + points au joueur.
* Ennemi ↔ Joueur → Fin de partie.
* Ennemi ↔ Limite inférieure de l’écran → Fin de partie.
* Système de score affiché en temps réel.
* Gestion de la fin de partie (victoire si tous les ennemis sont détruits, défaite sinon).



2\. Fonctionnalités secondaires (optionnelles)

* Effets visuels ou sonores (tir, explosion).
* Écran d’accueil avec menu (Jouer / Quitter).
* Apparition aléatoire d’ennemis spéciaux rapportant plus de points.
* Niveaux progressifs avec difficulté croissante (vitesse des ennemis, nombre d’ennemis).
* Sauvegarde et affichage du meilleur score.



###### B. Priorisation des fonctionnalités



* Priorité 1 (essentielles, livrables obligatoires) :

&nbsp;	Déplacement du joueur, tirs, ennemis qui descendent, collisions, score, conditions de victoire/défaite.



* Priorité 2 (améliorations recommandées si le temps le permet) :

&nbsp;	Progression de la difficulté, ennemis spéciaux, écran de fin de partie amélioré.



* Priorité 3 (bonus, optionnel) :

&nbsp;	Effets sonores/visuels, sauvegarde du meilleur score, menu complet.





###### C. Interactions entre les fonctionnalités



* Le déplacement du joueur influence la position de ses tirs.
* Les projectiles interagissent avec les ennemis → suppression de l’ennemi et augmentation du score.
* Les ennemis interagissent entre eux (formation collective et déplacement coordonné).
* Les ennemis interagissent avec le joueur ou la limite inférieure de l’écran → condition de défaite.
* Le score évolue en fonction des interactions (projectiles qui touchent les ennemis).
* Les niveaux progressifs dépendent de la victoire (tous les ennemis détruits).





##### V. Contraintes et limitations



###### A. Contraintes de temps

###### 

* Le projet doit être réalisé durant le semestre 5 l’année universitaire 2025-2026 dans le cadre du BUT Informatique.
* Le développement sera réalisé de manière incrémentale, avec un suivi régulier via GitHub.
* Le code, la documentation, le plan de tests et les tests unitaires doivent être terminés avant la date de rendu fixée par l’enseignant.
* Une bonne gestion du temps est nécessaire : priorité aux fonctionnalités essentielles, puis aux améliorations si le calendrier le permet.



###### 

###### B. Contraintes techniques



* Langage de programmation : Python avec Pygame
* Environnement de développement : chaque membre doit disposer d’un environnement compatible (IDE, librairies installées, gestion de dépendances).
* Gestion de version : utilisation obligatoire de GitHub avec un fork du dépôt fourni.
* Qualité du code : respect des normes de codage, bonne lisibilité, commentaires clairs.
* Architecture : séparation stricte entre la logique du jeu et l’interface graphique.
* Tests unitaires : mise en place avec un framework adapté à Pygame





##### VI. Tests et validation



###### A. Stratégie de test



La stratégie de test repose sur deux niveaux :



1\.  Tests unitaires

* Mise en place avec un framework adapté (ex. pytest pour Python).
* Chaque fonction critique (déplacement, tir, collisions, score) doit être testée de manière isolée.



2\.  Tests fonctionnels

* Vérification des scénarios de jeu complets.
* Simulation d’actions du joueur (déplacement, tir) et validation du comportement attendu (ennemis détruits, score incrémenté, etc.).
* Validation manuelle sur l’interface graphique pour vérifier l’expérience utilisateur.





###### B. Critères de réussite des tests



1\.  Critères unitaires

* Déplacement du joueur limité aux bords de l’écran.
* Projectile créé correctement et se déplaçant vers le haut.
* Collision projectile ↔ ennemi : l’ennemi est supprimé, score mis à jour.
* Collision ennemi ↔ joueur : fin de partie.
* Ennemi atteignant le bas de l’écran → fin de partie.



2\.  Critères fonctionnels

* Le joueur peut jouer une partie complète sans crash.
* L’affichage du score est correct et mis à jour en temps réel.
* La victoire est détectée lorsque tous les ennemis sont détruits.
* La défaite est détectée si un ennemi touche le joueur ou atteint la limite inférieure.



3\.  Critères de qualité

* Taux de couverture des tests unitaires suffisant (> 70% recommandé).
* Code lisible, documenté, et validé via les pull-requests.
* Documentation et plan de test mis à jour et cohérents avec le code final.





###### C. Procédure de validation du projet



1\. Phase de développement

* Chaque fonctionnalité est codée et validée par des tests unitaires.
* Le code est intégré sur la branche principale uniquement après revue de code.



2\. Phase de test global

* Exécution de l’ensemble des tests unitaires et fonctionnels.
* Tests manuels en conditions réelles de jeu (simulation de parties).



3\. Phase de livraison

* Vérification que tous les livrables (code, documentation technique, plan de test, cahier des charges) sont présents sur GitHub.
* Validation par l’enseignant après présentation du projet et démonstration du jeu.





##### VII. Glossaire



###### A. Définition des termes techniques utilisés dans le cahier des charges



