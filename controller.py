
def handle_graph(self, e):
    """ Handler per gestire creazione del grafo """
    self._model.BuildGraf()

    self._view.lista_visualizzazione_1.controls.clear()
    self._view.lista_visualizzazione_1.controls.append(ft.Text(f' '))

    self._view.button.disabled = False
    self._view.update()


# Metodo per popolare i dropdown
def populate_dd(self):

    for year in self._model.get_year():
        self._view.dd_year.options.append(
            ft.DropdownOption(key=squadra.id, text=squadra.name))

    for shape in self._model.get_shape():
        self._view.dd_shape.options.append(
            ft.DropdownOption(f'{shape}'))

    self._view.update()



#scrittura per scrivere       nodo --> nodo  peso
for i in range(len(path) - 1):
        w = self._model.G[path[i]][path[i + 1]]["weight"]
        self._view.txt_risultato.controls.append(ft.Text(f"{path[i]} -> {path[i + 1]} (peso {w})"))
    self._view.txt_risultato.controls.append(ft.Text(f"Peso totale: {weight}"))
    self._view.update()
    
########################################################################
#PUNTO 2

def handle_ricerca(self, e):
    """ Handler per gestire il problema ricorsivo di ricerca del cammino """""

try:
    threshold = float(self._view.txt_name.value)
    self._model.ricerca_cammino(threshold)
    self._view.lista_visualizzazione_3.controls.clear()
    self._view.lista_visualizzazione_3.controls.append(
        ft.Text(f"Numero archi percorso più lungo: {len(self._model.soluzione_best)}"))
    self._view.update()

    self._view.lista_visualizzazione_3.controls.append(ft.Text(
        f"Peso cammino massimo: {str(self._model.compute_weight_path(self._model.soluzione_best))}"))

    '''for ii in self._model.soluzione_best:
        self._view.lista_visualizzazione_3.controls.append(ft.Text(
            f"{ii[0]} --> {ii[1]}: {str(ii[2]['weight'])}"))
    '''
except ValueError:
    self._view.show_alert("    ")



