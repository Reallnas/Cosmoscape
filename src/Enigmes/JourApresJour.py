import pygame

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *


class BoutonDescription(Objet):
    def __init__(self):
        Objet.__init__(self,"question_mark.jpg",x=10,y=10)

    def onClick(self):
        self.ordonnerAction("ouvrirDescription")
  
class Lundi(Objet):
    def __init__(self,x=33,y=154,jour=False):
        Objet.__init__(self,"JourApresJour/lundi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)
        
class Mardi(Objet):
    def __init__(self,x=399,y=154,jour=False):
        Objet.__init__(self,"JourApresJour/mardi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)

class Mercredi(Objet):
    def __init__(self,x=785,y=156,jour=False):
        Objet.__init__(self,"JourApresJour/mercredi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)

class Jeudi(Objet):
    def __init__(self,x=230,y=386,jour=False):
        Objet.__init__(self,"JourApresJour/jeudi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)

class Vendredi(Objet):
    def __init__(self,x=580,y=383,jour=False):
        Objet.__init__(self,"JourApresJour/vendredi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)

class Samedi(Objet):
    def __init__(self,x=171,y=613,jour=False):
        Objet.__init__(self,"JourApresJour/samedi.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)

class Dimanche(Objet):
    def __init__(self,x=606,y=611,jour=True):
        Objet.__init__(self,"JourApresJour/dimanche.jpg",x,y,jour)
        self.jour = jour
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.jour)
       
class JourApresJour(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="JourApresJour")
        self.setBackground("JourApresJour.jpg")
        self.ajouterDialogue("description")
        self.ajouterDialogue("faux")
        self.ajouterDialogue("vrai")
        self.ajouterObjet(BoutonDescription())
        self.ajouterObjet(Lundi())
        self.ajouterObjet(Mardi())
        self.ajouterObjet(Mercredi())
        self.ajouterObjet(Jeudi())
        self.ajouterObjet(Vendredi())
        self.ajouterObjet(Samedi())
        self.ajouterObjet(Dimanche())
        reussi = False

        
    def actionsEvent(self,dictionnaire):
        if "ouvrirDescription" in dictionnaire:
            self.ouvrirDialogue("description")
        if "Verifier" in dictionnaire:
            reussi = dictionnaire["Verifier"]
            if reussi == False :
                self.ouvrirDialogue("faux")
            if reussi == True :
                self.ouvrirDialogue("vrai")
                self.sauvegarderEnigmeReussie(1)
                self.ordonnerAction("changerScene","CouloirUn")
                

        

            
