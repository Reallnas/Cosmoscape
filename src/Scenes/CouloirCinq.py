from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneCouloirCinq(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Couloir 5")
        self.setBackground("CouloirCinq.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleFinale())
        self.ajouterObjet(PorteGenerateur())
        self.ajouterObjet(PorteGrosseSalle())


class PorteSalleFinale(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="CouloirCinq/PorteSalleFinale.jpg",x=413,y=270,onHoverCursor="FlecheHaut")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleFinale")


class PorteGenerateur(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="CouloirCinq/PorteGenerateur.jpg",x=1115,y=50,onHoverCursor="FlecheDroite")

    def onClick(self):
        self.ordonnerAction("changerScene","DigicodeTrois")
        
class PorteGrosseSalle(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="CouloirCinq/PorteGrosseSalle.jpg",x=260,y=594,onHoverCursor="FlecheBas")

    def onClick(self):
        self.ordonnerAction("changerScene","GrosseSalle")
