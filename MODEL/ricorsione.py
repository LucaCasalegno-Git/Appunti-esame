#--------------------------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------------------------#
# Ricorsione che parte da un album iniziale e considera solo album
# appartenenti alla sua componente connessa.
# Costruisce insiemi di album senza ripetizioni.
# Mantiene il vincolo sul peso totale (durata complessiva ≤ soglia).
# Aggiorna la soluzione migliore massimizzando il numero di album.

def compute_best_set(self, start_album, max_duration):
    """Ricerca ricorsiva del set massimo di album nella componente connessa"""
    component = self.get_component(start_album)
    self.soluzione_best = []
    self._ricorsione(component, [start_album], start_album.duration, max_duration)
    return self.soluzione_best

def _ricorsione(self, albums, current_set, current_duration, max_duration):
    if len(current_set) > len(self.soluzione_best):
        self.soluzione_best = current_set[:]

    for album in albums:
        if album in current_set:
            continue
        new_duration = current_duration + album.duration
        if new_duration <= max_duration:
            current_set.append(album)
            self._ricorsione(albums, current_set, new_duration, max_duration)
            current_set.pop()

#--------------------------------------------------------------------------------------------------------------#
# Ricorsione che esplora tutti i cammini semplici di lunghezza fissata.
# Parte da un nodo iniziale e segue solo archi diretti del grafo.
# Evita cicli controllando che un nodo non compaia già nel percorso.
# Quando il cammino è completo, verifica che termini nel nodo target.
# Calcola il punteggio come somma dei pesi degli archi del cammino.
# Mantiene il cammino con punteggio massimo come soluzione migliore.
def _ricorsione(self, parziale, lungh, start, end):
    if len(parziale) == lungh:
        if  parziale[-1] == end and self._get_score(parziale) > self.best_score:
            self.best_score = self._get_score(parziale)
            self.best_path = copy.deepcopy(parziale)
        return

    for n in self.G.successors(parziale[-1]):
        if n not in parziale:
            parziale.append(n)
            self._ricorsione(parziale, lungh, start, end)
            parziale.pop()

def _get_score(self, parziale):
    score = 0
    for i in range(1, len(parziale)):
        score += self.G[parziale[i-1]][parziale[i]]["weight"]
    return score