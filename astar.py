import math


class AStar:

    def __init__(self, grafo):

        self.grafo = grafo

        self.caminho = []
        self.custo = 0
        self.heuristicas = {}


    # ==========================================
    # HAVERSINE
    # ==========================================

    def haversine(self, id_origem, id_destino):

        origem = self.grafo.vertices[id_origem]
        destino = self.grafo.vertices[id_destino]

        if origem.latitude is None or origem.longitude is None:
            raise ValueError(
                f"o vertice '{id_origem}' nao possui latitude e longitude."
            )

        if destino.latitude is None or destino.longitude is None:
            raise ValueError(
                f"o vertice '{id_destino}' nao possui latitude e longitude."
            )

        raio_terra = 6371.0

        lat1 = math.radians(origem.latitude)
        lon1 = math.radians(origem.longitude)

        lat2 = math.radians(destino.latitude)
        lon2 = math.radians(destino.longitude)

        diferenca_lat = lat2 - lat1
        diferenca_lon = lon2 - lon1

        a = (
            math.sin(diferenca_lat / 2) ** 2
            +
            math.cos(lat1)
            * math.cos(lat2)
            * math.sin(diferenca_lon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        distancia = raio_terra * c

        return distancia


    # ==========================================
    # CALCULAR HEURISTICAS
    # ==========================================

    def calcular_heuristicas(self, destino):

        self.heuristicas = {}

        for id_vertice in self.grafo.vertices:

            distancia = self.haversine(
                id_vertice,
                destino
            )

            self.heuristicas[id_vertice] = distancia

        return self.heuristicas


    # ==========================================
    # OBTER VIZINHOS
    # ==========================================

    def obter_vizinhos(self, id_vertice):

        vizinhos = []

        for arco in self.grafo.lista_adjacencia[id_vertice]:

            if self.grafo.direcionado:

                if arco.orig != id_vertice:
                    continue

                vizinho = arco.dest

            else:

                vizinho = self.grafo.outro_extremo(
                    arco,
                    id_vertice
                )

            vizinhos.append(
                (vizinho, arco.val)
            )

        return vizinhos


    # ==========================================
    # RECONSTRUIR CAMINHO
    # ==========================================

    def reconstruir_caminho(self, anteriores, destino):

        caminho = []

        atual = destino

        while atual is not None:

            caminho.append(atual)

            atual = anteriores[atual]

        caminho.reverse()

        return caminho


    # ==========================================
    # EXECUTAR A*
    # ==========================================

    def executar(self, origem, destino):

        if origem not in self.grafo.vertices:
            raise ValueError(
                f"o vertice '{origem}' nao existe."
            )

        if destino not in self.grafo.vertices:
            raise ValueError(
                f"o vertice '{destino}' nao existe."
            )

        self.caminho = []
        self.custo = 0

        self.calcular_heuristicas(destino)

        abertos = [origem]

        fechados = []

        anteriores = {}

        g = {}

        f = {}


        for id_vertice in self.grafo.vertices:

            anteriores[id_vertice] = None

            g[id_vertice] = float("inf")

            f[id_vertice] = float("inf")


        g[origem] = 0

        f[origem] = self.heuristicas[origem]


        while len(abertos) > 0:

            atual = min(
                abertos,
                key=lambda vertice: f[vertice]
            )


            if atual == destino:

                self.caminho = self.reconstruir_caminho(
                    anteriores,
                    destino
                )

                self.custo = g[destino]

                return self.caminho


            abertos.remove(atual)

            fechados.append(atual)


            for vizinho, peso in self.obter_vizinhos(atual):

                if vizinho in fechados:
                    continue


                novo_g = g[atual] + peso


                if novo_g < g[vizinho]:

                    anteriores[vizinho] = atual

                    g[vizinho] = novo_g

                    f[vizinho] = (
                        novo_g
                        +
                        self.heuristicas[vizinho]
                    )


                    if vizinho not in abertos:
                        abertos.append(vizinho)


        return None