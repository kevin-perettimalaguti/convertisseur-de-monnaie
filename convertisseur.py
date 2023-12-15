from forex_python.converter import CurrencyRates
import json
import os
from tkinter import *
from tkinter import ttk

# Couleur que je vais utiliser
orange = (253, 103, 24)
white = "#ffffff"
dark_grey = "#21212b"


# Fenêtre principale du convertisseur
fenetre = Tk()
fenetre.geometry("450x350")
fenetre.title("Convertisseur de monnaie")
fenetre.config(bg = "#f3810e")

# # Créer une instance de CurrencyRates
c = CurrencyRates()

# Liste des devise dont la fonction disposes
devises_supportees = list(c.get_rates('USD').keys())

# Header
top = Frame(fenetre, width=450, height=80, bg=dark_grey)
top.place(x=0,y=0)

label_title = Label(top, text="Converstisseur de Monnaie", font=("Ivy 20"), width = 35, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, bg=dark_grey, fg=white, justify=CENTER)
label_title.place(relx=0.1, rely=0.2)

# Montant
label_a = Label(fenetre, text="Le Montant", font=("Ivy 15"), width = 10, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, bg="#f3810e")
label_a.place(relx=0.5, rely=0.35, anchor=CENTER)  # Place au centre

montant_visuel = Entry(fenetre, justify=CENTER, width=30)
montant_visuel.place(relx=0.5, rely=0.45, anchor=CENTER)  # Place au centre

# Label "From"
label_de = Label(fenetre, text="From", font=("Ivy 15"), width = 10, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, bg="#f3810e")
label_de.place(relx=0.3, rely=0.55, anchor=CENTER)  # Place au centre

# Label "To"
label_a = Label(fenetre, text="To", font=("Ivy 15"), width = 10, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, bg="#f3810e")
label_a.place(relx=0.7, rely=0.55, anchor=CENTER)  # Place au centre

# Combobox "From"
devise_depart = ttk.Combobox(fenetre, width=8, justify=CENTER, font=("Ivy 15"))
devise_depart.place(relx=0.3, rely=0.65, anchor=CENTER)  # Place au centre
devise_depart["values"] = devises_supportees  # Vous devez définir les valeurs pour la liste des devises

# Combobox "To"
devise_arrive = ttk.Combobox(fenetre, width=8, justify=CENTER, font=("Ivy 15"))
devise_arrive.place(relx=0.7, rely=0.65, anchor=CENTER)  # Place au centre
devise_arrive["values"] = devises_supportees  # Vous devez définir les valeurs pour la liste des devises

label_resultat = Label(fenetre, text="", font=("Ivy 15"), width = 35, height=1, padx = 5, pady = 1,  relief = "flat", anchor = NW, bg="#ffffff")
label_resultat.place(relx=0.5, rely=0.78, anchor=CENTER)  # Place au centre

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

        
# Bouton de conversion
bouton_convertir = Button(fenetre, text="Convertir", font=("Ivy 15"), width=8, height=1, command=calcule_conversion)
bouton_convertir.place(relx=0.5, rely=0.92, anchor=CENTER)  # Place au centre

# Sauvegarder l'historique des conversions
def save_historique():
    with open(fichier_historique, 'w') as file:
        json.dump(historique_conversions, file)
        
        
fenetre.mainloop()  
