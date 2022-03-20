from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneGrosseSalle(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Grosse Salle")
        self.setBackground("GrosseSalle.jpg")
        self.sauvegarderScene()
        self.ajouterObjet(PorteCouloirDeux())
        self.ajouterObjet(PorteSalleTrois())
        self.ajouterObjet(PorteCouloirCinq())
        self.ajouterObjet(PorteSalleRepos())
        

class PorteCouloirDeux(Objet):
     def __init__(self):
         Objet.__init__(self,nomImage="GrosseSalle/PorteCouloirDeux.jpg",x=0,y=572,onHoverCursor="FlecheBas")

     def onClick(self):
        self.ordonnerAction("changerScene","CouloirDeux")

class PorteSalleTrois(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="GrosseSalle/PorteSalleTrois.jpg",x=14,y=258,onHoverCursor="FlecheGauche")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleTrois")

class PorteCouloirCinq(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="GrosseSalle/PorteCouloirCinq.jpg",x=714,y=332,onHoverCursor="FlecheHaut")

    def onClick(self):
        self.ordonnerAction("changerScene","CouloirCinq")
	 
class PorteSalleRepos(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="GrosseSalle/PorteSalleRepos.jpg",x=1076,y=312,onHoverCursor="FlecheDroite")

    def onClick(self):
        self.ordonnerAction("changerScene","SalleRepos")
