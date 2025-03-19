import pickle

# Fonction pour charger les données de zoo.p
def charger_zoo():
    try:
        with open('zoo.p', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Le fichier zoo.p n'existe pas encore. Création d'un nouveau fichier.")
        return {}

# Fonction pour sauvegarder les données dans zoo.p
def sauvegarder_zoo(zoo):
    with open('zoo.p', 'wb') as f:
        pickle.dump(zoo, f)
    print("Les modifications ont été sauvegardées dans 'zoo.p'.")

# Fonction pour afficher les animaux
def afficher_animaux(zoo):
    if not zoo:
        print("Le zoo est vide !")
    else:
        print("\nAnimaux présents dans le zoo :")
        for animal, details in zoo.items():
            print(f"- {animal.capitalize()} : {details['espèce']} (Âge: {details['âge']} ans, Enclos: {details['enclos']}, Régime: {details['régime']})")

# Fonction pour ajouter un animal
def ajouter_animal(zoo):
    nom = input("Entrez le nom de l'animal : ").lower()
    espece = input("Entrez l'espèce de l'animal : ")
    age = int(input("Entrez l'âge de l'animal (en années) : "))
    enclos = int(input("Entrez le numéro de l'enclos de l'animal : "))
    regime = input("Entrez le régime alimentaire de l'animal (carnivore/herbivore) : ").lower()

    zoo[nom] = {
        "espèce": espece,
        "âge": age,
        "enclos": enclos,
        "régime": regime
    }
    print(f"L'animal {nom.capitalize()} a été ajouté au zoo.")

# Fonction pour supprimer un animal
def supprimer_animal(zoo):
    nom = input("Entrez le nom de l'animal à supprimer : ").lower()
    if nom in zoo:
        del zoo[nom]
        print(f"L'animal {nom.capitalize()} a été supprimé du zoo.")
    else:
        print("Cet animal n'existe pas dans le zoo.")

# Menu principal
def afficher_menu():
    print("\n--- MENU DE GESTION DU ZOO ---")
    print("1. Afficher les animaux")
    print("2. Ajouter un animal")
    print("3. Supprimer un animal")
    print("4. Sauvegarder les modifications")
    print("5. Quitter")

# Programme principal
def main():
    zoo = charger_zoo()

    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-5) : ")

        if choix == '1':
            afficher_animaux(zoo)
        elif choix == '2':
            ajouter_animal(zoo)
        elif choix == '3':
            supprimer_animal(zoo)
        elif choix == '4':
            sauvegarder_zoo(zoo)
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir un numéro entre 1 et 5.")

if __name__ == "__main__":
    main()
