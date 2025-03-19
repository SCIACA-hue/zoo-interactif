import pickle
# Données du zoo
zoo = {
    "lion": {
        "espèce": "Panthera leo",
        "âge": 5,
        "enclos": 1,
        "régime": "carnivore"
    },
    "girafe": {
        "espèce": "Giraffa camelopardalis",
        "âge": 8,
        "enclos": 2,
        "régime": "herbivore"
    },
    "pingouin": {
        "espèce": "Aptenodytes forsteri",
        "âge": 3,
        "enclos": 3,
        "régime": "carnivore"
    }
}

# Sauvegarde dans un fichier pickle (binaire)
with open('zoo.p', 'wb') as f:
    pickle.dump(zoo, f)

print("Le fichier 'zoo.p' a été créé avec succès !")
