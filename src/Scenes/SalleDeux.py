from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleDeux(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="SalleDeux")
        self.setBackground("SalleDeux.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirTrois())
        self.ajouterObjet(PorteCouloirDeux())
        

class PorteCouloirTrois(Objet):

    def __init__(self):
        Objet.__init__(self,nomImage="SalleDeux/PorteCouloirTrois.jpg",x=1136,y=77,onHoverCursor="FlecheDroite")

    def onClick(self):
        self.ordonnerAction("changerScene","CouloirTrois")
        

class PorteCouloirDeux(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="SalleDeux/PorteCouloirDeux.jpg",x=0,y=0,onHoverCursor="FlecheGauche")

     def onClick(self):
        self.ordonnerAction("changerScene","CouloirDeux")

	 

