import pygame
pygame.init()
import math
from player import player
from game import Game
from projectile import projectile




#générer la fenetre de notre jeu
pygame.display.set_caption("comet fall game")
screen =pygame.display.set_mode((1080,720))

#importer et charger l'arriere plan de notre jeu
bg=pygame.image.load("Asset/bg.jpg")


#importer notre banniere de notre jeu
banner = pygame.image.load("Asset/banner.png")
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importer notre bouton pour lancer la partie:
play_button = pygame.image.load("Asset/button.png")
play_button =  pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)




#charger notre jeux

game = Game()

runinng = True

#boucle tant que cette condition est vrai:

while runinng:

    #appliquer l'arriere plan de notre jeu
    
    screen.blit(bg,(0,-200))

    #verifier si notre jeu à commencer 
    if game.is_playing:
        #declancher les instruction de la partie
        game.update(screen)
    
    #verifier si  notre jeu n'à pas  commencer 
    else:
        #ajouter mon écran de bienvenu
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)
        


    #mettre ajour l'écran 
    pygame.display.flip()
    
    #si le joueur ferme cette fénétre 
    for event in pygame.event.get():
        
        #L'evenement fermeture de l'environement

        if event.type == pygame.QUIT:
            runinng = False
            pygame.quit()
        
        #detecter si un joeur lacher une touche du clavier

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclencher pour lancer les projectile
            if event.key == pygame.K_SPACE:
                game.player.lanch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souri est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #Lancer le jeu
                game.start()




