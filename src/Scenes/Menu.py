from pygame.locals import *

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *
from src.Commun.SaveManager import *

class BoutonNouvellePartie(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="Menu/BoutonNP.jpg",x=461,y=200)

    def onClick(self):
        self.ordonnerAction("changerScene","Pilote")

class BoutonContinuer(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="Menu/BoutonContinuer.jpg",x=632,y=335)

    def onClick(self):
        scene = SaveManager().obtenirSceneActuelle()
        self.ordonnerAction("changerScene",scene)
        
class BoutonQuitter(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="Menu/BoutonQuitter.jpg",x=679,y=478)

    def onClick(self):
        evt = pygame.event.Event(QUIT)
        pygame.event.post(evt)

class BoutonMusique(Objet):
    def __init__(self):
        Objet.__init__(self,nomImage="Menu/BoutonMusiqueOn.jpg",x=0,y=579)

    def onClick(self):
        if pygame.mixer.get_init():
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                self.setImage("Menu/BoutonMusiqueOff.jpg")
            else:
                pygame.mixer.music.play()
                self.setImage("Menu/BoutonMusiqueOn.jpg")

            
class SceneMenu(Scene):
    
    def __init__(self):
        Scene.__init__(self,nom="Menu")
        self.setBackground("Menu.jpg")
        self.ajouterObjet(BoutonNouvellePartie())
        self.ajouterObjet(BoutonContinuer())
        self.ajouterObjet(BoutonQuitter())
        self.ajouterObjet(BoutonMusique())
