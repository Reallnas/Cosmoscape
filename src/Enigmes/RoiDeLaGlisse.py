import pygame
import time

from src.Commun.ObjetBase import *
from src.Commun.SceneBase import *

class FlecheHaut(Objet):
    def __init__(self,x=0,y=0):
        Objet.__init__(self,"RoiDeLaGlisse/FlecheHaut.jpg",x=1000,y=300)
        
    def onClick(self):
        self.ordonnerAction("Monter")
        
class BoutonDescription(Objet):
    def __init__(self):
        Objet.__init__(self,"question_mark.jpg",x=10,y=10)

    def onClick(self):
        self.ordonnerAction("ouvrirDescription")


class Pingouin(Objet):
    def __init__(self,x=0,y=0,numeroPingouin=1):
        Objet.__init__(self,"RoiDeLaGlisse/pingouin.jpg",x,y,numeroPingouin)
        self.numeroPingouin = numeroPingouin
        self.x = x
        self.y = y
        
    def onClick(self):
        self.ordonnerAction("ActualiserPingouinActif",(self.x,self.y,self.numeroPingouin))
        

class Empereur(Pingouin):
    def __init__(self,x=0,y=0):
        #Le numéroPingouin de l'empereur est toujours 0 car il n'y a qu'un empereur
        Pingouin.__init__(x,y,0)
        self.setImage("RoiDeLaGlisse/empereur.jpg")
        

class RoiDeLaGlisse(Scene):
    def __init__(self,ecran):
        Scene.__init__(self,ecran,nom="RoiDeLaGlisse")
        self.setBackground("RoiDeLaGlisse.jpg")
        self.ajouterDialogue("description")
        """self.listePingouin = [Pingouin(335,70,0),Pingouin(575,70,1)]
        self.ajouterObjet(BoutonDescription())
        self.ajouterObjet(self.listePingouin[0])
        self.ajouterObjet(self.listePingouin[1])"""
        #self.ajouterObjet(self.listePingouin[2])
        #self.ajouterObjet(self.listePingouin[3])
        #self.ajouterObjet(self.listePingouin[4])
        #self.ajouterObjet(Empereur(coordonnees))
        self.ajouterObjet(FlecheHaut())
        self.pingouinActif = 0
        #self.directionPingouinActif = "R"
        self.position = [[1,0,1,0,0],[2,0,0,0,0],[0,0,0,0,1],[0,1,0,0,0],[0,0,0,1,0]]
        self.listePingouin=[]
        k=1
        self.positionPingouinActif=[0,0]
        for i in range(0,len(self.position)):
            for j in range(0,len(self.position[0])):
                if self.position[i][j]==1:
                    ping=Pingouin(335+119*j,70+117*i,k)
                    k+=1
                    self.ajouterObjet(ping)
                    self.listePingouin.append(ping)
                elif self.position[i][j]==2:
                    emp=Empereur(335+119*j,70+117*i)
                    self.ajouterObjet(emp)
                    self.listePingouin.append(emp)
                                   
        

    def actionsEvent(self,dictionnaire):
        x=0
        y=0
        if "ouvrirDescription" in dictionnaire:
            self.ouvrirDialogue("description")
        if "ActualiserPingouinActif" in dictionnaire:
            print (dictionnaire)
            #print(self.listePingouin[dictionnaire["ActualiserPingouinActif"]])
            self.pingouinActif = self.listePingouin[dictionnaire["ActualiserPingouinActif"][2]]#Comment faire pour qu'il trouve le chiffre à coté de "ActualiserPingouinActif" dans dictionnaire ?
            #si numéroPingouin=0 alors c'est l'empereur
            x=dictionnaire["ActualiserPingouinActif"][0]
            y=dictionnaire["ActualiserPingouinActif"][1]
            print(self.pingouinActif)
            self.positionPingouinActif=[x,y]
        if "Monter" in dictionnaire:
            fini=False
            y=self.positionPingouinActif[1]
            x=self.positionPingouinActif[0]
            i=(y-70)//117
            j=(x-70)//119
            i=idep
            j=jdep
            while fini==False:
                i=i-1
                if i<0:
                    self.position[idep][jdep]=0
                    fini=True
                """elif:
                    if i =! 1 :
                        monte()
                    else:
                        fini=True"""
            
                    
                    
    #def monte():
        

            

    """def updateFrame(self):
        if self.directionPingouinActif == "R":
            return
        elif self.directionPingouinActif == "N"
            coord = self.pingouinActif.getPosition()
            if coord > 5:
                self.pingouinActif.setPosition(coord[0],coord[1]-5)
            else:
                self.directionPingouinActif = "R" """

