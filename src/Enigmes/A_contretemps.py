import pygame

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *


class BoutonDescription(Objet):
    def __init__(self):
        Objet.__init__(self,"question_mark.jpg",x=10,y=10)

    def onClick(self):
        self.ordonnerAction("ouvrirDescription")
  
class Zero(Objet):
    def __init__(self):
        Objet.__init__(self,"Zero.jpg",x=0,y=0,numero=0)
        self.numero = numero

    def onClick(self):
        self.ordonnerAction("ActualiserNumeroActif",numero)
        self.ordonnerAction("ChangerNumero",1)
        
class Un(Objet):
    def __init__(self):
        Objet.__init__(self,"Un.jpg",x=0,y=0,numero=1)
        self.numero = numero

    def onClick(self):
        self.ordonnerAction("ActualiserNumeroActif",numero)
        self.ordonnerAction("ChangerNumero",2)

class Deux(Objet):
    def __init__(self):
        Objet.__init__(self,"Deux.jpg",x=0,y=0,numero=2)
        self.numero = numero

    def onClick(self):
        self.ordonnerAction("ActualiserNumeroActif",numero)
        self.ordonnerAction("ChangerNumero",0)
        
       
class A_contretemps(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="A_contretemps")
        self.setBackground("A_contretemps.jpg")
        self.ajouterDialogue("description")
        self.ajouterObjet(BoutonDescription())
        self.ajouterObjet(Zero())
        Zero.setVisibility = True
        self.ajouterObjet(Un())
        Un.setVisibility = False
        self.ajouterObjet(Deux())
        Deux.setVisibility = False
        self.numeroActif = 0
        
    def listeNumeros1(self):
        liste=[Zero(520,500,0),Un(520,500,1),Deux(520,500,1)]
        return liste

    def actionsEvent(self,dictionnaire):
        if "ouvrirDescription" in dictionnaire:
            self.ouvrirDialogue("description")
        if "ActualiserNumeroActif" in dictionnaire:
            self.numeroActif = listeNumeros1[dictionnaire["ActualiserNumeroActif"]]
        if "ChangerNumero" in dictionnaire:
            
            
