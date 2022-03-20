import pygame

from src.Commun.LoadingManager import *

class Curseur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mouse.set_visible(0)
        self.x = 0
        self.y = 0
        self.setImage("Curseur/defaut.png")
        self.type = "Defaut"

    def setPosition(self,x,y):
        self.x=x
        self.y=y
        self.rect.topleft = (x,y)

    def setImage(self,nomImage):
        chemin = "Images/Objets/"+nomImage
        self.image = loadImage(chemin,True)
        self.rect = self.image.get_rect()
        self.setPosition(self.x,self.y)

    def actualiser(self,typeObjet):
        if typeObjet is not self.type:
            if typeObjet == "Dialogue":
                self.setImage("Curseur/dialogue.png")
                self.type = typeObjet
            elif typeObjet == "Loupe":
                self.setImage("Curseur/loupe.png")
                self.type = typeObjet
            elif typeObjet == "FlecheHaut":
                self.setImage("Curseur/fleche_haut.png")
                self.type = typeObjet
            elif typeObjet == "FlecheBas":
                self.setImage("Curseur/fleche_bas.png")
                self.type = typeObjet
            elif typeObjet == "FlecheGauche":
                self.setImage("Curseur/fleche_gauche.png")
                self.type = typeObjet
            elif typeObjet == "FlecheDroite":
                self.setImage("Curseur/fleche_droite.png")
                self.type = typeObjet
            elif typeObjet == "Defaut":
                self.setImage("Curseur/defaut.png")
                self.type = typeObjet
            else:
                print("Attention, typeObjet invalide:",typeObjet)

    def draw(self,surface):
        surface.blit(self.image, self.rect)
