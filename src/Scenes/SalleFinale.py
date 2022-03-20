from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneSalleFinale(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="SalleFinale")
        self.setBackground("SalleFinale.jpg")
        self.sauvegarderScene()
        self.ajouterDialogue("Final",action="enigmeFinale")
        self.ouvrirDialogue("Final")

    def actionsDialogue(self,action):
        if "enigmeFinal" in action:
            self.ordonnerAction("changerScene","JourApresJour")

        

