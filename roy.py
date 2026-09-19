class Roy:

    def __init__(self, grafo):

        self.grafo = grafo
        self.componentes = []


    def alcancar(self, inicio, vizinhos):

        marcados = {inicio}
        pilha = [inicio]

        while pilha:

            atual = pilha.pop()

            for vizinho in vizinhos[atual]:

                if vizinho not in marcados:
                    marcados.add(vizinho)
                    pilha.append(vizinho)

        return marcados


    def executar(self):

        if len(self.grafo.vertices) == 0:
            raise ValueError("o grafo esta vazio.")

        self.componentes = []

        sucessores = {id: [] for id in self.grafo.vertices}
        antecessores = {id: [] for id in self.grafo.vertices}

        for id in self.grafo.vertices:

            for aresta in self.grafo.lista_adjacencia[id]:

                vizinho = self.grafo.outro_extremo(aresta, id)

                sucessores[id].append(vizinho)
                antecessores[vizinho].append(id)

        atribuidos = set()

        for id in self.grafo.vertices:

            if id in atribuidos:
                continue

            descendentes = self.alcancar(id, sucessores)
            ascendentes = self.alcancar(id, antecessores)

            componente = []

            for outro in self.grafo.vertices:

                if outro in descendentes and outro in ascendentes:
                    componente.append(outro)

            atribuidos.update(componente)

            self.componentes.append(componente)


    def texto(self):

        if self.grafo.direcionado:
            nome = "FORTEMENTE CONEXAS"
        else:
            nome = "CONEXAS"

        texto = f"ALGORITMO DE ROY - COMPONENTES {nome}\n\n"

        texto += f"Quantidade de componentes: {len(self.componentes)}\n\n"

        for i, componente in enumerate(self.componentes, start=1):
            texto += f"C{i} = {{ " + ", ".join(componente) + " }\n"

        return texto
