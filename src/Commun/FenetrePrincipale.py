import pygame
from pygame.locals import *

from src.Enigmes.EnigmeUne import *
from src.Enigmes.RoiDeLaGlisse import *
from src.Enigmes.JourApresJour import *
from src.Enigmes.Infirmiere import *

from src.Scenes.CombinaisonsEquipage import *
from src.Scenes.CouloirUn import *
from src.Scenes.Menu import *
from src.Scenes.Pilote import *
from src.Scenes.SalleUne import *
from src.Scenes.Vaisseau import *
from src.Scenes.DigicodeUn import *
from src.Scenes.DigicodeDeux import *
from src.Scenes.DigicodeTrois import *
from src.Scenes.SalleControle import *
from src.Scenes.CouloirDeux import *
from src.Scenes.SalleDeux import *
from src.Scenes.GrosseSalle import *
from src.Scenes.CouloirTrois import *
from src.Scenes.SalleSoins import *
from src.Scenes.SalleTrois import *
from src.Scenes.CouloirCinq import *
from src.Scenes.SalleRepos import *
from src.Scenes.ChambreUne import *
from src.Scenes.SalleQuatre import *
from src.Scenes.Generateur import *
from src.Scenes.SalleFinale import *

class FenetrePrincipale:

    nomJeu = "Cosmoscape"
    
    dictScenes = {"EnigmeUne":EnigmeUne,
                  "RoiDeLaGlisse":RoiDeLaGlisse,
                  #"A_contretemps":A_contretemps,
                  "JourApresJour":JourApresJour,
                  "Infirmiere":Infirmiere,
                  "CombinaisonsEquipage":SceneCombinaisonsEquipage,
                  "CouloirUn":SceneCouloirUn,
                  "Menu":SceneMenu,
                  "Pilote":ScenePilote,
                  "SalleUne":SceneSalleUne,
                  "DigicodeUn":SceneDigicodeUn,
                  "DigicodeDeux":SceneDigicodeDeux,
                  "DigicodeTrois":SceneDigicodeTrois,
                  "Vaisseau":SceneVaisseau,
                  "SalleControle":SceneSalleControle,
                  "CouloirDeux":SceneCouloirDeux,
                  "GrosseSalle":SceneGrosseSalle,
                  "SalleDeux":SceneSalleDeux,
                  "CouloirTrois":SceneCouloirTrois,
                  "SalleSoins":SceneSalleSoins,
                  "SalleTrois":SceneSalleTrois,
                  "CouloirCinq":SceneCouloirCinq,
                  "ChambreUne":SceneChambreUne,
                  "SalleRepos":SceneSalleRepos,
                  "Generateur":SceneGenerateur,
                  "SalleQuatre":SceneSalleQuatre,
                  "SalleFinale":SceneSalleFinale,
                  }
  
    def __init__(self):
        framerate = 30
        self.tempsParFrame = int(1000/framerate)
        self.ecran = pygame.display.set_mode((1280, 720))
        self.positionCurseur = (0,0)
        self.curseur = Curseur()
        self.chargerMusique()
        self.changerScene("Menu")
        
    def changeTitre(self,nouveauTitre):
        nouveauTitre = self.nomJeu+" - "+nouveauTitre
        pygame.display.set_caption(nouveauTitre)

    def changerScene(self,nomScene):
        print("Nom de scene changée:",nomScene)
        self.scene = self.dictScenes[nomScene]()
        self.changeTitre(nomScene)
        self.bougerCurseur()
        
    def chargerMusique(self):
        try:
            pygame.mixer.init()
        except:
            return
        pygame.mixer.music.load('Musique/After_Dark.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def arreteMusique(self):
        if pygame.mixer.get_init():
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            
    def exec(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    self.arreteMusique()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    #Le bouton a l'index 1 est le clic gauche
                    if event.__dict__["button"] == 1:
                        self.scene.click(event.__dict__["pos"])
                elif event.type == MOUSEMOTION:
                    self.positionCurseur=event.__dict__["pos"]
                    self.bougerCurseur()
                elif event.type == USEREVENT:
                    if "changerScene" in event.__dict__:
                        self.changerScene(event.__dict__["changerScene"])
                    else:
                        self.scene.manageEvent(event)
            self.draw()
            pygame.display.flip()
            self.scene.onFrameUpdate()
            pygame.time.wait(self.tempsParFrame)

    def draw(self):
        self.scene.draw(self.ecran)
        self.curseur.draw(self.ecran)
        
    def bougerCurseur(self):
        typeObjet = self.scene.getCurrentObjectType(self.positionCurseur)
        self.curseur.setPosition(self.positionCurseur[0],self.positionCurseur[1])
        self.curseur.actualiser(typeObjet)
