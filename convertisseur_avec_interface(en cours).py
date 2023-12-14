from forex_python.converter import CurrencyRates
import json
import os
from tkinter import *
from PIL import Image, ImageTk
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
# devise_depart["values"] = liste_devise  # Vous devez définir les valeurs pour la liste des devises

# Combobox "To"
devise_arrive = ttk.Combobox(fenetre, width=8, justify=CENTER, font=("Ivy 15"))
devise_arrive.place(relx=0.7, rely=0.65, anchor=CENTER)  # Place au centre
# devise_arrive["values"] = liste_devise  # Vous devez définir les valeurs pour la liste des devises

fenetre.mainloop()


# # Créer une instance de CurrencyRates
# c = CurrencyRates()

# # Vérifier si le fichier d'historique existe
# fichier_historique = 'save_des_conversion.json'
# if os.path.exists(fichier_historique):
#     # Charger l'historique existant depuis le fichier
#     with open(fichier_historique, 'r') as file:
#         historique_conversions = json.load(file)
# else:
#     # Créer une liste vide si le fichier n'existe pas encore
#     historique_conversions = []

# # Afficher la liste des devises supportées
# try:
#     devises_supportees = list(c.get_rates('USD').keys())
#     print("Devises supportées :", devises_supportees)
# except Exception as e:
#     print(f"Erreur lors de la récupération des devises supportées : {e}")

# # Demander à l'utilisateur de saisir le montant
# while True:
#     try:
#         montant = int(input("Entrez le montant à convertir : "))
#         break       
#     except ValueError:
#         print("Le montant n'est pas lisable")       

# # Demander à l'utilisateur de saisir la devise source
# devise_source = input("Entrez la devise source comme indiqué précédement en capital : ")

# # Demander à l'utilisateur de saisir la devise cible
# devise_cible = input("Entrez la devise cible comme indiqué précédement en capital : ")

# # Obtenir le taux de change entre les devises choisies
# try:
#     taux = c.get_rate(devise_source, devise_cible)
# except Exception as e:
#     print(f"Erreur lors de la récupération du taux de change : {e}")
#     taux = None

# # Vérifier si la conversion est possible
# if taux is not None:
#     montant_converti = montant * taux
#     print(f"{montant} {devise_source} équivaut à {montant_converti} {devise_cible}")

#     # Ajouter la conversion à l'historique
#     historique_conversions.append({
#         "montant": montant,
#         "devise_source": devise_source,
#         "devise_cible": devise_cible,
#         "montant_converti": montant_converti
#     })
# else:
#     print("Cette conversion est impossible.")

# # Sauvegarder l'historique des conversions
# def save_historique():
#     with open(fichier_historique, 'w') as file:
#         json.dump(historique_conversions, file)

# # Appeler la fonction pour sauvegarder l'historique
# save_historique()

# print("Programme Terminé")
