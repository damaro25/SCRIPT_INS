import pandas as pd
import os
list_fichiers = os.listdir("E:/backup_agent_carto/final_zip/Output_final_ilot_loc_dist/ilot_Output") 
print(len(list_fichiers))

dist = []

dist = [ pd.read_excel("E:/backup_agent_carto/final_zip/Output_final_ilot_loc_dist/ilot_Output/{}".format(f))  for f in list_fichiers[:50]]
print(dist[0].info())

#print(dist[1].info())
data = pd.concat(dist)
#data.to_csv("E:/backup_agent_cartofinal_zip/Output_final_ilot_loc_dist/final_output/ilot_final.csv", index=False)
print(data.head())



