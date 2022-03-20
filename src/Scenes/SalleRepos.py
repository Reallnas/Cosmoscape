from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleRepos(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Salle De Repos")
        self.setBackground("SalleRepos.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteChambreUne())
        self.ajouterObjet(PorteGrosseSalle())
        
class PorteChambreUne(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleRepos/PorteChambreUne.jpg",x=873,y=81,onHoverCursor="FlecheDroite")

    def onClick(self):
        self.ordonnerAction("changerScene","ChambreUne")


class PorteGrosseSalle(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleRepos/PorteGrosseSalle.jpg",x=6,y=233,onHoverCursor="FlecheGauche")

    def onClick(self):
        self.ordonnerAction("changerScene","GrosseSalle")

