from tkinter import*
from random import*
from time import *

class Pingouin:
    def __init__(self,canvas,x,y,numero,empereur):
        self.x=x
        self.y=y
        self.numero=numero
        self.empereur=empereur
        if self.empereur:
            self.color="red"
        else:
            self.color="orange"
        self.canvas=canvas
        self.placer()
        self.dep=0
        self.nbdep=0
        self.mort=False

    def setMort(self):
        self.mort=True

    def getMort(self):
        return self.mort

    def setNbDep(self,n):
        self.dep=0
        self.nbdep=n

    def getNum(self):
        return self.numero

    def getCoordonnées(self):
        return self.x,self.y

    def getPosition(self):
        return ((self.y-50)//100,(self.x-50)//100)

    def placer(self):
        self.obj=self.canvas.create_oval(self.x-30,self.y-30,self.x+30,self.y+30,fill=self.color,tag=str(num))

    def deplacer(self,direction):
        if direction=="N":
            self.y-=10
        elif direction=="S":
            self.y+=10
        elif direction=="O":
            self.x-=10
        else:
            self.x+=10
        if self.nbdep!=0:
            self.canvas.coords(self.obj,self.x-30,self.y-30,self.x+30,self.y+30)
            self.dep+=1
        if self.dep<self.nbdep*10:
            self.canvas.after(200,lambda x=direction:self.deplacer(x))
        else:
            if self.numero==0:
                if self.mort:
                    print("Vous avez perdu")
                elif self.getPosition()[0]==2 and self.getPosition()[1]==2:
                    print("Vous avez gagné")

    def __eq__(self,other):
        if self.num==other.getNum():
            return True
        else:
            return False

def isPingouin(listePingouins,i,j):
        present=False
        for k in range(len(listePingouins)):
            if listePingouins[k].getPosition()[0]==i and listePingouins[k].getPosition()[1]==j and not listePingouins[k].getMort():
                present=True
        return present
    
def detection(evt):
    global pa
    obj=can.gettags(CURRENT)
    if len(obj)!=0:
        pa=int(obj[0])
        print(pa)

def fleche(evt):
    global tab_obj,pa
    pos=tab_obj[pa].getPosition()
    i=pos[0]
    j=pos[1]
    #print(str(evt.keysym))
    if str(evt.keysym)=="Up":
        deplacement=0
        while i>=0 and not isPingouin(tab_obj,i-1,j):
            deplacement+=1
            i=i-1
            #print("i=",i)
            #print("pingouin :",isPingouin(tab_obj,i-1,j))
        if i<0:
            tab_obj[pa].setMort()
        tab_obj[pa].setNbDep(deplacement)
        tab_obj[pa].deplacer("N")
    if str(evt.keysym)=="Down":
        deplacement=0
        while i<=4 and not isPingouin(tab_obj,i+1,j):
            deplacement+=1
            i=i+1
            #print("i=",i)
            #print("pingouin :",isPingouin(tab_obj,i+1,j))
        if i>4:
            tab_obj[pa].setMort()
        tab_obj[pa].setNbDep(deplacement)
        tab_obj[pa].deplacer("S")
    if str(evt.keysym)=="Left":
        pos=tab_obj[pa].getPosition()
        deplacement=0
        while j>=0 and not isPingouin(tab_obj,i,j-1):
            deplacement+=1
            j=j-1
        if j<0:
            tab_obj[pa].setMort()
            #print("i=",i)
            #print("pingouin :",isPingouin(tab_obj,i+1,j))
        tab_obj[pa].setNbDep(deplacement)
        tab_obj[pa].deplacer("O")
    if str(evt.keysym)=="Right":
        deplacement=0
        while j<=4 and not isPingouin(tab_obj,i,j+1):
            deplacement+=1
            j=j+1
        if j>4:
            tab_obj[pa].setMort()
            #print("i=",i)
            #print("pingouin :",isPingouin(tab_obj,i+1,j))
        tab_obj[pa].setNbDep(deplacement)
        tab_obj[pa].deplacer("E")    

                
pa=0
k=0
  
fen=Tk()

can=Canvas(height=500,width=500)
for k in range(1,5):
    can.create_line(0,100*k,500,100*k)
    can.create_line(100*k,0,100*k,500)
    
can.pack()

tab_obj=[]
positions=[[3,0],[0,0],[1,2],[2,4],[3,4],[4,3]]
for num in range(len(positions)):
    i=positions[num][0]
    j=positions[num][1]
    if num==0:
        empereur=True
    else:
        empereur=False
    tab_obj.append(Pingouin(can,50+100*j,50+100*i,num,empereur))
    print("objet",tab_obj[num].getNum(),":",tab_obj[num].getPosition())
    print(i,j)

can.bind("<Button-1>",detection)
can.bind("<Key>",fleche)
can.focus_set()

"""for i in range(0,2):
    can.tag_bind(tab[i],"<Button-1>",detection)"""

fen.mainloop()