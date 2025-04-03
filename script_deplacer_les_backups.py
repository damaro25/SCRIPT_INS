# import os
# import pandas as pd 
# df = pd.read_excel("F:/backup_agent_carto/liste_fichiers_zip.xlsx", sheet_name="Feuil5")
# print(df["Nom du fichier"])
import os
import shutil
import pandas as pd

# 📍 Dossier source contenant les fichiers ZIP à copier
dossier_source = "F:/backup_agent_carto/"  # à adapter

# 📍 Dossier de destination où tu veux copier les ZIP
dossier_destination = "F:/backup_agent_carto/final_zip"  # à adapter

# 📥 Chargement de la liste depuis l'Excel
df = pd.read_excel("F:/backup_agent_carto/liste_fichiers_zip.xlsx", sheet_name="Feuil5")

# 🔁 Parcours de chaque fichier dans la colonne
for nom_fichier in df["Nom du fichier"]:
    chemin_source = os.path.join(dossier_source, nom_fichier)
    chemin_destination = os.path.join(dossier_destination, nom_fichier)
    
    # Vérifie que le fichier existe avant de copier
    if os.path.exists(chemin_source):
        shutil.copy2(chemin_source, chemin_destination)
        print(f"✅ Copié : {nom_fichier}")
    else:
        print(f"❌ Fichier introuvable : {nom_fichier}")

print("✅ Copie terminée.")
