#----------------------------------------------------------------------------------------#
# funzione per cercare valore minimo e massimo dei pesi degli archi.
def getMaxWeight(self):
    pesoMax = max(self._graf.edges(data=True), key=lambda edge: edge[2]['weight'])
    return pesoMax[-1]['weight']

def getMinWeight(self):
    pesoMin = min(self._graf.edges(data=True), key=lambda edge: edge[2]['weight'])
    return pesoMin[-1]['weight']
#----------------------------------------------------------------------------------------#
# funzione che conta il numero di archi con peso > o < di una soglia
def count_edges_by_threshold(self, soglia):
    num_minori = 0
    num_maggiori = 0
    for edge in self._lista_archi:
        peso = edge[-1]
        if peso < soglia:
            num_minori += 1
        elif peso > soglia:
            num_maggiori += 1
    return num_minori, num_maggiori
#----------------------------------------------------------------------------------------#
# funzione che restituisce una lista di nodi connessi con un nodo START
def get_component(self, start):
    if start not in self._G:
        return []
    return list(nx.node_connected_component(self._G, start))
#----------------------------------------------------------------------------------------#
# Riceve l’ID di un nodo (tipicamente come stringa dalla GUI),
# lo converte tramite un dizionario di mapping nel nodo reale del grafo,
# esegue una visita in ampiezza (BFS) a partire da quel nodo e restituisce
# il sottografo BFS che contiene tutti e soli i nodi raggiungibili da esso,
# cioè in pratica tutta la parte del grafo collegata a quel nodo.
def get_connected_component(self, album_id):
    album = self._node_dict[int(album_id)]
    return nx.bfs_tree(self.G, album)
#----------------------------------------------------------------------------------------#
# funzione per calcolare peso di un percorso
def calcolaPeso(self, listaNodi):
    pesoTotale = 0;
    for i in range(0, len(listaNodi) - 1):
        u = listaNodi[i]
        v = listaNodi[i + 1]
        pesoTotale += self._graf[u][v]["weight"]
    return pesoTotale
#----------------------------------------------------------------------------------------#
# funzione per calcolare il peso di tutti gli archi tra un nodo e i suoi adiacenti
def get_peso_archi_adiacenti(self, node):
    peso = 0
    for vicino in self._G.neighbors(node):
        peso += int(self._G[node][vicino]['weight'])
    return peso
#----------------------------------------------------------------------------------------#
# funzione per calcolare la DISTANZA tra due nodi
def get_distance(self, nodo1, nodo2):
    distanza = distance.geodesic((nodo1.lat, nodo1.lng), (nodo2.lat, nodo2.lng)).km
    return distanza
#----------------------------------------------------------------------------------------#
# Riceve l’ID di un nodo, lo converte nel nodo reale del grafo tramite un
# dizionario di mapping e, a partire da esso, analizza la porzione di grafo
# collegata in tre modi diversi: usando dfs_successors(G, nodo) per ottenere
# i nodi raggiungibili seguendo solo gli archi uscenti durante una visita in
# profondità, usando dfs_predecessors(G, nodo) per individuare i nodi dai quali
# il nodo sorgente è raggiungibile seguendo gli archi entranti,
# e usando dfs_tree(G, nodo) per costruire l’albero di visita DFS che rappresenta
# l’insieme completo dei nodi esplorabili dal nodo sorgente, restituendo infine
# la dimensione di questa parte connessa come numero di nodi dell’albero.
def calcolaConnessa(self, id_nodo):
    nodo_sorgente = self._objects_dict[id_nodo]
    # Usando i successori
    successori = nx.dfs_successors(self._grafo, nodo_sorgente)
    print(f"Successori: {len(successori)}")
    # Usando i predecessori (ma devo poi increm. di 1)
    prededessori = nx.dfs_predecessors(self._grafo, nodo_sorgente)
    print(f"Prededessori: {len(prededessori)}")
    # Ottenendo l'albero di visita
    albero = nx.dfs_tree(self._grafo, nodo_sorgente)
    print(f"Albero: {albero}")
    return len(albero.nodes)
#----------------------------------------------------------------------------------------#
#trova vicini di un nodo e tieni la coppia nodo-peso
def get_neighbors(self, team):
    vicini = []
    for n in self.G.neighbors(team):
        w = self.G[team][n]["weight"]
        vicini.append((n, w))
    return sorted(vicini, key=lambda x: x[1], reverse=True)
#----------------------------------------------------------------------------------------#
#per ogni nodo somma il peso dei vicini
def get_sum_weight_per_node(self):
    pp = []
    for n in self.G.nodes():
        sum_w = 0
        for e in self.G.edges(n, data=True):
            sum_w += e[2]['weight']
        pp.append((n.id, sum_w))
    return pp
#----------------------------------------------------------------------------------#
#calcolo distanze con geodesic
from geopy import distance
  def get_distance_weight(self, e):
        return distance.geodesic((e[0].lat, e[0].lng),
                                 (e[1].lat, e[1].lng)).km
#-----------------------------------------------------------------------------------#
# Calcola un punteggio per ogni nodo del grafo come
# somma dei pesi degli archi uscenti meno quelli entranti.
# Ordina i nodi per punteggio decrescente e restituisce i migliori.
def get_best_prodotti(self):
    best_prodotti = []
    for n in self.G.nodes:
        score = 0
        for e_out in self.G.out_edges(n, data=True):
            score += e_out[2]["weight"]
        for e_in in self.G.in_edges(n, data=True):
            score -= e_in[2]["weight"]

        best_prodotti.append((n, score))

    best_prodotti.sort(reverse=True, key=lambda x: x[1])
    return best_prodotti[0:5]
#------------------------------------------------------------------------------------#