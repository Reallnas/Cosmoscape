import pygame

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *


class BoutonDescription(Objet):
    def __init__(self):
        Objet.__init__(self,"question_mark.jpg",x=10,y=10)

    def onClick(self):
        self.ordonnerAction("ouvrirDescription")
  
class SourceElectricite(Objet):
    def __init__(self,direction=0,x=0,y=0,abscisse=0,ordonnee=0):
        #Direction: 0=Haut,1=droite,2=Bas,3=Gauche
        Objet.__init__(self,"sourceElec.jpg",x,y,True)
        self.direction=direction
        self.abscisse=abscisse
        self.ordonnee=ordonnee
        self.rotate()
        self.ordonnerAction("majTableau",(self.abscisse,self.ordonnee,self.direction))
        
    def rotate(self):
        self.image = pygame.transform.rotate(self.image,self.direction*(-90))

class CableElectricite(Objet):
    def __init__(self,direction,x=0,y=0,abscisse=0,ordonnee=0):
        Objet.__init__(self,"cableAllume.jpg",x,y,True)
        self.abscisse=abscisse
        self.ordonnee=ordonnee
        self.direction=direction
        self.ordonnerAction("majTableau",(self.abscisse,self.ordonnee,self.direction))

    def onClick(self):
        if self.direction >=1:
            self.direction = 0
        else:
            self.direction+=1
        self.rotate()
        self.ordonnerAction("majTableau",(self.abscisse,self.ordonnee,self.direction))
        
    def rotate(self):
        self.image = pygame.transform.rotate(self.image,-90)

class CableDroite(Objet):
    def __init__(self,direction,x=0,y=0,abscisse=0,ordonnee=0):
        Objet.__init__(self,"cableDroite.jpg",x,y,True)
        self.abscisse=abscisse
        self.ordonnee=ordonnee
        self.direction=direction
        self.ordonnerAction("majTableau",(self.abscisse,self.ordonnee,self.direction))

    def onClick(self):
        if  self.direction>=3 :
            self.direction = 0
        else:
            self.direction+=1
        self.rotate()
        self.ordonnerAction("majTableau",(self.abscisse,self.ordonnee,self.direction))
        
    def rotate(self):
        self.image = pygame.transform.rotate(self.image,-90)
        
class EnigmeUne(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="EnigmeUne")
        self.setBackground("testEnigme.jpg")
        self.ajouterDialogue("description")
        self.ajouterObjet(BoutonDescription())
        
        self.solution = [[1,0,1,0,0],[0,0,3,1,0],[0,0,0,3,3]]
        self.etatActuel = [[True,False,False,True,True],[True,True,False,False,True],[True,True,True,False,True]]
        self.ajouterObjet(SourceElectricite(1,100,100,0,0))
        self.ajouterObjet(CableElectricite(1,300,100,1,0))
        self.ajouterObjet(CableDroite(0,500,100,2,0))
        self.ajouterObjet(CableDroite(0,482,300,2,1))
        self.ajouterObjet(CableDroite(0,682,300,3,1))
        self.ajouterObjet(CableDroite(0,665,500,3,2))
        self.ajouterObjet(SourceElectricite(3,865,500,4,2))

    def actionsEvent(self,dictionnaire):
        if "ouvrirDescription" in dictionnaire:
            self.ouvrirDialogue("description")
        if "majTableau" in dictionnaire:
            abscisse = dictionnaire["majTableau"][0]
            ordonnee = dictionnaire["majTableau"][1]
            etat = dictionnaire["majTableau"][2]
            print(etat)
            self.etatActuel[ordonnee][abscisse] = etat == self.solution[ordonnee][abscisse]
            reussi = True
            for lignes in self.etatActuel:
                for etats in lignes:
                    if not etats:
                        reussi = False
            if reussi:
                self.reussite()
                
    def reussite(self):
        self.sauvegarderEnigmeReussie(1)
        self.ordonnerAction("changerScene","CouloirUn")
                
