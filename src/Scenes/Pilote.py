from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class ScenePilote(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Pilote")
        self.setBackground("Pilote.jpg")
        self.sauvegarderScene()
        self.ajouterDialogue("debut",action="allerDialogue1")
        self.ajouterDialogue("robot",action="allerDialogue2",police="Courier New")
        self.ajouterDialogue("reponse",action="avancerHistoire")
        self.ouvrirDialogue("debut")

    def actionsDialogue(self,action):
        if "allerDialogue1" in action:
            self.ouvrirDialogue("robot")
        elif "allerDialogue2" in action:
            self.ouvrirDialogue("reponse")
        elif "avancerHistoire" in action:
            self.ordonnerAction("changerScene","Vaisseau")
