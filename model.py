import networkx as nx


class Model:
    def __init__(self):
        #inizializza liste DAO

        self._G= nx.Graph()         #grafo non orientato   nx.DiGraph   grafo orientato
        self._lista_nodi = []
        self._dict_nodi = {}
        self._lista_archi = []

    #  def load_materiale_dao(self):
    #           inizializza liste DAO= funzioni DAO
    #
    #   SE HANNO PARAMETRO FAI SOLO RETURN E LE CHIAMO NEL CONTROLLER

    # CREO DIZIONARIO PER NODI.ID ---> OBJ
    self._dict_nodi = {}
    for node in self._lista_nodi:
        self._dict_nodi[node.cromosoma] = node
    #O in BuildGraf oppure in load_nodi dal DAO




    def BuildGraf(self):
        self._G.clear()
        self._lista_nodi = []
        self._lista_archi = []

        #CREAZIONE NODI GRAFO
        for node in self.lista_dao:
            self._lista_nodi.append(node)
        self._G.add_nodes_from(self._lista_nodi)

        #CREAZIONE ARCHI GRAFO

        #metodo1 (LAB13 geni)
        #Il peso di ciascun arco dovrà essere calcolato come la somma algebrica della correlazione
        #(tabella interazione, colonna correlazione), facendo attenzione a contare ogni coppia di geni una sola volta.
        edges = {}
        for id1, id2, peso in self._lista_edge_dao:
            obj1 = self._dict_nodi[id1]
            obj2 = self._dict_nodi[id2]

            if (obj1, obj2) not in edges:
                edges[( obj1, obj2)] = float(PESO)
            else:
                edges[(obj1, obj2 )] += float(PESO)

        for k, v in edges.items():
            self.lista_edges.append((k[0], k[1], v))
        self.G.add_weighted_edges_from(self._edges)


#ALTERNATIVA


    # funzione per buildare il grafo
    def BuildGraf(self):
        self._lista_nodi = DAO.readNodi()
        for node in self._lista_nodi:
            self._dict_nodi[node.id] = node
            self._graf.add_node(node)

        self._lista_archi = DAO.readArchi(self._dict_nodi)
        for u, v, peso in self._lista_archi:
            self._graf.add_edge(u, v, weight=peso)

    # funzione per cercare valore minimo e massimo dei pesi degli archi.
    def getMaxWeight(self):
        pesoMax = max(self._graf.edges(data=True), key=lambda edge: edge[2]['weight'])
        return pesoMax[-1]['weight']

    def getMinWeight(self):
        pesoMin = min(self._graf.edges(data=True), key=lambda edge: edge[2]['weight'])
        return pesoMin[-1]['weight']

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

    # funzione che restituisce una lista di nodi connessi con un nodo START
    def get_component(self, start):
        if start not in self._G:
            return []
        return list(nx.node_connected_component(self._G, start))

    #Riceve l’ID di un nodo (tipicamente come stringa dalla GUI),
    # lo converte tramite un dizionario di mapping nel nodo reale del grafo,
    # esegue una visita in ampiezza (BFS) a partire da quel nodo e restituisce
    # il sottografo BFS che contiene tutti e soli i nodi raggiungibili da esso,
    # cioè in pratica tutta la parte del grafo collegata a quel nodo.
    def get_connected_component(self, album_id):
        album = self._node_dict[int(album_id)]
        return nx.bfs_tree(self.G, album)

    # funzione per calcolare peso di un percorso
    def calcolaPeso(self, listaNodi):
        pesoTotale = 0;
        for i in range(0, len(listaNodi) - 1):
            u = listaNodi[i]
            v = listaNodi[i + 1]
            pesoTotale += self._graf[u][v]["weight"]
        return pesoTotale

    # funzione per calcolare il peso di tutti gli archi tra un nodo e i suoi adiacenti
    def get_peso_archi_adiacenti(self, node):
        peso = 0
        for vicino in self._G.neighbors(node):
            peso += int(self._G[node][vicino]['weight'])
        return peso

    # funzione per calcolare la DISTANZA tra due nodi
    def get_distance(self, nodo1, nodo2):
        distanza = distance.geodesic((nodo1.lat, nodo1.lng), (nodo2.lat, nodo2.lng)).km
        return distanza

    #Riceve l’ID di un nodo, lo converte nel nodo reale del grafo tramite un
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

----------------------------------------------------------------------------------------------------------

