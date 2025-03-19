import json

# Chargement du manifest.json
with open('manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Affichage des infos principales
print("\n📄 MANIFESTE DU PROJET\n" + "-"*30)
for cle, valeur in manifest.items():
    if isinstance(valeur, dict):
        print(f"{cle} :")
        for sous_cle, v in valeur.items():
            print(f"  - {sous_cle} : {v}")
    elif isinstance(valeur, list):
        print(f"{cle} :")
        for item in valeur:
            print(f"  - {item}")
    else:
        print(f"{cle} : {valeur}")


