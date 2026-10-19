class Prim:

    def __init__(self, grafo):

        self.grafo = grafo
        self.agm = [] #arvore geradora minima
        self.custo = 0


    def executar(self, inicio):

        if self.grafo.direcionado:
            raise ValueError(
                "o algoritmo de Prim funciona em grafos NAO direcionados."
            )

        if inicio not in self.grafo.vertices:
            raise ValueError(f"o vertice '{inicio}' nao existe.")

        self.agm = []
        self.custo = 0

        visitados = {inicio} #vert inicial ja entra como visitado 

        while len(visitados) < len(self.grafo.vertices): #faz enquanto visitados for menor q total de verts

            menor_arco = None
            novo_vertice = None

            for id in visitados:

                for arco in self.grafo.lista_adjacencia[id]: #pega os arcos do vertice atual

                    vizinho = self.grafo.outro_extremo(arco, id) #pega o outro vertice do arco

                    if vizinho in visitados: #verifica se ja foi visitado 
                        continue

                    if menor_arco is None or arco.val < menor_arco.val: #verifica se o arco atual eh menor q a menor arco ja encontrada
                        menor_arco = arco
                        novo_vertice = vizinho

            if menor_arco is None: #se nao encontrar nenhum arco, o grafo nao eh conexo
                self.agm = []
                self.custo = 0
                raise ValueError("o grafo nao eh conexo.")

            self.agm.append(menor_arco)
            self.custo += menor_arco.val
            visitados.add(novo_vertice)


    def texto(self):

        texto = "ARVORE GERADORA MINIMA - PRIM\n\n"

        if not self.agm:
            return texto + "AGM sem arcos (grafo com um unico vertice).\n"

        for arco in self.agm:
            texto += (
                f"{arco.id}: {arco.orig} -- {arco.dest} "
                f"| peso = {arco.val}\n"
            )

        texto += f"\nCusto total da AGM: {self.custo}\n"

        return texto
