
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:27:41 2018

@author: assef, esra, thiz """

#Interface graphique

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from  tkinter.filedialog import *

from time import sleep



nbtrace=-1
bit=-1
lk_hypmax1=[]
class cryptoApp():
    def __init__(self,window):
        mainframe=ttk.LabelFrame(window,text="DATA",width=150,height=75)
        self.compteurerreurmotdepasse = 5
        self.entrynombredetrace=ttk.Entry(mainframe)
        self.entrybitchoisie=ttk.Entry(mainframe)
        self.label=ttk.Label(mainframe,text=" Bit choisi ",font=('Calibri',12,'bold'))
        self.label1=ttk.Label(mainframe,text=" Nombre de traces ",font=('Calibri',12,'bold'))
        self.buttonerror=ttk.Button(mainframe,text="OK",command=self.getinformation)
        self.checki=ttk.Checkbutton(mainframe,text="J'atteste avoir pris en considération la charte d'utilisation de ce si beau programme")
                
                #self.label=ttk.Label(window,text=" nombre d'essai :" + str(self.compteurerreurmotdepasse),font=('Calibri',14,'bold'))
                #self.buttonerror=ttk.Button(window,text="declancher",command=self.probleme)
                #self.nombredetracevoulu=ttk.Scale(window,from_=0, to=10000)
        mainframe.pack()
        self.label1.pack()
        self.entrynombredetrace.pack()
        self.label.pack()
        self.entrybitchoisie.pack()
        self.checki.pack()
        self.buttonerror.pack()


    def verificationsaisi(self):
        Listebit=[0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8]
        if int(self.entrybitchoisie.get()) not in Listebit:
            messagebox.showinfo("Erreur","Erreur survenue lors de la saisie du bit")
            return -1

        if not (int(self.entrynombredetrace.get()) > 0 and int(self.entrynombredetrace.get()) <= 10000):
            messagebox.showinfo("Erreur","Erreur survenue lors de la saisie du nombre de traces")
            return -1
        return 0



    def remove(self):
        if self.compteurerreurmotdepasse > 0:
            self.compteurerreurmotdepasse-= 1
            self.label.config(text="Il vous reste  :" + str(self.compteurerreurmotdepasse) + "tentatives")

    def probleme(self):
        messagebox.showinfo("ERREUR","Un problème est survenu lors de l'éxecution")

    def getinformation(self):
        global nbtrace
        global bit
        if self.verificationsaisi() == 0:
            nbtrace= int (self.entrynombredetrace.get())
            bit = self.entrybitchoisie.get()
        window.destroy()
        print (nbtrace)
        print (bit)



window=Tk()
window.minsize(250,125)
#filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
#window.resizable(width=False,height=False)
window.positionfrom("user")
app=cryptoApp(window)
window.mainloop()
print (nbtrace)
print (bit)

Listebit=[0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8]
bit=Listebit[int(bit)-1]        
from progr_int import progr_int
lk_hypmax=progr_int(nbtrace,bit)

cleorigine=[43, 126, 21, 22, 40, 174, 210, 166, 171, 247, 21, 136, 9, 207, 79, 60]

class cryptoEND():
    def __init__(self,window2):
        mainframe1=ttk.LabelFrame(window2,text=" C'est l'heure de vérité ",width=500,height=300)
        #self.entrylkypmax=ttk.Entry(mainframe1)
        self.makypmax=ttk.Label(mainframe1,text= "Notre clé obtenu est " + str(lk_hypmax),font=('Calibri',12,'bold'))
        #self.label2=ttk.Label(mainframe1,text=" saisissez votre clé",font=('Calibri',12,'bold'))
        self.buttonerror=ttk.Button(mainframe1,text="Valider",command=self.verificationcle)
        self.checki2=ttk.Checkbutton(mainframe1,text="J'assure qu'en cas d'erreur je ne dégraderai pas le matériel ! ")
                
                #self.label=ttk.Label(window,text=" nombre d'essai :" + str(self.compteurerreurmotdepasse),font=('Calibri',14,'bold'))
                #self.buttonerror=ttk.Button(window,text="declancher",command=self.probleme)
                #self.nombredetracevoulu=ttk.Scale(window,from_=0, to=10000)
        mainframe1.pack()
        self.makypmax.pack()
        #self.label2.pack()
        #self.entrylkypmax.pack()
        self.checki2.pack()
        self.buttonerror.pack()

    def getinformation1(self):
        global lk_hypmax1
        if len(list(self.entrylkypmax.get())) == len(lk_hypmax):
            lk_hypmax1= list(self.entrylkypmax.get())
    
        return 1

    def verificationcle(self):
        y=0
        nberreur=0
        global lk_hypmax

        #self.getinformation1()
        print(lk_hypmax1)
        #while(y <=(len(lk_hypmax) -1)):
        if lk_hypmax != cleorigine:
            messagebox.showinfo("ATTENTION ERREUR","La clé obtenue ne correspond pas !\n La clé mystère était " + str(cleorigine))
            return 1
        else:
            messagebox.showinfo("BIIIIINNNNGOOOOOOOO!","Tu es plutôt intelligent :)")
            return -1
                #nberreur+=1
                #y=y + 1

        """if nberreur != 0:
            messagebox.showinfo("ATTENTION ERREUR","la clé obtenu ne correspond pas ! tu as" + str(nberreur) + "erreurs")
            return -1
        else:
            messagebox.showinfo("BIIIIINNNNGOOOOOOOO!","T'es plutot intélligent :)")
            return 1"""
        window2.destroy()






window2=Tk()
window2.maxsize(500,300)
#filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
#window.resizable(width=False,height=False)
window2.positionfrom("user")
app=cryptoEND(window2)
window2.mainloop()
print(lk_hypmax1)



