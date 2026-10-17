class DSATUR:

    def __init__(self, grafo):

        self.grafo = grafo
        self.cores = {}


    def obter_vizinhos(self, id_vertice):

        vizinhos = []

        for aresta in self.grafo.lista_adjacencia[id_vertice]:

            vizinho = self.grafo.outro_extremo(aresta, id_vertice)

            if vizinho not in vizinhos:
                vizinhos.append(vizinho)

        return vizinhos


    def grau(self, id_vertice):

        return len(self.obter_vizinhos(id_vertice))


    def cores_vizinhos(self, id_vertice):

        cores = set()

        for vizinho in self.obter_vizinhos(id_vertice):

            if vizinho in self.cores:
                cores.add(self.cores[vizinho])

        return cores


    def grau_saturacao(self, id_vertice):

        return len(self.cores_vizinhos(id_vertice))


    def escolher_vertice(self, nao_coloridos):

        maior_saturacao = -1
        maior_grau = -1
        escolhido = None

        for id_vertice in nao_coloridos:

            saturacao = self.grau_saturacao(id_vertice)
            grau = self.grau(id_vertice)

            if saturacao > maior_saturacao:

                maior_saturacao = saturacao
                maior_grau = grau
                escolhido = id_vertice

            elif saturacao == maior_saturacao and grau > maior_grau:

                maior_grau = grau
                escolhido = id_vertice

        return escolhido


    def escolher_cor(self, id_vertice):

        cores_usadas = self.cores_vizinhos(id_vertice)

        cor = 1

        while cor in cores_usadas:
            cor += 1

        return cor


    def executar(self):

        self.cores = {}

        nao_coloridos = list(self.grafo.vertices.keys())

        while len(nao_coloridos) > 0:

            vertice = self.escolher_vertice(nao_coloridos)

            cor = self.escolher_cor(vertice)

            self.cores[vertice] = cor

            nao_coloridos.remove(vertice)

        return self.cores