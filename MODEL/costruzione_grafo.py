import networkx as nx


class Model:
    def __init__(self):
        #inizializza liste DAO

        self._G= nx.Graph()         #grafo non orientato   nx.DiGraph   grafo orientato
        self._lista_nodi = []
        self._dict_nodi = {}
        self._lista_archi = []

        #definire variabili della ricorsione

    #  def load_materiale_dao(self):
    #           inizializza liste DAO= funzioni DAO
    #
    #   SE HANNO PARAMETRO FAI SOLO RETURN E LE CHIAMO NEL CONTROLLER


    def BuildGraph(self):
        self._G.clear()
        self._lista_nodi = []
        self._lista_archi = []

        #(CREAZIONE NODI GRAFO)-----------------------------------------------------------------------#
        for node in self.lista_dao:
            self._lista_nodi.append(node)
        self._G.add_nodes_from(self._lista_nodi)

        self._dict_nodi = {}
        for node in self._lista_nodi:
            self._dict_nodi[node.cromosoma] = node

        #(CREAZIONE ARCHI GRAFO)---------------------------------------------------------------------#

        #metodo1 (LAB13 geni)------------------------------------------------------------------------#
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

        #STANDARD------------------------------------------------------------------------#
        self._lista_archi = DAO.readArchi(self._dict_nodi)
        for u, v, peso in self._lista_archi:
            self._graf.add_edge(u, v, weight=peso)

        # (2)(ITUNES)------------------------------------------------------------------------#
        #creazione archi sfalsando iterazione di 1 quindi: (1-2,1-3,1-4,2-3,2-4,3-4) piu uso dei set
        for i, a1 in enumerate(self.albums):
            for a2 in self.albums[i + 1:]:
                if self.album_playlist_map[a1] & self.album_playlist_map[a2]:
                    self.G.add_edge(a1, a2)

        #caso molto simile in BASEBALL
        for i, t1 in enumerate(self.teams):
            for t2 in self.teams[i + 1:]:
                w = self.salary_map.get(t1.id, 0) + self.salary_map.get(t2.id, 0)
                self.G.add_edge(t1, t2, weight=w)


        #DARE UN OCCHIO AL MODEL DI METROPARIS!!!




