import numpy as np
from collections import defaultdict

# il grafo viene rappresentato come una adj_list che, al posto del nodo destinazione,
            # ha una mappa nodo_dest -> (length, road_type) rappresentata usando un dizionario di liste.
            # {
            #   nodo_source1: {
            #                    nodo_dest1: [lenght1,road_type1],
            #                    nodo_dest2: [lenght2,road_type2]
            #                 }
            #   nodo_source2: {
            #                   nodo_dest1: [lenght1,road_type1]
            #                 }
            # }

class weightedGraphFromFile:
    def __init__(self,path):
        # la key indica il tipo della strada, il primo elemeno della lista la vel. massima e il secondo la capacita
        label_road = {
            1: [30.0,500], # strada di tipo 1 -> velocita max = 30 km/h e capacita = 500 veicoli/ora
            2: [50.0,750],
            3: [50.0,1000],
            4: [70.0,1500],
            5: [70.0,2000],
            6: [90.0,4000]
        }

        self.weighted_adj_list = defaultdict(dict)
        f = np.loadtxt(path, delimiter="\t")
        i = 0

        for line in f:
            source_node = int(line[0])
            dest_node = int(line[1])
            road_length = line[2] # in metri
            road_type = int(line[3])
            road_speed_max = label_road[road_type][0]
            road_capacity = label_road[road_type][1]
            road_time = (road_length / 1000) / road_speed_max # in ore

            if(source_node != dest_node): # no cappi
                if(source_node not in self.weighted_adj_list): # se il source_node non e' stato gia' aggiunto
                    self.weighted_adj_list[source_node] = defaultdict(list)
                self.weighted_adj_list[source_node][dest_node].extend([road_time, road_capacity]) # si potrebbe usare una tupla (immutable)?

            i = i + 1

    # OCCHIO ALLE ECCEZIONI SU QUESTI 3 METODI

    def getAdjNodes(self,source_node):
        return (self.weighted_adj_list[source_node]).keys()

    def getRoadTime(self,source_node,dest_node):
        return (self.weighted_adj_list[source_node][dest_node])[0]

    def getRoadCapacity(self,source_node,dest_node): # o road capacity?
        return (self.weighted_adj_list[source_node][dest_node])[1]
