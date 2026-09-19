from vertice import Vertice
from aresta import Aresta


class Grafo:

    def __init__(self, direcionado=False):

        self.direcionado = direcionado
        self.vertices = {}
        self.arestas = {}
        self.lista_adjacencia = {}


    def inserir_vertice(self, id):

        if id in self.vertices:
            raise ValueError(f"o vertice '{id}' ja existe.")

        self.vertices[id] = Vertice(id)
        self.lista_adjacencia[id] = []


    def inserir_aresta(self, id, orig, dest, val):

        if orig not in self.vertices:
            raise ValueError(f"o vertice '{orig}' nao existe.")

        if dest not in self.vertices:
            raise ValueError(f"o vertice '{dest}' nao existe.")

        if id in self.arestas:
            raise ValueError(f"a aresta/arco '{id}' ja existe.")

        aresta = Aresta(id, orig, dest, val)

        self.arestas[id] = aresta

        self.lista_adjacencia[orig].append(aresta)

        if not self.direcionado and orig != dest:
            self.lista_adjacencia[dest].append(aresta)


    def remover_aresta(self, id):

        if id not in self.arestas:
            raise ValueError(f"a aresta/arco '{id}' nao existe.")

        aresta = self.arestas[id]

        self.lista_adjacencia[aresta.orig].remove(aresta)

        if not self.direcionado and aresta.orig != aresta.dest:
            self.lista_adjacencia[aresta.dest].remove(aresta)

        del self.arestas[id]


    def remover_vertice(self, id):

        if id not in self.vertices:
            raise ValueError(f"o vertice '{id}' nao existe.")

        arestas_remover = []

        for aresta in self.arestas.values():

            if aresta.orig == id or aresta.dest == id:
                arestas_remover.append(aresta.id)

        for id_aresta in arestas_remover:
            self.remover_aresta(id_aresta)

        del self.vertices[id]
        del self.lista_adjacencia[id]


    def outro_extremo(self, aresta, id):

        if aresta.orig == id:
            return aresta.dest

        return aresta.orig


    def texto_lista_adjacencia(self):

        if len(self.vertices) == 0:
            return "LISTA DE ADJACENCIA\n\nGrafo vazio."

        seta = "->" if self.direcionado else "--"

        texto = "LISTA DE ADJACENCIA\n\n"

        for id in self.vertices:

            texto += f"{id} :"

            for aresta in self.lista_adjacencia[id]:

                vizinho = self.outro_extremo(aresta, id)

                texto += f"  {seta} {vizinho} [{aresta.id}, peso={aresta.val}]"

            texto += "\n"

        return texto


    def matriz_adjacencia(self):

        vertices = list(self.vertices)

        posicao = {id: i for i, id in enumerate(vertices)}

        matriz = [[0 for _ in vertices] for _ in vertices]

        for aresta in self.arestas.values():

            i = posicao[aresta.orig]
            j = posicao[aresta.dest]

            matriz[i][j] = 1

            if not self.direcionado:
                matriz[j][i] = 1

        return vertices, matriz


    def matriz_incidencia(self):

        vertices = list(self.vertices)
        arestas = list(self.arestas.values())

        posicao = {id: i for i, id in enumerate(vertices)}

        matriz = [[0 for _ in arestas] for _ in vertices]

        for j, aresta in enumerate(arestas):

            i_orig = posicao[aresta.orig]
            i_dest = posicao[aresta.dest]

            if aresta.orig == aresta.dest:

                matriz[i_orig][j] = 2

            elif self.direcionado:

                matriz[i_orig][j] = 1
                matriz[i_dest][j] = -1

            else:

                matriz[i_orig][j] = 1
                matriz[i_dest][j] = 1

        return vertices, [a.id for a in arestas], matriz


    def formatar_matriz(self, titulo, linhas, colunas, matriz):

        if len(linhas) == 0:
            return f"{titulo}\n\nGrafo vazio."

        if len(colunas) == 0:
            return f"{titulo}\n\nO grafo nao possui arestas/arcos."

        largura = max(len(str(x)) for x in linhas + colunas) + 3

        texto = f"{titulo}\n\n"

        texto += " " * largura

        for coluna in colunas:
            texto += f"{str(coluna):^{largura}}"

        texto += "\n"

        for i in range(len(linhas)):

            texto += f"{str(linhas[i]):^{largura}}"

            for j in range(len(colunas)):
                texto += f"{matriz[i][j]:^{largura}}"

            texto += "\n"

        return texto


    def texto_matriz_adjacencia(self):

        vertices, matriz = self.matriz_adjacencia()

        return self.formatar_matriz(
            "MATRIZ DE ADJACENCIA", vertices, vertices, matriz
        )


    def texto_matriz_incidencia(self):

        vertices, arestas, matriz = self.matriz_incidencia()

        return self.formatar_matriz(
            "MATRIZ DE INCIDENCIA", vertices, arestas, matriz
        )
