from forex_python.converter import CurrencyRates
import json
import os

# Créer une instance de CurrencyRates
c = CurrencyRates()

# Vérifier si le fichier d'historique existe
fichier_historique = 'save_des_conversion.json'
if os.path.exists(fichier_historique):
    # Charger l'historique existant depuis le fichier
    with open(fichier_historique, 'r') as file:
        historique_conversions = json.load(file)
else:
    # Créer une liste vide si le fichier n'existe pas encore
    historique_conversions = []

# Afficher la liste des devises supportées
try:
    devises_supportees = list(c.get_rates('USD').keys())
    print("Devises supportées :", devises_supportees)
except Exception as e:
    print(f"Erreur lors de la récupération des devises supportées : {e}")

# Demander à l'utilisateur de saisir le montant
while True:
    try:
        montant = int(input("Entrez le montant à convertir : "))
        break       
    except ValueError:
        print("Le montant n'est pas lisable")       

# Demander à l'utilisateur de saisir la devise source
devise_source = input("Entrez la devise source comme indiqué précédement en capital : ")

# Demander à l'utilisateur de saisir la devise cible
devise_cible = input("Entrez la devise cible comme indiqué précédement en capital : ")

# Obtenir le taux de change entre les devises choisies
try:
    taux = c.get_rate(devise_source, devise_cible)
except Exception as e:
    print(f"Erreur lors de la récupération du taux de change : {e}")
    taux = None

# Vérifier si la conversion est possible
if taux is not None:
    montant_converti = montant * taux
    print(f"{montant} {devise_source} équivaut à {montant_converti} {devise_cible}")

    # Ajouter la conversion à l'historique
    historique_conversions.append({
        "montant": montant,
        "devise_source": devise_source,
        "devise_cible": devise_cible,
        "montant_converti": montant_converti
    })
else:
    print("Cette conversion est impossible.")

# Sauvegarder l'historique des conversions
def save_historique():
    with open(fichier_historique, 'w') as file:
        json.dump(historique_conversions, file)

# Appeler la fonction pour sauvegarder l'historique
save_historique()

print("Programme Terminé")
