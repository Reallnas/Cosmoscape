from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class PorteSalleUne(Objet):
    
    def __init__(self):
        Objet.__init__(self,nomImage="CombinaisonsEquipage/PorteSalleUne.jpg",x=1134,y=122,onHoverCursor="FlecheDroite")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleUne")

class CombiUn(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="CombinaisonsEquipage/CombiUn.jpg",x=790,y=330,onHoverCursor="Loupe")

    def onClick(self):
        self.ordonnerAction("ouvrirDialogue","regarde")

class CombiDeux(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="CombinaisonsEquipage/CombiDeux.jpg",x=20,y=260,onHoverCursor="Loupe")

    def onClick(self):
        self.ordonnerAction("ouvrirDialogue","code")
        
class SceneCombinaisonsEquipage(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="CombinaisonsEquipage")
        self.setBackground("CombinaisonsEquipage.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteSalleUne())
        self.ajouterObjet(CombiUn())
        self.ajouterObjet(CombiDeux())
        self.ajouterDialogue("regarde")
        self.ajouterDialogue("code")
