import pygame
from projectile import projectile



class player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack =10
        self.velocity = 5
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load("Asset/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    
    def damage(self,amount):
        if self.health - amount > amount:
            #Infliger des degat
            self.health -= amount
        
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()
    
    def update_health_bar (self,surface):
        #definir une couleur pour notre jauge de vie(vert clair)
        bar_color = (111, 210,46)
        #definir une couleur pour  l'arrire plan de notre jauge de vie(gris)
        bg_bar_color = (60,63,60)
        #definir la position de notre jauge de vie ainsi que sa la largeur et son epaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        #definir la position de l'arrire plan de  notre jauge de vie ainsi que sa la largeur et son epaisseur
        bg_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]

        #dessiner notre jauge de vie
        pygame.draw.rect(surface,bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)

    
    def lanch_projectile(self):
        
        self.all_projectile.add(projectile(self))

    def move_rigth(self):
        #si le joueur n'est pas en collision avec le monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x+=self.velocity

    def move_left(self):
        self.rect.x -=self.velocity

