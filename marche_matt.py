from tkinter import *

def anim():
    global x, frame, Fichier_perso
    x = x + 40
    if x > 1000 : x = -500
    frame = frame + 1
    if frame == 9 : frame = 1
    Fichier_perso = PhotoImage(file="matt"+str(frame)+".gif")
    Fond.itemconfig(Matt, image = Fichier_perso)
    Fond.coords(Matt,x,0)
    fenetre.after(100,anim)

fenetre=Tk()
fenetre.title("Le marcheur")

Fond=Canvas(fenetre,width=1000,height=300,bg="white")
Fond.grid()

Fichier_perso = PhotoImage(file="matt1.gif")
Matt = Fond.create_image(-250,0,image=Fichier_perso,anchor='nw')

x, frame = -250, 1
anim()

fenetre.mainloop()






