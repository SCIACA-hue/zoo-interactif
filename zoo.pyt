import pickle

zoo = {
    "lion": {
        "espèce": "Panthera leo",
        "âge": 5,
        "enclos": 1,
        "régime": "carnivore"
    },
    "éléphant": {
        "espèce": "Loxodonta africana",
        "âge": 12,
        "enclos": 2,
        "régime": "herbivore"
    },
    "zèbre": {
        "espèce": "Equus quagga",
        "âge": 7,
        "enclos": 3,
        "régime": "herbivore"
    }
}

# Sauvegarde dans le fichier zoo.p
with open('zoo.p', 'wb') as f:
    pickle.dump(zoo, f)

