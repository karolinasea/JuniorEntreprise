# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:44:01 2019

@author: carole
"""

import Document.py
import Facture.py
import Convention.py

#initialisation des listes de factures et convention
#ce sont des listes d'objets de type Convention et de type facture
listeFacture = []
listeConvention = []

#fonctions pour gerer les listes de convention et de facture

#on ajoute une convention a la liste de convention
def ajouterConvention(convention):
    listeConvention.append(convention)
    
#on ajoute une facture a la liste de facture
def ajouterFacture(facture):
    listeFacture.append(facture)

#getNbMissonsFinies
def getNbMissionsTerminees():
    nb = 0
    for convention in listeConvention:
        if convention.getStatut()=="Terminee":
            nb = nb + 1
    return nb

#getNbMissionsEnCours
def getNbMissionsEnCours():
    nb = 0
    for convention in listeConvention:
        if convention.getStatut()=="En cours":
            nb = nb + 1
    return nb

#affiche la convention dont on a chercher le numero dans la recherche
def RechercheViaNumeroConvention(numeroConvention):
    for convention in listeConvention:
        if convention.getNumeroConvention()==numeroConvention:
            #affichera sa dans une table qu on construira avec Kivy si on a le temps ..
            print(convention.getNumeroConvention() + " " + convention.getDate() + convention.getNomClient() + convention.getNomEtudiant() + convention.getStatut() + ) 
            # + get facture status but how????
            

#rechercheParClient

#rechercheParEtudiant
            
#rechercheParAnnee






    
        

