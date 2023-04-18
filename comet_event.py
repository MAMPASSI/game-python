import pygame

from comet import Comet


class CometFallEvent:
    #lors du chargement -> créer un compteur:
    def __init__(self,game) :
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        # un groupe de sprite pour stocker nos comet
        self.all_comets = pygame.sprite.Group()

    
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100
    
    def meteor_full(self):
        for i in range(1,10):
            #apparaitre notre 1 er comete
            self.all_comets.add(Comet(self))
        
    def attempt_fall(self):
        #la jauge d'evenement est totalement charger:
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            print('pluie de commete')
            self.meteor_full()
           
            self.fall_mode = True
              
    def update_bar(self,surface):

        #AJOUTER du pourcentage à la bar
        self.add_percent()

       
        
        #bare noir en arriere plan 
        pygame.draw.rect(surface,(0,0,0), [
            0, # l'axe en x
            surface.get_height() - 20, #l'axe des y
            surface.get_width(),#la longueur de de ma fenetre
            10 #l'epaisseur de la bare
        ])
        #bare rouge (jauge d'even)
        pygame.draw.rect(surface,(187,11,11), [
            0, # l'axe en x
            surface.get_height() - 20, #l'axe des y
            (surface.get_width()/100) * self.percent,#la longueur de de ma fenetre
            10 #l'epaisseur de la bare
        ])
        


