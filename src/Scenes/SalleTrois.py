from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleTrois(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Salle 3")
        self.setBackground("SalleTrois.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteGrossesalle())
        #self.ajouterObjet(PC())


class PorteGrossesalle(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleTrois/PorteGrosseSalle.jpg",x=20,y=14,onHoverCursor="FlecheGauche")

    def onClick(self):
        self.ordonnerAction("changerScene","GrosseSalle")

