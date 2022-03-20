from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneCouloirDeux(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="CouloirDeux")
        self.setBackground("CouloirDeux.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleDeux())
        self.ajouterObjet(PorteGrosseSalle())
        self.ajouterObjet(PorteSalleControle())
        

class PorteSalleDeux(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="CouloirDeux/PorteSalleDeux.jpg",x=553,y=380,onHoverCursor="FlecheGauche")

     def onClick(self):
        self.ordonnerAction("changerScene","SalleDeux")
        

class PorteGrosseSalle(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="CouloirDeux/PorteGrosseSalle.jpg",x=870,y=348,onHoverCursor="FlecheHaut")

     def onClick(self):
        self.ordonnerAction("changerScene","DigicodeDeux")


class PorteSalleControle(Objet):
    
     def __init__(self):
         Objet.__init__(self,nomImage="CouloirDeux/PorteSalleControle.jpg",x=0,y=572,onHoverCursor="FlecheBas")

     def onClick(self):
        self.ordonnerAction("changerScene","SalleControle")
	 

