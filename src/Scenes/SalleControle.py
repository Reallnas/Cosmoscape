from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleControle(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="SalleControle")
        self.setBackground("SalleControle.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirDeux())
        self.ajouterObjet(PorteCouloirUn())
        

class PorteCouloirDeux(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="SalleControle/PorteCouloirDeux.jpg",x=1083,y=11,onHoverCursor="FlecheDroite")

     def onClick(self):
        self.ordonnerAction("changerScene","CouloirDeux")
	 

class PorteCouloirUn(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="SalleControle/PorteCouloirUn.jpg",x=0,y=0,onHoverCursor="FlecheGauche")

     def onClick(self):
        self.ordonnerAction("changerScene","CouloirUn")
