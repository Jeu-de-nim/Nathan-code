#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     18/02/2023
# Copyright:   (c) Thomas 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import pygame

pygame.init()

# Générer la fenêtre de notre jeu
#titre de la fenêtre
pygame.display.set_caption("Jeu de nim")
#taille largeur sur longeur
screen = pygame.display.set_mode((1080,720))

#importer l'arrière plan
background = pygame.image.load("image_jeu/bg.png")

#importer carre
carre = pygame.image.load("image_jeu/carre.jpg")

carre1 = carre
carre1 = pygame.transform.scale(carre1,(200,210))
#changer taille carre
carre = pygame.transform.scale(carre,(25,40))

running = True


class Allumette(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image_jeu/allumette.png")
        self.image = pygame.transform.scale(self.image,(200,300))
        self.rect = self.image.get_rect()

allumette1 = Allumette()

#définir le style et la taille de la police
police = pygame.font.SysFont("monospace" ,45)

image_texte = police.render ( "Appuyer sur 1,2 ou 3", 1 , (255,0,255) )

texte_j = police.render ("Joueur   à ton tour", 1 , (255,0,255))

j1 = police.render ("1", 1 , (255,0,255))

j2 = police.render ("2", 1 , (255,0,255))

win_j1 = police.render ("Bravo joueur 1 ! Tu as gagné !", 1 , (255,0,255))

win_j2 = police.render ("Bravo joueur 2 ! Tu as gagné !", 1 , (255,0,255))

relancer = police.render ("Cliquer sur 1 pour relancer", 1 , (255,0,255))

while running :
    #appliquer l'arrière plan de notre jeu
    screen.blit(background,(0,0))

    #appliquer l'allumette
    o = -50
    for i in range(21):
        screen.blit(allumette1.image,(o,150))
        o+=50

    #appliquer le texte
    screen.blit(image_texte, (300,150))

    #appliquer texte_j
    screen.blit(texte_j,(350,200))

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'événement est fermeture de fenêtre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu")

    def checkageVictoire(J,N):
        if(N>0):
            print("Tour ",J,": il reste :",N)
        else:
            if J == "J2":
                screen.blit(win_j2, (100,240))
                screen.blit(relancer, (150,350))
                pygame.display.flip()
            else :
                screen.blit(win_j1,(100,240))
                screen.blit(relancer,(150,350))
                pygame.display.flip()


    N = 21 #c'est le nombre d'allumettes
    a = 0 #cette variable me sert juste à alterner entre le joueur 1 et 2
    b = 1065 #cordonée en x de départ de carre1
    while N >= 0 :
        if a % 2 == 0 :
            # afficher carre
            screen.blit(carre, (540,200))
            #afficher 1
            screen.blit(j1, (540,200))
            #mettre à jour l'affichage
            pygame.display.flip()
            for event in pygame.event.get():
            #détecter touche enfoncée
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        b -= 50
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 1
                        checkageVictoire("J2",N)
                        a += 1
                    elif event.key == pygame.K_2:
                        if N-2 >= 0 :
                            b -= 100
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 2
                            checkageVictoire("J2",N)
                            a += 1
                        else :
                            print("Il n'y a plus assez d'allumettes")
                    elif event.key == pygame.K_3:
                        if N-3 >= 0 :
                            b -= 150
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 3
                            checkageVictoire("J2",N)
                            a += 1
                        else :
                            print("Il n'y a plus assez d'allumettes")
                if event.type == pygame.QUIT :
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                    sys.exit()

        else :
            # afficher carre
            screen.blit(carre, (540,200))
            #afficher 2
            screen.blit(j2, (540,200))
            #mettre à jour l'affichage
            pygame.display.flip()
            for event in pygame.event.get():
            #détecter touche enfoncée
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        b -= 50
                        screen.blit(carre1,(b,240))
                        pygame.display.flip()
                        N -= 1
                        checkageVictoire("J1",N)
                        a += 1
                    elif event.key == pygame.K_2:
                        if N-2 >= 0 :
                            b -= 100
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 2
                            checkageVictoire("J1",N)
                            a += 1
                        else :
                            print("Il n'y a plus assez d'allumettes")
                    elif event.key == pygame.K_3:
                        if N-3 >= 0 :
                            b -= 150
                            screen.blit(carre1,(b,240))
                            pygame.display.flip()
                            N -= 3
                            checkageVictoire("J1",N)
                            a += 1
                        else :
                            print("Il n'y a plus assez d'allumettes")
                if event.type == pygame.QUIT :
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                    sys.exit()




"""
def saisirValeur(N):
    valeur = 0
    valeurLegale =(1,2,3)

    while valeur not in valeurLegale:
        valeur = int(input("Entre 1 et 3 : "))
        if(N-valeur<0):
            print("Ptit malin, il y a moins d'allumette ")
            valeur = 0
    return valeur






def jeu_avec_ordi(n):
    J1 = input("Nom du joueur 1 :")
    N = 21
    while N > 0 :
        print(J1, " à ton tour")
        tourAllu = saisirValeur(N)
        valeur = tourAllu
        N -= tourAllu
        checkageVictoire(("ia"),N)

        tourAllu = ia(N, valeur)
        N -= tourAllu
        checkageVictoire(J1, N)


def ia(N, valeur):
    if valeur == 1:
        return 3
    elif valeur == 2:
        return 2
    elif valeur == 3:
        return 1



a = int(input("Entrer 1 pour jouer contre l'IA ou 2 pour jouer à 2 joueurs : "))
if a == 2:
    joueurs(a)
elif a == 1:
    jeu_avec_ordi(a)
"""