# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:41:13 2022

@author: Thomas
"""
import sys
def saisirValeur(N):
    valeur = 0
    valeurLegale =(1,2,3)
    
    while valeur not in valeurLegale:
        valeur = int(input("Entre 1 et 3 : "))
        if(N-valeur<0):
            print("Ptit malin, il y a moins d'allumette ")
            valeur = 0
    return valeur

def checkageVictoire(J,OUI):
    if(OUI>0):
        print("Tour ",J,": il reste :",OUI)
    else:
        print(J, " : Bravo tu as gagné ")
        sys.exit(0)
    
J1 = input("Nom du joeur 1 :")
J2 = input("Nom du joeur 2 :")   
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
