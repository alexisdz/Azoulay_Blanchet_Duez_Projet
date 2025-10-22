import pygame
from player import Player
from enemy import Enemy, Extra
from laser import Laser
from random import choice, randint
from walls import Wall

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.display.set_caption("Space Invaders")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = pygame.sprite.GroupSingle(Player((screen_width / 2, screen_height), screen_width))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = 0          # Score du joueur
        self.lives = 3          # Nombre de vies
        self.font = pygame.font.Font(None, 36)  # Police pour l'affichage

        # Gestion des ennemis
        self.enemies = pygame.sprite.Group()
        self.enemy_setup(rows=6, cols=8, screen_width=screen_width)
        self.enemy_direction = 1

        # Lasers ennemis
        self.enemy_lasers = pygame.sprite.Group()
        self.enemy_shoot_timer = 0

        # Ennemi bonus
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40, 80)

        # Création des murs
        self.walls = pygame.sprite.Group()
        self.create_walls()

    def create_walls(self):
        # Murs de gauche
        self.walls.add(Wall(120, self.screen_height * 3 / 4))
        self.walls.add(Wall(120, self.screen_height * 3 / 4 + 32))
        self.walls.add(Wall(152, self.screen_height * 3 / 4))
        self.walls.add(Wall(184, self.screen_height * 3 / 4))
        self.walls.add(Wall(184, self.screen_height * 3 / 4 + 32))

        # Murs du milieu
        self.walls.add(Wall(self.screen_width / 2 - 48, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width / 2 - 48, self.screen_height * 3 / 4 + 32))
        self.walls.add(Wall(self.screen_width / 2 - 16, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width / 2 + 16, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width / 2 + 16, self.screen_height * 3 / 4 + 32))

        # Murs de droite
        self.walls.add(Wall(self.screen_width - 152, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width - 152, self.screen_height * 3 / 4 + 32))
        self.walls.add(Wall(self.screen_width - 184, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width - 216, self.screen_height * 3 / 4))
        self.walls.add(Wall(self.screen_width - 216, self.screen_height * 3 / 4 + 32))

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause_menu()

    def update(self):
        self.player.update()
        self.enemies.update(self.enemy_direction)
        self.extra.update()
        self.enemy_lasers.update()

        self.enemy_position_checker()
        self.collision_checks()
        self.extra_enemy_timer()
        self.enemy_shoot_logic()

    def display(self):
        self.screen.fill("black")
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.extra.draw(self.screen)
        self.player.sprite.lasers.draw(self.screen)
        self.enemy_lasers.draw(self.screen)
        self.walls.draw(self.screen)

        # Affichage du score et des vies
        score_text = self.font.render(f"Score: {self.score}", True, "white")
        lives_text = self.font.render(f"Vies: {self.lives}", True, "white")
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (self.screen_width - 150, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.laser_hits_wall()
            self.check_game_over()
            self.display()
            self.clock.tick(60)

    def enemy_setup(self, rows, cols, screen_width, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index < 2:
                    enemy_sprite = Enemy((x, y), screen_width, 'bruh')
                elif row_index < 4:
                    enemy_sprite = Enemy((x, y), screen_width, 'piruru')
                else:
                    enemy_sprite = Enemy((x, y), screen_width, 'sgriiipapa')
                self.enemies.add(enemy_sprite)

    def enemy_position_checker(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.right >= self.screen_width - 10:
                self.enemy_direction = -1
                self.enemy_move_down(2)
            elif enemy.rect.left <= 10:
                self.enemy_direction = 1
                self.enemy_move_down(2)

    def enemy_move_down(self, distance):
        for enemy in self.enemies.sprites():
            enemy.rect.y += distance

    def enemy_shoot_logic(self):
        """Les ennemis tirent périodiquement vers le joueur"""
        self.enemy_shoot_timer += 1
        if self.enemy_shoot_timer >= 60:  # toutes les 60 frames (~1 sec)
            self.enemy_shoot_timer = 0
            if self.enemies.sprites():
                shooter = choice(self.enemies.sprites())
                laser = Laser(shooter.rect.center, 6, self.screen_height)
                self.enemy_lasers.add(laser)

    def extra_enemy_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left']), self.screen_width))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # Lasers du joueur
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # Collision avec les ennemis
                if pygame.sprite.spritecollide(laser, self.enemies, True):
                    laser.kill()
                    self.score += 100  # +100 points par ennemi détruit
                # Collision avec l'ennemi extra
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()
                    self.score += 1000  # +1000 points pour l'ennemi bonus
                # Collision avec les murs
                hit_walls = pygame.sprite.spritecollide(laser, self.walls, False)
                if hit_walls:
                    laser.kill()
                    for wall in hit_walls:
                        wall.update()  # abîme le mur

        # Lasers ennemis
        if hasattr(self, 'enemy_lasers') and self.enemy_lasers:
            for laser in self.enemy_lasers:
                # Collision avec le joueur
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.running = False  # Game over
                # Collision avec les murs
                hit_walls = pygame.sprite.spritecollide(laser, self.walls, False)
                if hit_walls:
                    laser.kill()
                    for wall in hit_walls:
                        wall.update()  # abîme le mur


    def laser_hits_wall(self):
        collisions = pygame.sprite.groupcollide(
            self.player.sprite.lasers,
            self.walls,
            True,
            False
        )
        for _, hit_walls in collisions.items():
            for wall in hit_walls:
                wall.update()

    # --- MENUS ---
    def show_menu(self):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        options = ["Jouer", "Quitter"]
        selected = 0

        menu_running = True
        while menu_running:
            self.screen.fill("black")

            title_text = font.render("SPACE INVADERS", True, "white")
            title_rect = title_text.get_rect(center=(self.screen_width / 2, self.screen_height / 4))
            self.screen.blit(title_text, title_rect)

            for i, option in enumerate(options):
                color = "yellow" if i == selected else "white"
                option_text = small_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + i * 60))
                self.screen.blit(option_text, option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if options[selected] == "Jouer":
                            menu_running = False
                        elif options[selected] == "Quitter":
                            pygame.quit()
                            exit()

    def pause_menu(self):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)
        options = ["Continuer", "Quitter"]
        selected = 0

        paused = True
        while paused:
            self.screen.fill("black")

            title_text = font.render("PAUSE", True, "white")
            title_rect = title_text.get_rect(center=(self.screen_width / 2, self.screen_height / 4))
            self.screen.blit(title_text, title_rect)

            for i, option in enumerate(options):
                color = "yellow" if i == selected else "white"
                option_text = small_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + i * 60))
                self.screen.blit(option_text, option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if options[selected] == "Continuer":
                            paused = False
                        elif options[selected] == "Quitter":
                            pygame.quit()
                            exit()

    def check_game_over(self):
        # Condition : tous les ennemis sont détruits
        if not self.enemies:
            self.end_screen(victory=True)

        # Condition : plus de vies
        elif self.lives <= 0:
            self.end_screen(victory=False)

        # Condition : un ennemi touche le joueur
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(self.player.sprite.rect):
                self.end_screen(victory=False)

    def end_screen(self, victory=False):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        if victory:
            title = "VICTOIRE !"
            color = "green"
        else:
            title = "GAME OVER"
            color = "red"

        end_running = True
        while end_running:
            self.screen.fill("black")

            # Titre (victoire ou défaite)
            title_text = font.render(title, True, color)
            title_rect = title_text.get_rect(center=(self.screen_width / 2, self.screen_height / 3))
            self.screen.blit(title_text, title_rect)

            # Score
            score_text = small_font.render(f"Score : {self.score}", True, "white")
            score_rect = score_text.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
            self.screen.blit(score_text, score_rect)

            # Message de retour
            msg_text = small_font.render("Appuie sur Entrée pour revenir au menu", True, "gray")
            msg_rect = msg_text.get_rect(center=(self.screen_width / 2, self.screen_height * 3 / 4))
            self.screen.blit(msg_text, msg_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    end_running = False
                    self.show_menu()
                    self.__init__(self.screen_width, self.screen_height)  # reset du jeu
                    self.run()
                    return
                