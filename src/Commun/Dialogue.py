import pygame

from src.Commun.LoadingManager import *

class Dialogue:

    marge = 10
    nbTotalLigne = 3
    
    def __init__(self,fichier,balise,nomPolice="Helvetica"):
        if not pygame.font.get_init():
            print("Bibliotheque 'pygame.font' non trouvée")
            raise SystemError
        self.imageBoite = loadImage("Images/Objets/boite_dialogues.jpg")
        self.initCoordonnees()
        self.police = pygame.font.SysFont(nomPolice,30)
        self.nomFichier = fichier
        self.listeMots = []
        self.indexProchainMot = 0
        self.estTexteFini = False
        self.chargeTexte(balise)
        
    def initCoordonnees(self):
        self.rect = self.imageBoite.get_rect()
        x = (1280-self.rect.width)/2
        y = 720-self.rect.height
        self.rect.topleft = (x,y)
        
    def chercheBalise(self,balise):
        with open(self.nomFichier, "r",encoding="utf8") as file:
            data = file.readlines()
            ligneBalise = -1
            for counter,line in enumerate(data):
                if line.startswith('-'):
                    indexEgal = line.find('=')
                    text = line[1:indexEgal]
                    if text == balise:
                        ligneBalise = counter
                        print("Balise",balise,"trouvée à la ligne",ligneBalise,
                              "du fichier",self.nomFichier)
        if ligneBalise == -1:
            print("!Erreur! Balise",balise,"non trouvée dans le fichier",
                  self.nomFichier)
            print("""Cela vient probablement d'une faute de frappe dans le nom du
                  fichier ou de la balise""")
        return ligneBalise
        
    def chargeTexte(self,baliseTexte):
        ligneBalise = self.chercheBalise(baliseTexte)
        if ligneBalise < 0:
            return
        
        self.retourAuDebut()
        with open(self.nomFichier, "r",encoding="utf8") as file:
            #place le curseur a la ligne ou se trouve la balise
            for i in range(0,ligneBalise):
                file.readline()
            text = '\"'
            while text.find('\"') >=0:
                text=file.readline()
                posPremierGuillemet=text.find('\"')+1
                posDeuxiemeGuillemet=text.rfind('\"')
                ligne = text[posPremierGuillemet:posDeuxiemeGuillemet]

                if ligne != "":
                    self.listeMots.extend(ligne.split())
                    print("Ligne ajoutée:",ligne)

    def avancerMot(self):
        self.indexProchainMot += 1
        self.estTexteFini = self.indexProchainMot >= len(self.listeMots)
        if self.estTexteFini:
            print("Texte Fini")
        
    def remplirLigne(self,numeroLigne):
        ligne = ""
        estLigneFinie = False
        while not estLigneFinie and not self.estTexteFini:
            mot = self.listeMots[self.indexProchainMot]
            #le mot "!$!" force le programme a arreter de remplir
            #les lignes actuelles
            if mot == "!$!":
                estLigneFinie = True
                #si on est sur la derniere ligne, avancer d'un mot
                #pour ne pas tomber dans une boucle infinie
                if numeroLigne == self.nbTotalLigne-1:
                    self.avancerMot()
            #le mot "!n!" force le programme a arreter de remplir
            #la ligne actuelle
            elif mot == "!n!":
                #avancer d'un mot pour ne pas
                #tomber dans une boucle infinie
                estLigneFinie = True
                self.avancerMot()
            else:
                texte = ligne+mot+' '
                #on verifie que la ligne ne depasse
                #pas une certaine largeur
                if self.police.size(texte)[0]-self.marge*2 < self.rect.width:
                    ligne = texte
                    self.avancerMot()
                else:
                    estLigneFinie = True
        return ligne
    
    def avancerTexte(self):
        self.imageFinale = self.imageBoite.copy()
        for i in range(0,self.nbTotalLigne):
            ligne = self.remplirLigne(i)
            print("Ligne",i,":",ligne)
            #on rend le texte visible une fois que l'on a rempli les lignes
            rendu = self.police.render(ligne,False,(0,0,0))
            yLigne = self.calculYLigne(i,self.police.get_linesize())
            xLigne = self.calculXLigne(self.police.size(ligne)[0])
            self.imageFinale.blit(rendu,(self.marge+10,yLigne))
        return self.estTexteFini

    def calculYLigne(self,numeroLigne,taillePolice):
        diffTotale = self.rect.height - taillePolice*self.nbTotalLigne-2*self.marge
        interligne = diffTotale/(self.nbTotalLigne+1)
        return self.marge+self.police.get_linesize()*numeroLigne+interligne*(numeroLigne+1)

    def calculXLigne(self,largeurLigne):
        return(self.rect.width-largeurLigne)/2
    
    def draw(self,surface):
        surface.blit(self.imageFinale,self.rect)

    def retourAuDebut(self):
        self.indexProchainMot = 0
        self.estTexteFini = False
        
