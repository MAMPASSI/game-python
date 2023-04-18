import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self,game) :
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack =0.3
        self.velocity = random.randint(2,4)
        self.image = pygame.image.load("Asset/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
    
    def damage(self,amount):
        #Infliger des degat
        self.health -= amount

        #verifier si son nouveau npmbre de pont de vie est inferieur ou égale à zéro
        if self.health<=0:
            #Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health

            #si la bare d'evenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monster.remove(self)
                
                #appel de la methode pour essayer de déclancher la plui de comete
                self.game.comet_event.attempt_fall()


    def update_health_bar (self,surface):
        #definir une couleur pour notre jauge de vie(vert clair)
        bar_color = (111, 210,46)
        #definir une couleur pour  l'arrire plan de notre jauge de vie(gris)
        bg_bar_color = (60,63,60)
        #definir la position de notre jauge de vie ainsi que sa la largeur et son epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        #definir la position de l'arrire plan de  notre jauge de vie ainsi que sa la largeur et son epaisseur
        bg_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #dessiner notre jauge de vie
        pygame.draw.rect(surface,bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)

       


    
    def forward(self):
        #le deplacement se fais que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colision avec le joueur
        else:
            #infliger des dégats au joueur
            self.game.player.damage(self.attack)
