class Busca:

    def __init__(self, grafo):

        self.grafo = grafo
        self.visitados = []
        self.arvore = []
        self.caminho = []
        self.encontrou = False


    def executar(self, saida, chegada):

        if saida not in self.grafo.vertices:
            raise ValueError(f"o vertice '{saida}' nao existe.")

        if chegada not in self.grafo.vertices:
            raise ValueError(f"o vertice '{chegada}' nao existe.")

        self.visitados = [saida]
        self.arvore = []
        self.caminho = []
        self.encontrou = saida == chegada

        pai = {saida: None}
        indice = {saida: 0}
        pilha = [saida]

        while pilha and not self.encontrou:

            atual = pilha[-1]

            adjacentes = self.grafo.lista_adjacencia[atual]

            if indice[atual] == len(adjacentes):
                pilha.pop()
                continue

            aresta = adjacentes[indice[atual]]

            indice[atual] += 1

            vizinho = self.grafo.outro_extremo(aresta, atual)

            if vizinho in pai:
                continue

            pai[vizinho] = aresta
            indice[vizinho] = 0

            self.visitados.append(vizinho)
            self.arvore.append(aresta)
            pilha.append(vizinho)

            if vizinho == chegada:
                self.encontrou = True

        if self.encontrou:

            atual = chegada

            while pai[atual] is not None:
                self.caminho.append(pai[atual])
                atual = self.grafo.outro_extremo(pai[atual], atual)

            self.caminho.reverse()


    def texto(self, saida, chegada):

        texto = f"BUSCA EM PROFUNDIDADE: {saida} -> {chegada}\n\n"

        texto += "Ordem de visita: " + ", ".join(self.visitados) + "\n\n"

        texto += "Arestas/arcos da arvore gerada:\n"

        if not self.arvore:
            texto += "  (nenhuma)\n"

        for aresta in self.arvore:
            texto += f"  {aresta.id}: {aresta.orig} - {aresta.dest}\n"

        texto += "\n"

        if not self.encontrou:
            return texto + f"Nao existe caminho de {saida} ate {chegada}.\n"

        custo = sum(aresta.val for aresta in self.caminho)

        texto += "Caminho encontrado:\n"

        atual = saida

        texto += f"  {atual}"

        for aresta in self.caminho:
            atual = self.grafo.outro_extremo(aresta, atual)
            texto += f" -[{aresta.id}]-> {atual}"

        texto += f"\n\nCusto do caminho: {custo}\n"

        return texto
