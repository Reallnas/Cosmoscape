import pygame

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *


class BoutonDescription(Objet):
    def __init__(self):
        Objet.__init__(self,"question_mark.jpg",x=10,y=10)

    def onClick(self):
        self.ordonnerAction("ouvrirDescription")
  
class chiffre18(Objet):
    def __init__(self,x=184,y=154,numero=False):
        Objet.__init__(self,"Infirmiere/18.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)
        
class chiffre38(Objet):
    def __init__(self,x=540,y=153,numero=False):
        Objet.__init__(self,"Infirmiere/38.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre69(Objet):
    def __init__(self,x=901,y=154,numero=True):
        Objet.__init__(self,"Infirmiere/69.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre29(Objet):
    def __init__(self,x=182,y=331,numero=False):
        Objet.__init__(self,"Infirmiere/29.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre49(Objet):
    def __init__(self,x=531,y=329,numero=False):
        Objet.__init__(self,"Infirmiere/49.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre65(Objet):
    def __init__(self,x=898,y=329,numero=False):
        Objet.__init__(self,"Infirmiere/65.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre33(Objet):
    def __init__(self,x=177,y=510,numero=False):
        Objet.__init__(self,"Infirmiere/33.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre54(Objet):
    def __init__(self,x=541,y=510,numero=False):
        Objet.__init__(self,"Infirmiere/54.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)

class chiffre71(Objet):
    def __init__(self,x=891,y=506,numero=False):
        Objet.__init__(self,"Infirmiere/71.jpg",x,y,numero)
        self.numero = numero
        
    def onClick(self):
        self.ordonnerAction("Verifier",self.numero)
       
class Infirmiere(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Infirmiere")
        self.setBackground("Infirmiere.jpg")
        self.ajouterDialogue("description")
        self.ajouterDialogue("faux")
        self.ajouterDialogue("vrai")
        self.ajouterObjet(BoutonDescription())
        self.ajouterObjet(chiffre18())
        self.ajouterObjet(chiffre38())
        self.ajouterObjet(chiffre69())
        self.ajouterObjet(chiffre29())
        self.ajouterObjet(chiffre49())
        self.ajouterObjet(chiffre65())
        self.ajouterObjet(chiffre33())
        self.ajouterObjet(chiffre54())
        self.ajouterObjet(chiffre71())
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
                
        

            
