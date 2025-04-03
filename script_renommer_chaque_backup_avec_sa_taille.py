import os
import pandas as pd

# Spécifie le chemin du dossier à analyser
dossier = 'F:/backup_agent_carto'  # ⬅️ à modifier

# Liste pour stocker les infos
data = []

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier):
    if fichier.lower().endswith('.zip'):
        chemin_fichier = os.path.join(dossier, fichier)
        taille_octets = os.path.getsize(chemin_fichier)
        taille_mo = round(taille_octets / (1024 * 1024), 2)  # Taille en Mo
        data.append([fichier, taille_mo])

# Création du DataFrame
df = pd.DataFrame(data, columns=['Nom du fichier', 'Taille (Mo)'])

# Export vers Excel
df.to_excel('liste_fichiers_zip.xlsx', index=False)

print("Export terminé avec succès dans 'liste_fichiers_zip.xlsx'.")
