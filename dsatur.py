class DSATUR:

    def __init__(self, grafo):

        self.grafo = grafo
        self.cores = {}


    def obter_vizinhos(self, id_vertice):

        vizinhos = []

        for arco in self.grafo.lista_adjacencia[id_vertice]: #percorre os arcos ligados ao vertice

            vizinho = self.grafo.outro_extremo(arco, id_vertice) #pega o arco ligado e bota em vizinho

            if vizinho not in vizinhos: #se não estiver em vizinhos
                vizinhos.append(vizinho) #add

        return vizinhos


    def grau(self, id_vertice):

        return len(self.obter_vizinhos(id_vertice))


    def cores_vizinhos(self, id_vertice):

        cores = set() #guarda as cores sem repetir

        for vizinho in self.obter_vizinhos(id_vertice): #percorre os vizinhos

            if vizinho in self.cores: #se o vizinho ja tiver cor, add a cor dele no set cores
                cores.add(self.cores[vizinho])

        return cores


    def grau_saturacao(self, id_vertice):

        return len(self.cores_vizinhos(id_vertice)) 


    def escolher_vertice(self, nao_coloridos):

        maior_saturacao = -1 #começa -1 pq uma saturação minima é 0
        maior_grau = -1
        escolhido = None

        for id_vertice in nao_coloridos: #passa 1 por 1 de quem ainda não tem cor

            saturacao = self.grau_saturacao(id_vertice)
            grau = self.grau(id_vertice)

            if saturacao > maior_saturacao:

                maior_saturacao = saturacao
                maior_grau = grau
                escolhido = id_vertice

            elif saturacao == maior_saturacao and grau > maior_grau: #se a saturação empatar, verfica se o grau é maior

                maior_grau = grau
                escolhido = id_vertice

        return escolhido #retorna o maior vertice encontrado 


    def escolher_cor(self, id_vertice):

        cores_usadas = self.cores_vizinhos(id_vertice) #descobre a cor dos viznhos

        cor = 1 #começa tentando a cor 1 

        while cor in cores_usadas: #enquanto a cor estiver sendo usada pelos vizinhos, tenta a proxima cor
            cor += 1

        return cor


    def executar(self):

        self.cores = {} #limpa o dicionario de cores

        nao_coloridos = list(self.grafo.vertices.keys()) #pega todos os vertices do grafo

        while len(nao_coloridos) > 0: #enquanto ainda tiver vert sem cor, continua  

            vertice = self.escolher_vertice(nao_coloridos)

            cor = self.escolher_cor(vertice)

            self.cores[vertice] = cor

            nao_coloridos.remove(vertice)

        return self.cores