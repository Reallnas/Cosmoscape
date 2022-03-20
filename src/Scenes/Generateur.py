from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneGenerateur(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Générateur")
        self.setBackground("Generateur.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirCinq())
        
class PorteCouloirCinq(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="Generateur/PorteCouloirCinq.jpg",x=665,y=200,onHoverCursor="FlecheHaut")

    def onClick(self):
        self.ordonnerAction("changerScene","CouloirCinq")
