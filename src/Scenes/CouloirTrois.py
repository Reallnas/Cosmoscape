from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneCouloirTrois(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="CouloirTrois")
        self.setBackground("CouloirTrois.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleSoins())
        self.ajouterObjet(PorteSalleDeux())
       

class PorteSalleSoins(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="CouloirTrois/PorteSalleSoins.jpg",x=438,y=108,onHoverCursor="FlecheHaut")

     def onClick(self):
        self.ordonnerAction("changerScene","SalleSoins")
	 

class PorteSalleDeux(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="CouloirTrois/PorteSalleDeux.jpg",x=0,y=572,onHoverCursor="FlecheBas")

     def onClick(self):
        self.ordonnerAction("changerScene","SalleDeux")
