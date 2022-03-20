from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneChambreUne(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Chambre 1")
        self.setBackground("ChambreUne.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleRepos())


class PorteSalleRepos(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="ChambreUne/PorteSalleRepos.jpg",x=5,y=17,onHoverCursor="FlecheHaut")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleRepos")

