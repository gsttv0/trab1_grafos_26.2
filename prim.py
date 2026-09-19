class Prim:

    def __init__(self, grafo):

        self.grafo = grafo
        self.agm = []
        self.custo = 0


    def executar(self, inicio):

        if self.grafo.direcionado:
            raise ValueError(
                "o algoritmo de Prim funciona em grafos nao direcionados."
            )

        if inicio not in self.grafo.vertices:
            raise ValueError(f"o vertice '{inicio}' nao existe.")

        self.agm = []
        self.custo = 0

        visitados = {inicio}

        while len(visitados) < len(self.grafo.vertices):

            menor_aresta = None
            novo_vertice = None

            for id in visitados:

                for aresta in self.grafo.lista_adjacencia[id]:

                    vizinho = self.grafo.outro_extremo(aresta, id)

                    if vizinho in visitados:
                        continue

                    if menor_aresta is None or aresta.val < menor_aresta.val:
                        menor_aresta = aresta
                        novo_vertice = vizinho

            if menor_aresta is None:
                self.agm = []
                self.custo = 0
                raise ValueError("o grafo nao eh conexo.")

            self.agm.append(menor_aresta)
            self.custo += menor_aresta.val
            visitados.add(novo_vertice)


    def texto(self):

        texto = "ARVORE GERADORA MINIMA - PRIM\n\n"

        if not self.agm:
            return texto + "AGM sem arestas (grafo com um unico vertice).\n"

        for aresta in self.agm:
            texto += (
                f"{aresta.id}: {aresta.orig} -- {aresta.dest} "
                f"| peso = {aresta.val}\n"
            )

        texto += f"\nCusto total da AGM: {self.custo}\n"

        return texto
