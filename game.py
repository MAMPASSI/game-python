import pygame
from player import player
from monster import Monster
from comet_event import CometFallEvent

class Game():

    def __init__(self):
        #definir si notre jeu à commencer ou non:
        self.is_playing = True

        self.all_players = pygame.sprite.Group()
        self.player =  player(self)
        self.all_players.add(self.player)
        #générer l'evenement
        self.comet_event = CometFallEvent(self)
        #créer notre groupe de monstre dans le jeu
        self.all_monster = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
    
    def game_over(self):
        # remetre le jeu à neuf, retirer les monstre
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self,screen):
        #appliquer l'image de notre joeur
        screen.blit(self.player.image,self.player.rect)

        #actualiser la bar de vie de mon joueur
        self.player.update_health_bar(screen)

        #actualiser la bar d'evenement du jeu
        self.comet_event.update_bar(screen)


        #appliquer l'ensemble des images de mon groupe projectile:
        self.player.all_projectile.draw(screen)

        #appliquer l'ensemble des images de mon groupe de monstre:
        self.all_monster.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comet
        self.comet_event.all_comets.draw(screen)
        
        #recuperer les projectile du joueur
        for projectile in self.player.all_projectile:
            projectile.move() 

        #recuperer les monstre de notre jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        #recuperer les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        #verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x>0:
            self.player.move_left()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    
    def spawn_monster(self):
        self.all_monster.add(Monster(self))
