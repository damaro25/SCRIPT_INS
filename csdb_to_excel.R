library(DBI)
library(RSQLite)
library(writexl)  # ou use openxlsx
library(tidyverse)  

# Chemin vers ton fichier CSDB
chemin_csdb <- "F:/backup_agent_carto/final_zip/disTRICT/EXT_LOCALITE_TE_DICT_54020_backup54020_2024-12-02 07_24.csdb"
for 
# Connexion à la base SQLite
con <- dbConnect(RSQLite::SQLite(), chemin_csdb)

# Affiche les tables disponibles

df <- dbReadTable(con, "repertoire_localite_rec")
df2 <- dbReadTable(con, "level-1")

# Supposons que tu veux lire la première table


# Fermeture de la connexion
dbDisconnect(con)

df3 <- left_join(df,df2)%>%
  mutate(fichiersource=nomfichier[i])
# Export vers Excel
write_xlsx(df3, nomfichier[i])


print("✅ Export terminé dans 'eEXT_LOCALITE_TE_DICT_54020_backup54020_2024-12-02 07_24.csdb.xlsx")
