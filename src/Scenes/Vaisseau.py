from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneVaisseau(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Vaisseau")
        self.setBackground("Vaisseau.jpg")
        self.sauvegarderScene()
        self.ajouterDialogue("vaisseau",action="avancerHistoire")
        self.ouvrirDialogue("vaisseau")

    def actionsDialogue(self,action):
        if "avancerHistoire" in action:
            self.ordonnerAction("changerScene","SalleUne")
