from tkinter import *
#reglages graphisme fenêtre
color = "#F5BEB4"
color_texte = "#485B42"
color_texte_input = "#485B42"
color_texte_button = "#485B42"
typo = "helvetica"
typo2 = "arial"
bg_input = "white"
bg_bouton = "#E9816D"
bg_bouton2 = "#9BC472"
taille_typo = 25
taille_typo_input  = 15
taille_typo_bouton = 20


#fonction pour le stop-loss de  vente
def action():
    a = float(prix.get())
    b = a * (0.02/int(levier.get()))
    c = a + b
    vente.delete(0,END)
    vente.insert(0,c)

#fonction pour le stop-loss d'achat
def action2():
    a = float(prix.get())
    b = a * (0.02/int(levier.get()))
    c = a - b
    achat.delete(0,END)
    achat.insert(0,c)

# fenetre tkinter
fenetre= Tk()
fenetre.title("cryptanalyse")
fenetre.minsize(360, 360)
fenetre.config(background=color)
boite = Frame(bg=color)

#input pour le levier
label_levier = Label(boite, text=" levier ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_levier.grid(row=0, column=2, columnspan=3)
levier = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=3, exportselection=0)
levier.grid(row=1, column=2, columnspan=3)

#input pour le prix de l'action
label_prix = Label(boite, text="prix de l'action ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_prix.grid(row=3, column=2, columnspan=3)
prix = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
prix.grid(row=4, column=2, columnspan=3)

#input pour stop loss de vente
label_vente = Label(boite, text="stop-loss de vente ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_vente.grid(row=5, column=2, columnspan=3)
vente = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
vente.grid(row=6, column=2, columnspan=3)

#input pour stop loss d'achat
label_vente = Label(boite, text="stop-loss d'achat ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_vente.grid(row=7, column=2, columnspan=3)
achat = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
achat.grid(row=8, column=2, columnspan=3)

#tricherie pour espace
label_espace = Label(boite, text="   ", font=(typo, 25), bg=color, fg=color_texte)
label_espace.grid(row=9, column=2, columnspan=3)

#bouton pour action
B_vente = Button(boite, text="Vente", font=(typo, taille_typo_bouton), bg=bg_bouton,fg=color_texte_button,padx=20, command= action)
B_vente.grid(row=10, column=1, columnspan=3, sticky="W")
B_achat = Button(boite, text="Achat", font=(typo, taille_typo_bouton), bg=bg_bouton2,fg=color_texte_button,padx=20, command= action2)
B_achat.grid(row=10, column=3, columnspan=3, sticky="E")



boite.pack(expand=YES)
fenetre.mainloop()


