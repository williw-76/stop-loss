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


#fonction pour le stop-loss de vente
def action():
    a = float(prix.get())
    b = a * (0.02/int(levier.get()))
    c = a + b
    vente.delete(0,END)
    vente.insert(0,c)
    d = a * (0.11 / int(levier.get()))
    e = a - d
    take_vente.delete(0, END)
    take_vente.insert(0, e)

#fonction pour le stop-loss d'achat
def action2():
    a = float(prix.get())
    b = a * (0.02/int(levier.get()))
    c = a - b
    achat.delete(0,END)
    achat.insert(0,c)
    d = a*(0.11/int(levier.get()))
    e = a + d
    take_achat.delete(0, END)
    take_achat.insert(0, e)

# fenetre tkinter
fenetre= Tk()
fenetre.title("stop-loss/take-profits")
fenetre.minsize(360, 360)
fenetre.config(background=color)
boite = Frame(bg=color)

#tricherie pour espace
label_espace = Label(boite, text="   ", font=(typo, 5), bg=color, fg=color_texte)
label_espace.grid(row=0, column=0, columnspan=5)

#input pour le titre
label_ordre = Label(boite, text="ORDRE", font=(typo, taille_typo), bg=color, fg=color_texte)
label_ordre.grid(row=2, column=1, columnspan=1)

#input pour le levier
label_levier = Label(boite, text="levier", font=(typo, taille_typo), bg=color, fg=color_texte)
label_levier.grid(row=2, column=0, columnspan=1)
levier = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
levier.grid(row=3, column=0, columnspan=1)

#input pour le prix de l'action
label_prix = Label(boite, text="prix", font=(typo, taille_typo), bg=color, fg=color_texte)
label_prix.grid(row=2, column=2, columnspan=3)
prix = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
prix.grid(row=3, column=2, columnspan=3)

#tricherie pour espace
label_espace = Label(boite, text="   ", font=(typo, 20), bg=color, fg=color_texte)
label_espace.grid(row=4, column=0, columnspan=5)

#bouton pour action
B_vente = Button(boite, text="Vente", font=(typo, taille_typo_bouton), bg=bg_bouton,fg=color_texte_button,padx=50, command= action)
B_vente.grid(row=7, column=1, columnspan=1)

#input pour stop loss de vente
label_vente = Label(boite, text="stop-loss", font=(typo, taille_typo), bg=color, fg=color_texte)
label_vente.grid(row=6, column=0, columnspan=1)
vente = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
vente.grid(row=7, column=0, columnspan=1)

#input pour take-profit de vente
label_take_vente = Label(boite, text="take-profit ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_take_vente.grid(row=6, column=2, columnspan=3)
take_vente = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
take_vente.grid(row=7, column=2, columnspan=3)

#tricherie pour espace
label_espace = Label(boite, text="   ", font=(typo, 15), bg=color, fg=color_texte)
label_espace.grid(row=8, column=0, columnspan=5)

#bouton pour action
B_achat = Button(boite, text="Achat", font=(typo, taille_typo_bouton), bg=bg_bouton2,fg=color_texte_button,padx=50, command= action2)
B_achat.grid(row=11, column=1, columnspan=1)

#input pour stop loss d'achat
label_vente = Label(boite, text="stop-loss ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_vente.grid(row=10, column=0, columnspan=1)
achat = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
achat.grid(row=11, column=0, columnspan=1)

#input pour take-profit d'achat'
label_take_achat = Label(boite, text="take-profit ", font=(typo, taille_typo), bg=color, fg=color_texte)
label_take_achat.grid(row=10, column=2, columnspan=3)
take_achat = Entry(boite, font=(typo2, taille_typo_input), bg=bg_input, fg=color_texte_input, width=10, exportselection=0)
take_achat.grid(row=11, column=2, columnspan=3)

#tricherie pour espace
label_espace = Label(boite, text="   ", font=(typo, 15), bg=color, fg=color_texte)
label_espace.grid(row=12, column=0, columnspan=5)






boite.pack(expand=YES)
fenetre.mainloop()


