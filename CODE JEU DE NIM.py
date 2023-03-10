# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:41:13 2022

@author: Thomas
"""
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

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'événement est fermeture de fenêtre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu")
    #détecter touche enfoncée        
        if event.type == pygame.KEYDOWN:
            print("A key has been pressed")
            if event.key == pygame.K_1:
                print("1")
            if event.key == pygame.K_2:
                print("2")
            if event.key == pygame.K_3:
                print("3")


def saisirValeur(N):
    valeur = 0
    valeurLegale =(1,2,3)

    while valeur not in valeurLegale:
        valeur = int(input("Entre 1 et 3 : "))
        if(N-valeur<0):
            print("Ptit malin, il y a moins d'allumette ")
            valeur = 0
    return valeur

def checkageVictoire(J,N):
    if(N>0):
        print("Tour ",J,": il reste :",N)
    else:
        print(J, " : Bravo tu as gagné ")
        sys.exit(0)

def joueurs(n):
    J1 = input("Nom du joueur 1 :")
    J2 = input("Nom du joueur 2 :")
    N = 21
    while N > 0 :
        print(J1, " à ton tour")
        tourAllu = saisirValeur(N)
        N -= tourAllu
        checkageVictoire(J2,N)

        print(J2," a ton tour")
        tourAllu = saisirValeur(N)
        N -= tourAllu
        checkageVictoire(J1, N)


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

