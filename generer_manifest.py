import pickle
import json
from datetime import date

# Chargement du fichier zoo.p
with open('zoo.p', 'rb') as f:
    zoo = pickle.load(f)

# Récupération des espèces
especes = [zoo[animal]["espèce"] for animal in zoo]

# Construction du manifeste
manifest = {
    "nom_projet": "Gestion du Zoo",
    "description": "Ce projet utilise un fichier pickle (zoo.p) pour stocker les données d'un petit zoo.",
    "fichier_donnees": "zoo.p",
    "format_donnees": "dictionnaire Python",
    "structure": {
        "clé": "nom de l'animal (ex: lion)",
        "valeur": {
            "espèce": "nom scientifique",
            "âge": "entier (âge en années)",
            "enclos": "numéro d'enclos (entier)",
            "régime": "type de nourriture (carnivore/herbivore)"
        }
    },
    "especes_enregistrees": especes,
    "version": "1.0",
    "date_creation": str(date.today()),
    "dependances": ["pickle (standard Python)"],
    "auteur": "Ton Nom"
}

# Sauvegarde dans manifest.json
with open('manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=4, ensure_ascii=False)

print("✅ Le fichier 'manifest.json' a été généré automatiquement.")
