from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class PorteSalleControle(Objet):
    
    def __init__(self):
        Objet.__init__(self,nomImage="CouloirUn/PorteSalleControleDetruite.jpg",x=480,y=240,onHoverCursor="FlecheHaut")

    def onClick(self):
        self.ordonnerAction("changerScene","DigicodeUn")
    

class ZoneSalleUne(Objet):
    
    def __init__(self):
        Objet.__init__(self,nomImage="CouloirUn/ZoneSalleUne.jpg",x=62,y=567,onHoverCursor="FlecheBas")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleUne")
        
        
class SceneCouloirUn(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="CouloirUn")
        self.setBackground("CouloirUn.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleControle())
        self.ajouterObjet(ZoneSalleUne())
        self.ajouterDialogue("robot",police="Courier New",action="finDialogueRobot")
        if not self.estDialogueDejaAffiche(1):
            self.ouvrirDialogue("robot")

    def actionsDialogue(self,action):
        if "finDialogueRobot" in action:
            self.sauvegarderDialogueDejaAffiche(1)
