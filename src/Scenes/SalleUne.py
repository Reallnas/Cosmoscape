from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

from src.Commun.SaveManager import *

class PorteCombinaisonsEquipage(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleUne/PorteCombinaisonsEquipage.jpg",
                       x=0,y=321,onHoverCursor="FlecheGauche")

    def onClick(self):
        self.ordonnerAction("changerScene","CombinaisonsEquipage")

class PorteCouloirUn(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="SalleUne/PorteCouloirUn.jpg",
                       x=1143,y=253,onHoverCursor="FlecheDroite")

    def onClick(self):
        enigmeReussie = SaveManager().obtenirEtatEnigmePartieActuelle(1)
        if enigmeReussie:
            self.ordonnerAction("changerScene","CouloirUn")
        else:
            self.ordonnerAction("ouvrirDialogue","porte_bloquee")
        
class SceneSalleUne(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="SalleUne")
        self.setBackground("SalleUne.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCombinaisonsEquipage())
        self.ajouterObjet(PorteCouloirUn())
        self.ajouterDialogue("arrivée",action="allerDialogueRobot")
        self.ajouterDialogue("robot",police="Courier New",action="finDialogueRobot")
        self.ajouterDialogue("porte_bloquee",action="ouvrirEnigme")
        if not self.estDialogueDejaAffiche(0):
            self.ouvrirDialogue("arrivée")

    def actionsDialogue(self,action):
        if "allerDialogueRobot" in action:
            self.ouvrirDialogue("robot")
            
        if "finDialogueRobot" in action:
            self.sauvegarderDialogueDejaAffiche(0)

        if "ouvrirEnigme" in action:
            self.ordonnerAction("changerScene","EnigmeUne")
