from tkinter import *

fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("Gestion des campagnes JDR")

label = Label(fenetre, text="Hello World !")
label.pack()

bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()

