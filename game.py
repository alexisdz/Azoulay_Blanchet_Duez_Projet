import pygame
from player import Player
from enemy import Enemy, Extra
from laser import Laser
from random import choice, randint

from walls import Wall

class Game:
    # Initialisation du jeu
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))               # Surface d'affichage
        self.running = True                # État du jeu
        self.clock = pygame.time.Clock()   # Gestion du temps
        self.player = pygame.sprite.GroupSingle(Player((screen_width / 2,screen_height), screen_width))         # Création du joueur
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Gestion des ennemies
        self.enemies = pygame.sprite.Group()
        self.enemy_setup(rows = 6, cols = 8,screen_width = screen_width)
        self.enemy_direction = 1

        
		# Gestion de l'ennemie extra
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40,80)
        self.screen = pygame.display.set_mode((screen_width, screen_height)) # Surface d'affichage
        self.running = True # État du jeu
        self.clock = pygame.time.Clock() # Gestion du temps
        self.player = Player((screen_width/2, screen_height), screen_width) # Création du joueur
        
        # Création des murs
        self.walls = pygame.sprite.Group()

        # Murs de gauche
        self.walls.add(Wall(120, screen_height * 3/4))
        self.walls.add(Wall(120, screen_height * 3/4 + 32))
        self.walls.add(Wall(152, screen_height * 3/4))
        self.walls.add(Wall(184, screen_height * 3/4))
        self.walls.add(Wall(184, screen_height * 3/4 + 32))

        # Murs du milieu
        self.walls.add(Wall(screen_width/2 - 48, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 - 48, screen_height * 3/4 + 32))
        self.walls.add(Wall(screen_width/2 - 16, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 + 16, screen_height * 3/4))
        self.walls.add(Wall(screen_width/2 + 16, screen_height * 3/4 + 32))

        # Murs de droite
        self.walls.add(Wall(screen_width - 152, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 152, screen_height * 3/4 + 32))
        self.walls.add(Wall(screen_width - 184, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 216, screen_height * 3/4))
        self.walls.add(Wall(screen_width - 216, screen_height * 3/4 + 32))

    # Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():  
            # Fermeture de la fenêtre
            if event.type == pygame.QUIT: 
                self.running = False  


    # Mise à jour du jeu
    def update(self):
        self.player.update()
        self.enemies.update(self.enemy_direction)
        self.extra.update()

        self.enemy_position_checker()
        self.collision_checks()
        self.extra_enemy_timer()

    # Affichage du jeu
    def display(self):
        self.screen.fill("black")          # Nettoyage de l'écran
        self.player.draw(self.screen)      # Dessin du joueur
        self.enemies.draw(self.screen)      # Dessin des ennemis
        self.extra.draw(self.screen)        #Dessin de l'ennemi extra
        self.player.sprite.lasers.draw(self.screen)
        self.walls.draw(self.screen)       # Dessin des murs
        pygame.display.flip()              # Rafraîchissement

    # Boucle principale
    def run(self):
        while self.running:               
            self.handling_events()        
            self.update() 
            self.laser_hits_wall()                
            self.display()                
            self.clock.tick(60)
            
    def enemy_setup(self,rows,cols,screen_width,x_distance=60,y_distance=48,x_offset=70,y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                
                if row_index < 2: # Lignes 0 et 1 (les deux du haut)
                    enemy_sprite = Enemy((x,y), screen_width, 'bruh')
                elif row_index < 4: # Lignes 2 et 3 (les deux du milieu)
                    enemy_sprite = Enemy((x,y), screen_width, 'piruru')
                else: # Lignes 4 et 5 (les deux dernières)
                    enemy_sprite = Enemy((x,y), screen_width, 'sgriiipapa')
                self.enemies.add(enemy_sprite)

    # Gestion des collisions des ennemies
    def enemy_position_checker(self):
        all_enemies = self.enemies.sprites()
        for enemy in all_enemies:
            if enemy.rect.right >= self.screen_width - 10: # change la direction du groupe si un ennemi touche le bord
                self.enemy_direction = -1
                self.enemy_move_down(2)
            elif enemy.rect.left <= 10:
                self.enemy_direction = 1
                self.enemy_move_down(2)

    def enemy_move_down(self, distance):
        if self.enemies:
            for enemy in self.enemies.sprites():
                enemy.rect.y += distance

    def extra_enemy_timer(self):#gestion de l'ennemi bonus
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right','left']),self.screen_width))#choix aleatoire si l'ennemi apprait à gauche ou à droite
            self.extra_spawn_time = randint(400,800) # cooldown pour aleatoire sur l'apparition de l'ennemi

    
    def collision_checks(self):
        # player lasers 
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser,self.enemies,True):
                    laser.kill()
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()    
       
    def laser_hits_wall(self):
        # Vérifier collision entre lasers et murs
        collisions = pygame.sprite.groupcollide(
            self.player.lasers,  # groupe de lasers
            self.walls,          # groupe de murs
            True,                # supprime le laser après collision
            False                # ne supprime pas le mur automatiquement
        )

        # Mise à jour des murs lors d'une collision
        for _, hit_walls in collisions.items():
            for wall in hit_walls:
                wall.update()
