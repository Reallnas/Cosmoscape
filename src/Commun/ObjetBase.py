import pygame
from pygame.locals import *

from src.Commun.LoadingManager import *

class Objet(pygame.sprite.Sprite):
    def __init__(self,nomImage,x=0,y=0,transparence=False,
                 onHoverCursor="Defaut",visible=True):
        pygame.sprite.Sprite.__init__(self)
        self.visibility = visible
        self.onHoverCursor = onHoverCursor
        self.rect = pygame.Rect(x,y,0,0)
        self.setImage(nomImage,transparence)

    def ordonnerAction(self,nomAction,valeurAction=""):
        dictarg = {nomAction:valeurAction}
        evt = pygame.event.Event(USEREVENT,dictarg)
        pygame.event.post(evt)

    def draw(self,surface):
        if self.visibility == True:
            surface.blit(self.image, self.rect)
        
    def onClick(self):
        return

    def setPosition(self,x,y):
        self.rect.topleft = (x,y)

    def getPosition(self):
        return (self.rect.x,self.rect.y)
        
    def getRect(self):
        return self.rect

    def setVisibility(self,visible):
        self.visibility = visible

    def getVisibility(self):
        return self.visibility
        
    def setImage(self,nomImage,transparent=False):
        chemin = "Images/Objets/"+nomImage
        self.image = loadImage(chemin,transparent)
        oldRect = self.rect
        self.rect = self.image.get_rect()
        self.setPosition(oldRect.x,oldRect.y)

    def getOnHoverCursor(self):
        return self.onHoverCursor

    def setOnHoverCursor(self,nouveauType):
        self.onHoverCursor = nouveauType
