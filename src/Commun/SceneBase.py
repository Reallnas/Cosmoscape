import pygame
from pygame.locals import *

from src.Commun.Curseur import *
from src.Commun.Dialogue import *
from src.Commun.LoadingManager import *
from src.Commun.SaveManager import *

class Scene:
    def __init__(self,nom="Defaut"):
        self.background = None
        self.nomScene = nom
        self.listeObjet = pygame.sprite.Group()
        self.listeDialogues = {}
        self.listeActions = {}
        self.dialogueActif = ""
        self.dialogueActifFini = True
        self.dialogueActifFerme = True

    def setBackground(self,nomImage):
        cheminImage = "Images/Backgrounds/" + nomImage
        self.background = loadImage(cheminImage)

    def ajouterObjet(self,objet):
        self.listeObjet.add(objet)

    def getObjet(self,position):
        for objet in self.listeObjet:
            if objet.getRect().collidepoint(position) and objet.getVisibility():
                return objet
        return None
    
    def click(self,positionSouris):
        if self.dialogueActifFerme:
            objet = self.getObjet(positionSouris)
            if objet is not None:
                objet.onClick()
        elif self.dialogueActifFini :
            action = self.fermerDialogue()
            self.actionsDialogue(action)
        else:
            self.avancerDialogue()
        
    def draw(self,surface):
        surface.blit(self.background, (0,0))
        #for objet in self.listeObjet:
            #self.ecran.blit(self.background, objet.getRect(), objet.getRect())
        for objet in self.listeObjet:
            objet.draw(surface)
        if not self.dialogueActifFerme :
            self.listeDialogues[self.dialogueActif].draw(surface)

    def sauvegarderScene(self):
        SaveManager().sauvegarderSceneActuelle(self.nomScene)

    def sauvegarderEnigmeReussie(self,numeroEnigme):
        SaveManager().sauvegarderEnigmeReussie(numeroEnigme)

    def estEnigmeReussie(self,numeroEnigme):
        return SaveManager().obtenirEtatEnigmePartieActuelle(numeroEnigme)

    def sauvegarderDialogueDejaAffiche(self,numeroDialogue):
        SaveManager().sauvegarderDialogueSpecial(numeroDialogue)

    def estDialogueDejaAffiche(self,numeroDialogue):
        return SaveManager().obtenirEtatDialogueSpecial(numeroDialogue)
    
    def ajouterDialogue(self,balise,police="Helvetica",action=""):
        nomFichier = "Dialogues/"+self.nomScene+".txt"
        self.listeDialogues[balise] = Dialogue(nomFichier,balise,police)
        self.listeActions[balise] = action

    def ouvrirDialogue(self,balise):
        if self.dialogueActifFerme :
            self.dialogueActif = balise
            self.dialogueActifFini = self.listeDialogues[balise].avancerTexte()
            self.dialogueActifFerme = False
        else:
            print("Impossible de commencer le dialogue",balise,"car un autre dialogue est ouvert!")
        
    def avancerDialogue(self):
        self.dialogueActifFini = self.listeDialogues[self.dialogueActif].avancerTexte()
        
    def fermerDialogue(self):
        self.listeDialogues[self.dialogueActif].retourAuDebut()
        self.dialogueActifFerme = True
        return self.listeActions[self.dialogueActif]
        
    def manageEvent(self,event):
        if "ouvrirDialogue" in event.__dict__:
            balise = event.__dict__["ouvrirDialogue"]
            self.ouvrirDialogue(balise)
        else:
            self.actionsEvent(event.__dict__)

    def ordonnerAction(self,nomAction,valeurAction=""):
        dictarg = {nomAction:valeurAction}
        evt = pygame.event.Event(USEREVENT,dictarg)
        pygame.event.post(evt)

    def actionsDialogue(self,action):
        return
    
    def actionsEvent(self,dictionnaire):
        return

    def onFrameUpdate(self):
        return

    def getCurrentObjectType(self,positionCurseur):
        typeObjet = "Defaut"
        if self.dialogueActifFerme:
            objet = self.getObjet(positionCurseur)
            if objet is not None:
                typeObjet = objet.getOnHoverCursor()
        else:
            typeObjet = "Dialogue"
        return typeObjet