# RICORSIONE per il cammino massimo passando solo per archi con peso > o < di una soglia partendo da un nodo a caso
def getPercorsoMassimo(self, soglia):
    self._soluzioneMigliore = []  # Lista di nodi
    self._pesoMigliore = 0

    for v_iniziale in self._lista_nodi:
        parziale = [v_iniziale]
        self.ricorsione(parziale, soglia)

    return self._soluzioneMigliore, self._pesoMigliore

def ricorsione(self, parziale, soglia):
    # Qui ho una possibile soluzione
    # Verifico se sia "migliore" della attuale migliore,
    # ovvero se il suo peso sia maggiore del peso
    # massimo finora trovato per le soluzioni precedenti
    if self.calcolaPeso(parziale) > self._pesoMigliore:
        self._pesoMigliore = self.calcolaPeso(parziale)
        self._soluzioneMigliore = copy.deepcopy(parziale)
        if len(parziale) == len(self._lista_nodi):
            return

    # Altrimenti qui faccio ricorsione
    for v in self._graf.neighbors(parziale[-1]):  # Vicini dell'ultimo nodo aggiunto
        if v in parziale:
            continue
        if self._graf[parziale[-1]][v]['weight'] <= soglia:
            continue
        parziale.append(v)
        self.ricorsione(parziale, soglia)
        parziale.pop()

def calcolaPeso(self, listaNodi):
    pesoTotale = 0;
    for i in range(0, len(listaNodi) - 1):
        u = listaNodi[i]
        v = listaNodi[i + 1]
        pesoTotale += self._graf[u][v]["weight"]
    return pesoTotale

# ricorsione partendo da un nodo start che includa solo nodi connessi con a e che massimizzi il
# numero di nodi, il peso complessivo deve essere minore di un peso soglia
def _cerca_massimo_cammino(self, durata_max, album_partenza):
    self._result = [album_partenza]
    self._durata_reale = 0
    self.ricorsione([album_partenza], album_partenza.durata, durata_max)

    return self._result, self._durata_reale

def ricorsione(self, risultato_parziale, durata_parziale, durata_max):
    if durata_parziale > durata_max:
        return
    if len(risultato_parziale) > len(self._result):
        self._result = copy.deepcopy(risultato_parziale)
        self._durata_reale = copy.deepcopy(durata_parziale)
        print(self._result)
        print(self._durata_reale)

    for vicino in self.G.neighbors(risultato_parziale[-1]):
        print(vicino.title)
        if vicino in risultato_parziale:
            continue
        risultato_parziale.append(vicino)
        self.ricorsione(risultato_parziale, durata_parziale + vicino.durata, durata_max)
        risultato_parziale.pop()

# ricorsione che cerca percorso con distanza massima con nodi con peso crescente
def cerca_percorso(self):
    self.best_path = []
    self.best_distance = 0
    for node in self._G.nodes:
        self._ricorsione([node], 0, float("-inf"))
    return self.best_path, self.best_distance

def _ricorsione(self, path, distance, last_edge_weight):
    last = path[-1]
    if distance > self.best_distance:
        self.best_distance = distance
        self.best_path = path.copy()

    vicini = self._G.neighbors(last)

    for node in vicini:
        edge_w = self._G[last][node]['weight']
        if edge_w > last_edge_weight:
            path.append(node)
            d = self.get_distance(last, node)
            self._ricorsione(path, distance + d, edge_w)
            path.pop()

# ricorsione che cerca percorso peso massimo con nodo di partenza, con peso archi decrescente,
# visitando solo i primi K nodi adiacenti piu pesanti
def get_lista_squadre(self, squadra_partenza):
    lista_vicini = sorted(self._G.neighbors(squadra_partenza), key=lambda x: x.somma_stipendi, reverse=True)
    return lista_vicini

def trova_percorso(self, squadra_partenza, K=3):
    self._result = [squadra_partenza]
    self._costo_finale = 0
    self.ricorsione([squadra_partenza], 0, K, float("inf"))
    return self._result, self._costo_finale

def ricorsione(self, risultato_parziale, costo_parziale, K, peso_ultimo):
    if costo_parziale > self._costo_finale:
        self._result = copy.deepcopy(risultato_parziale)
        self._costo_finale = costo_parziale

    nodo = risultato_parziale[-1]

    candidati = []
    for vicino in self._G.neighbors(nodo):
        if vicino not in risultato_parziale:
            peso = self._G[nodo][vicino]["weight"]
            if peso < peso_ultimo:
                candidati.append((vicino, peso))

    candidati.sort(key=lambda x: x[1], reverse=True)
    candidati = candidati[:K]

    for vicino, peso in candidati:
        risultato_parziale.append(vicino)
        self.ricorsione(risultato_parziale, costo_parziale + peso, K, peso)
        risultato_parziale.pop()