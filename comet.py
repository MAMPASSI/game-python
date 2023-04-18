import pygame


import random

class Comet(pygame.sprite.Sprite) :

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('Asset/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2,5)
        self.rect.x = random.randint(20,800)
        self.rect.y= -random.randint(0,800)
        self.comet_event = comet_event
    
    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verifier si le nombres de comets et de 0
        if len(self.comet_event.all_comets) == 0 : 
            print("l'evenement est fini")
            self.comet_event.reset_percent()
            #apparaitre les 2 premier monstre :
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    
    def fall(self):
        self.rect.y += self.velocity
        #ne tombe pas sur le sole :
        if self.rect.y > 500:
            print("sol")
            self.remove()

            #s'il n'y a plus de boule de feu on fais 
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                #remet la jauge au depart
                
                self.comet_event.fall_mode = False


        

        #verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self,self.comet_event.game.all_players
        ):
            print("joueur touché !")
            self.remove()
            #subir 20 coup de dégat
            self.comet_event.game.player.damage(20)





            


