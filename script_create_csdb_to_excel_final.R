library(DBI)
library(RSQLite)
library(writexl)
library(tidyverse)

# 1. Dossier contenant les fichiers .csdb
dossier_csdb <- "F:/backup_agent_carto/final_zip/testdic"
output <- "/Output/"

# 2. Liste de tous les fichiers .csdb
liste_fichiers <- list.files(path = dossier_csdb, pattern = "\\.csdb$", full.names = TRUE)

# 3. Parcours de chaque fichier .csdb
for (i in seq_along(liste_fichiers)) {
  chemin_csdb <- liste_fichiers[i]
  nom_fichier <- basename(chemin_csdb)  # nom du fichier sans le chemin
  
  # Connexion à la base SQLite
  con <- dbConnect(RSQLite::SQLite(), chemin_csdb)
  
  # Vérifie si les deux tables existent
  tables_dispo <- dbListTables(con)
  if (all(c("repertoire_localite_rec", "level-1") %in% tables_dispo)) {
    #df1 <- dbReadTable(con, "district_rec")
    df1 <- dbReadTable(con, "district_rec")
    df2 <- dbReadTable(con, "level-1")
    
    # Jointure et ajout de la colonne source
    df_final <- left_join(df1, df2) %>%  # adapte la clé si nécessaire
      mutate(fichiersource = nom_fichier)
    
    # Nom du fichier Excel de sortie
    nom_fichier_xlsx <- file.path(dossier_csdb,output, paste0(tools::file_path_sans_ext(nom_fichier), ".xlsx"))
    
    # Export
    write_xlsx(df_final, nom_fichier_xlsx)
    
    cat("✅ Export terminé pour :", nom_fichier_xlsx, "\n")
  } else {
    cat("⚠️ Tables manquantes dans :", nom_fichier, "\n")
  }
  
  # Fermeture de la connexion
  dbDisconnect(con)
}
