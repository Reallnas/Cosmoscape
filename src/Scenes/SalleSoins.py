from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleSoins(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="SalleSoins")
        self.setBackground("SalleSoins.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirTrois())
        


class PorteCouloirTrois(Objet):

    def __init__(self):
        Objet.__init__(self,nomImage="SalleSoins/PorteCouloirTrois.jpg",x=0,y=21,onHoverCursor="FlecheGauche")

    def onClick(self):
        self.ordonnerAction("changerScene","CouloirTrois")
	 

