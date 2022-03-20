from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleQuatre(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Salle 4")
        self.setBackground("SalleQuatre.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirCinq())

        
class PorteCouloirCinq(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleQuatre/PorteCouloirCinq.jpg",x=0,y=0)

    def onClick(self):
        self.ordonnerAction("changerScene","CouloirCinq")


