from vertice import Vertice
from aresta import Aresta


class Grafo:

    def __init__(self, direcionado=False):

        self.direcionado = direcionado
        self.vertices = {}
        self.arestas = {}
        self.lista_adjacencia = {}


    # ==================================================
    # INSERIR VERTICE
    # ==================================================

    def inserir_vertice(self, id):

        if id in self.vertices:
            print(f"Erro: o vertice '{id}' ja existe.")
            return False

        vertice = Vertice(id)

        self.vertices[id] = vertice
        self.lista_adjacencia[id] = []

        return True


    # ==================================================
    # INSERIR ARESTA / ARCO
    # ==================================================

    def inserir_aresta(self, id, orig, dest, val):

        if orig not in self.vertices:
            print(f"Erro: o vertice '{orig}' nao existe.")
            return False

        if dest not in self.vertices:
            print(f"Erro: o vertice '{dest}' nao existe.")
            return False

        if id in self.arestas:
            print(f"Erro: a aresta/arco '{id}' ja existe.")
            return False

        aresta = Aresta(id, orig, dest, val)

        self.arestas[id] = aresta

        self.lista_adjacencia[orig].append(aresta)

        if not self.direcionado:
            self.lista_adjacencia[dest].append(aresta)

        return True


    # ==================================================
    # REMOVER ARESTA / ARCO
    # ==================================================

    def remover_aresta(self, id):

        if id not in self.arestas:
            print(f"Erro: a aresta/arco '{id}' nao existe.")
            return False

        aresta = self.arestas[id]

        orig = aresta.orig
        dest = aresta.dest

        self.lista_adjacencia[orig] = [
            a
            for a in self.lista_adjacencia[orig]
            if a.id != id
        ]

        if not self.direcionado:

            self.lista_adjacencia[dest] = [
                a
                for a in self.lista_adjacencia[dest]
                if a.id != id
            ]

        del self.arestas[id]

        return True


    # ==================================================
    # REMOVER VERTICE
    # ==================================================

    def remover_vertice(self, id):

        if id not in self.vertices:
            print(f"Erro: o vertice '{id}' nao existe.")
            return False

        arestas_remover = []

        for aresta in self.arestas.values():

            if aresta.orig == id or aresta.dest == id:
                arestas_remover.append(aresta.id)

        for id_aresta in arestas_remover:
            self.remover_aresta(id_aresta)

        del self.vertices[id]
        del self.lista_adjacencia[id]

        return True


    # ==================================================
    # MATRIZ DE ADJACENCIA
    # ==================================================

    def matriz_adjacencia(self):

        vertices = list(self.vertices.keys())

        quantidade = len(vertices)

        matriz = []

        for i in range(quantidade):

            linha = []

            for j in range(quantidade):

                linha.append(0)

            matriz.append(linha)


        # Relaciona cada vertice com uma posicao
        posicao = {}

        for i in range(quantidade):

            posicao[vertices[i]] = i


        # Percorre todas as arestas
        for aresta in self.arestas.values():

            origem = aresta.orig
            destino = aresta.dest

            i = posicao[origem]
            j = posicao[destino]

            matriz[i][j] = 1

            if not self.direcionado:

                matriz[j][i] = 1


        return vertices, matriz


    # ==================================================
    # MOSTRAR MATRIZ DE ADJACENCIA
    # ==================================================

    def mostrar_matriz_adjacencia(self):

        vertices, matriz = self.matriz_adjacencia()

        print("\n" + "=" * 50)
        print("MATRIZ DE ADJACENCIA")
        print("=" * 50)

        if len(vertices) == 0:

            print("Grafo vazio.")

            print("=" * 50)

            return

        # Cabecalho da matriz

        print("      ", end="")

        for vertice in vertices:

            print(f"{vertice:^6}", end="")

        print()

        # Linhas da matriz

        for i in range(len(vertices)):

            print(f"{vertices[i]:^5} ", end="")

            for j in range(len(vertices)):

                print(f"{matriz[i][j]:^6}", end="")

            print()

        print("=" * 50)

    def matriz_incidencia(self):

        vertices = list(self.vertices.keys())
        arestas = list(self.arestas.values())

        quantidade_vertices = len(vertices)
        quantidade_arestas = len(arestas)

        matriz = [
            [0 for _ in range(quantidade_arestas)]
            for _ in range(quantidade_vertices)
        ]

        posicao = {
            id: i
            for i, id in enumerate(vertices)
        }

        for j, aresta in enumerate(arestas):

            i_origem = posicao[aresta.orig]
            i_destino = posicao[aresta.dest]

            if self.direcionado:

                matriz[i_origem][j] = 1
                matriz[i_destino][j] = -1

            else:

                if aresta.orig == aresta.dest:

                    matriz[i_origem][j] = 2

                else:

                    matriz[i_origem][j] = 1
                    matriz[i_destino][j] = 1

        return vertices, arestas, matriz


    def mostrar_matriz_incidencia(self):

        vertices, arestas, matriz = self.matriz_incidencia()

        print("\n" + "=" * 50)
        print("MATRIZ DE INCIDENCIA")
        print("=" * 50)

        if len(vertices) == 0:

            print("Grafo vazio.")

            print("=" * 50)

            return

        print("      ", end="")

        for aresta in arestas:

            print(f"{aresta.id:^6}", end="")

        print()

        for i in range(len(vertices)):

            print(f"{vertices[i]:^5} ", end="")

            for j in range(len(arestas)):

                print(f"{matriz[i][j]:^6}", end="")

            print()

        print("=" * 50)