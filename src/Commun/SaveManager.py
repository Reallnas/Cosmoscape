class SaveManager:
    #se renseigner sur pickle
    
    ligneScenePartieActuelle = 0
    ligneEnigmesPartieActuelle = 1
    ligneEnigmesPartiesTotales = 2
    ligneDialoguesSpeciaux = 3
    
    def __init__(self):
        #cherche si un fichier de sauvegarde existe deja
        #sinon, en cree un nouveau
        try:
            file = open("save.txt", "r")
        except:
            print("Nouveau fichier de sauvegarde créé")
            self.hardReset()
        else:
            file.close()

    def getLine(self,numeroLigne=0):
        #permet d'obtenir la valeur d'une certaine ligne dans le fichier de sauvegarde
        with open("save.txt", "r",encoding="utf8") as file:
            for i in range (0,numeroLigne):
                file.readline()
            saveStr = file.readline()
            saveStr = saveStr.rstrip('\n')
            return saveStr

    def setLine(self,numeroLigne=0,text=""):
        #permet de remplacer une chaine de caractere par une nouvelle a la ligne specifiee dans le fichier de sauvegarde
        with open("save.txt", "r+",encoding="utf8") as file:
            text+='\n'
            #on a stocke toutes les lignes du fichier et on remet le curseur de lecture au debut
            data = file.readlines()
            file.seek(0)
            #on reecrit toutes les lignes precedentes a la ligne a change a l'identique,
            #si toutes les lignes on ete reecrites, on passe a la ligne suivante
            for i in range (0,numeroLigne):
                if(i < len(data)):
                    file.write(data[i])
                else:
                    file.write('\n')
            #on ecrit la ligne que l'on voulait changer
            file.write(text)
            file.truncate()
            #si il reste des lignes a ecrire, on les reecrit
            if(numeroLigne < len(data)):
                file.writelines(data[numeroLigne+1:])

    def obtenirSceneActuelle(self):
        saveStr = self.getLine(self.ligneScenePartieActuelle)
        print("Scene Actuelle en sauvegarde:",saveStr)
        return saveStr

    def sauvegarderSceneActuelle(self,nomScene):
        self.setLine(self.ligneScenePartieActuelle,nomScene)
        print("Scene Actuelle sauvegardée:",nomScene)

    def obtenirEtatEnigmePartieActuelle(self,numeroEnigme):
        sauvegardeEnigme = self.getLine(self.ligneEnigmesPartieActuelle)
        if(numeroEnigme<0 or numeroEnigme >= len(sauvegardeEnigme)):
            print("Numero d'énigme à vérifier invalide (Partie actuelle):",numeroEnigme)
        else:
            enigmeReussie = (sauvegardeEnigme[numeroEnigme] == '1')
            print("Enigme numero",numeroEnigme,"reussie:",enigmeReussie,"(Partie actuelle)")
            return enigmeReussie

    def obtenirEtatEnigmeTotal(self,numeroEnigme):
        sauvegardeEnigme = self.getLine(self.ligneEnigmesPartiesTotales)
        if(numeroEnigme<0 or numeroEnigme >= len(sauvegardeEnigme)):
            print("Numero d'énigme à vérifier invalide (total):",numeroEnigme)
        else:
            enigmeReussie = (sauvegardeEnigme[numeroEnigme] == '1')
            print("Enigme numero",numeroEnigme,"reussie:",enigmeReussie,"(Total)")
            return enigmeReussie

    def sauvegarderEnigmeReussie(self,numeroEnigme):
        sauvegardeEnigme = self.getLine(self.ligneEnigmesPartieActuelle)
        if(numeroEnigme<0):
            print("Numero d'énigme à sauvegarder invalide :",numeroEnigme)
            return
        elif(numeroEnigme >= len(sauvegardeEnigme)):
            sauvegardeEnigme = sauvegardeEnigme.ljust(numeroEnigme,'0') + '1'
        else:
            sauvegardeEnigme = sauvegardeEnigme[:numeroEnigme] + '1' + sauvegardeEnigme[numeroEnigme+1:]
        self.setLine(self.ligneEnigmesPartieActuelle,sauvegardeEnigme)
        print("Enigme numero",numeroEnigme,"sauvegardée")
        
        sauvegardeEnigmeTotale = self.getLine(self.ligneEnigmesPartiesTotales)
        if(numeroEnigme >= len(sauvegardeEnigmeTotale)):
            sauvegardeEnigmeTotale = sauvegardeEnigmeTotale.ljust(numeroEnigme,'0') + '1'
        else:
            sauvegardeEnigmeTotale = sauvegardeEnigmeTotale[:numeroEnigme] + '1' + sauvegardeEnigmeTotale[numeroEnigme+1:]
        self.setLine(self.ligneEnigmesPartiesTotales,sauvegardeEnigmeTotale)
        
    def sauvegarderDialogueSpecial(self,numeroDialogue):
        sauvegardeDialogues = self.getLine(self.ligneDialoguesSpeciaux)
        if(numeroDialogue<0):
            print("Numero de dialogue spécial à sauvegarder invalide :",numeroDialogue)
            return
        elif(numeroDialogue >= len(sauvegardeDialogues)):
            sauvegardeDialogues = sauvegardeDialogues.ljust(numeroDialogue,'0') + '1'
        else:
            sauvegardeDialogues = sauvegardeDialogues[:numeroDialogue] + '1' + sauvegardeDialogues[numeroDialogue+1:]
        self.setLine(self.ligneDialoguesSpeciaux,sauvegardeDialogues)
        print("Dialogue spécial numéro",numeroDialogue,"sauvegardé")

    def obtenirEtatDialogueSpecial(self,numeroDialogue):
        sauvegardeDialogues = self.getLine(self.ligneDialoguesSpeciaux)
        if(numeroDialogue<0 or numeroDialogue >= len(sauvegardeDialogues)):
            print("Numero de dialogue spécial à vérifier invalide:"
                  ,numeroDialogue)
        else:
            dialogueDejaFait = (sauvegardeDialogues[numeroDialogue] == '1')
            print("Dialogue spécial numero",numeroDialogue,"déjà eu:"
                  ,dialogueDejaFait)
            return dialogueDejaFait
        
    def resetPartieActuelle(self):
        print("Parie actuelle remise à zéro !")
        self.setLine(self.ligneScenePartieActuelle,"Pilote")
        self.setLine(self.ligneEnigmesPartieActuelle,"0"*20)
        self.setLine(self.ligneDialoguesSpeciaux,"0"*20)

    def hardReset(self):
        with open("save.txt", "w",encoding="utf8") as file:
            print("Sauvegarde remise à zéro !")
            file.truncate()
            file.write("Pilote\n")
            file.write('0'*20+'\n')
            file.write('0'*20+'\n')
            file.write('0'*20+'\n')

if __name__ == '__main__':
    sm = SaveManager()
    #sa = sm.obtenirSceneActuelle()
    #sm.resetPartieActuelle()
    #sm.sauvegarderSceneActuelle(sa)
    sm.sauvegarderEnigmeReussie(3)
    #sm.resetPartieActuelle()
    #sm.hardReset()
    sm.resetPartieActuelle()
    sm.obtenirEtatEnigmeTotal(3)
