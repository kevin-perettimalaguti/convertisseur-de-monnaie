# Importation des modules 
from forex_python.converter import CurrencyRates
import json
import os
from tkinter import *
from tkinter import ttk

# Couleurs que je vais utiliser
orange = "#f3810e"
white = "#ffffff"
dark_grey = "#21212b"

# Fenêtre principale du convertisseur
fenetre = Tk()
fenetre.geometry("450x430")
fenetre.title("Convertisseur de monnaie")
fenetre.config(bg=orange)

# Créer une instance de CurrencyRates
c = CurrencyRates()

# Liste des devises disponibles dans la fonction
devises_supportees = list(c.get_rates('USD').keys())

# Header
top = Frame(fenetre, width=450, height=80, bg=dark_grey)
top.place(x=0, y=0)

label_title = Label(top, text="Convertisseur de Monnaie", font=("Ivy 20"), width=35, height=1, padx=5, pady=1,
                    relief="flat", anchor=NW, bg=dark_grey, fg=white, justify=CENTER)
label_title.place(relx=0.1, rely=0.2)

# Montant
label_a = Label(fenetre, text="Le Montant", font=("Ivy 15"), width=10, height=1, padx=5, pady=1, relief="flat",
                anchor=NW, bg="#f3810e")
label_a.place(relx=0.5, rely=0.30, anchor=CENTER) 
 
montant_visuel = Entry(fenetre, justify=CENTER, width=30)
montant_visuel.place(relx=0.5, rely=0.37, anchor=CENTER)  

# Label "From"
label_de = Label(fenetre, text="From", font=("Ivy 15"), width=10, height=1, padx=5, pady=1, relief="flat",
                 anchor=NW, bg="#f3810e")
label_de.place(relx=0.3, rely=0.47, anchor=CENTER)  

# Combobox "From"
devise_depart = ttk.Combobox(fenetre, width=8, justify=CENTER, font=("Ivy 15"))
devise_depart.place(relx=0.3, rely=0.55, anchor=CENTER)  
devise_depart["values"] = devises_supportees 

# Label "To"
label_a = Label(fenetre, text="To", font=("Ivy 15"), width=10, height=1, padx=5, pady=1, relief="flat",
                anchor=NW, bg="#f3810e")
label_a.place(relx=0.7, rely=0.47, anchor=CENTER) 

# Combobox "To"
devise_arrive = ttk.Combobox(fenetre, width=8, justify=CENTER, font=("Ivy 15"))
devise_arrive.place(relx=0.7, rely=0.55, anchor=CENTER)  
devise_arrive["values"] = devises_supportees 

label_resultat = Label(fenetre, text="", font=("Ivy 15"), width=35, height=1, padx=5, pady=1, relief="flat",
                      anchor=NW, bg="#ffffff")
label_resultat.place(relx=0.5, rely=0.69, anchor=CENTER)  

# Vérifier si le fichier d'historique existe
fichier_historique = 'save_des_conversion.json'
if os.path.exists(fichier_historique):
    # Charger l'historique existant depuis le fichier
    with open(fichier_historique, 'r') as file:
        historique_conversions = json.load(file)
else:
    # Créer une liste vide si le fichier n'existe pas encore
    historique_conversions = []


def calcule_conversion():
    # Obtenir le taux de change entre les devises choisies
    taux = c.get_rate(devise_depart.get(), devise_arrive.get())

    # Vérifier si la conversion est possible
    try:
        montant_entree = float(montant_visuel.get())
        montant_converti = montant_entree * taux

        # Ajouter la conversion à l'historique
        historique_conversions.append({
            "montant": montant_entree,
            "devise_source": devise_depart.get(),
            "devise_cible": devise_arrive.get(),
            "montant_converti": montant_converti
        })
        label_resultat.config(text=f"{montant_entree} {devise_depart.get()} = {montant_converti} {devise_arrive.get()}")
    except ValueError:
        label_resultat.config(text="Erreur, veuillez entrer un montant valide.")

    # Sauvegarde de l'historique des conversions
    save_historique()

    if taux is None:
        label_resultat.config(text="Erreur, je ne comprends pas ta conversion")
        
# Fonction pour effacer l'historique
def clear_historique():
    # Effacer l'historique dans le code principal et mettre à jour l'affichage dans la fenêtre d'historique
    global historique_conversions
    historique_conversions = []
    afficher_historique()

# Afficher l'historique dans la fenêtre avec une barre de défilement
def afficher_historique():
    page_historique = Tk()
    page_historique.title("Historique")
    page_historique.geometry("320x460")
    page_historique.config(bg=dark_grey)    

    # Créer un widget Listbox avec la barre de défilement
    listbox_histo = Listbox(page_historique, width=40, height=20, font=("Ivy 10"), bg=dark_grey, fg=white, justify=CENTER)

    # Ajouter les éléments de l'historique à la Listbox
    for conversion in historique_conversions:
        montant_str = f"{conversion['montant']} {conversion['devise_source']} => " \
                      f"{conversion['montant_converti']} {conversion['devise_cible']}"
        listbox_histo.insert(END, montant_str)    

    listbox_histo.pack(pady=20)
    
    # Bouton pour fermer la fenêtre
    bouton_fermer = Button(page_historique, text="Fermer", font=("Ivy 12"), width=10, height=1,
                       command=page_historique.destroy, bg=orange, fg=dark_grey, relief="flat")
    bouton_fermer.pack(pady=5)  # Ajout d'un espace en bas

    # Bouton pour effacer l'historique
    bouton_clear_histo = Button(page_historique, text="Clear Historique", font=("Ivy 12"), width=15, height=1,
                            command=clear_historique, bg=orange, fg=dark_grey, relief="flat")
    bouton_clear_histo.pack(pady=5)  # Ajout d'un espace en bas
    

# Bouton de conversion
bouton_convertir = Button(fenetre, text="Convertir", font=("Ivy 15"), width=8, height=1, command=calcule_conversion,
                          bg=dark_grey, fg=white, relief="flat")
bouton_convertir.place(relx=0.5, rely=0.81, anchor=CENTER)  # Place au centre

# Bouton pour afficher mon historique
label_histo = Button(fenetre, text="Historique des conversions", font=("Ivy 15"), width=30, height=1,
                     command=afficher_historique, bg=dark_grey, fg=white, relief="flat")
label_histo.place(relx=0.5, rely=0.93, anchor=CENTER)

# Sauvegarder l'historique des conversions
def save_historique():
    with open(fichier_historique, 'w') as file:
        json.dump(historique_conversions, file)

fenetre.mainloop()
