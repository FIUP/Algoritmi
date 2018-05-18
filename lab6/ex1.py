''' Create un'immagine dei 15 cluster generati applicando l'algoritmo di Clustering Gerarchico
al set di dati completo con 3108 contee. Utilizzate un colore diverso per identificare ogni cluster.
È possibile allegare un'immagine con le 3108 contee colorate per cluster o una visualizzazione ottimizzata
con le contee colorate per cluster e collegate al centro dei relativi cluster con delle linee.
Non è necessario includere assi, etichette degli assi o un titolo per questa immagine.  '''

import csv

def readFromFile(path):
    county_data = {}
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            id = row[0]
            x, y = float(row[1]), float(row[2])
            people = int(row[3])
            cancer_sil = float(row[4])
            county_data[id] = [(x,y),people,county_data]
            break

    return county_data

print(readFromFile("data/unifiedCancerData_3108.csv"))
