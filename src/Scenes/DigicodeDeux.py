from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class SceneDigicodeDeux(Scene):
    k=-1
    def __init__(self):
        Scene.__init__(self,nom="DigicodeDeux")
        self.setBackground("Digicode.jpg")
        self.sauvegarderScene()
        self.liste=[0,0,0,0]
        self.solution=[6,3,0,9]
        k=-1
        self.k=k
        self.ajouterObjet(Nombre(600,525,0))
        self.ajouterObjet(Nombre(471,377,1))
        self.ajouterObjet(Nombre(600,377,2))
        self.ajouterObjet(Nombre(730,377,3))
        self.ajouterObjet(Nombre(471,228,4))
        self.ajouterObjet(Nombre(600,228,5))
        self.ajouterObjet(Nombre(730,228,6))
        self.ajouterObjet(Nombre(471,80,7))
        self.ajouterObjet(Nombre(600,80,8))
        self.ajouterObjet(Nombre(730,80,9))
        self.ajouterObjet(Vrai(730,525))
        self.ajouterObjet(Croix(471,525))
        self.ajouterObjet(Retour(70,320))
        self.ajouterDialogue("faux",police="Courier New")

    def actionsEvent(self,dictionnaire):
        if "Placer" in dictionnaire:
           if self.k<3:
               self.k=self.k+1
               self.liste[self.k]=dictionnaire["Placer"]
               print(self.liste)

        if "Annuler" in dictionnaire:
            if self.k>-1:
                self.liste[self.k]=0
                self.k=self.k-1
                print(self.liste)

        if "Verifier" in dictionnaire:
            if self.liste==self.solution:
                self.ordonnerAction("changerScene","GrosseSalle")
            else:
                self.ouvrirDialogue("faux")

        if "Retour" in dictionnaire:
            self.ordonnerAction("changerScene","CouloirDeux")

            

class Nombre(Objet):

    def __init__(self,x=0,y=0,numero=0):
        nomImage = "Digicode/"+str(numero)+".jpg"
        Objet.__init__(self,nomImage,x,y)
        self.numero=numero

    def onClick(self):
        self.ordonnerAction("Placer",self.numero)
        	 

class Croix(Objet):

    def __init__(self,x=0,y=0):
        Objet.__init__(self,"Digicode/Croix.jpg",x,y)

    def onClick(self):
        self.ordonnerAction("Annuler")

class Vrai(Objet):

    def __init__(self,x=0,y=0):
        Objet.__init__(self,"Digicode/Vrai.jpg",x,y)

    def onClick(self):
        self.ordonnerAction("Verifier")

class Retour(Objet):
    def __init__(self,x=0,y=0):
        Objet.__init__(self,"Digicode/Retour.jpg",x,y)

    def onClick(self):
        self.ordonnerAction("Retour")
