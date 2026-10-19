from vertice import Vertice
from arco import Arco


class Grafo:

    def __init__(self, direcionado=False):

        self.direcionado = direcionado
        self.vertices = {}
        self.arcos = {}
        self.lista_adjacencia = {}


    def inserir_vertice(self, id, latitude=None, longitude=None): #add latitude e longitude

        if id in self.vertices:
            raise ValueError(f"o vertice '{id}' ja existe.")

        self.vertices[id] = Vertice(id, latitude, longitude)
        self.lista_adjacencia[id] = []


    def inserir_arco(self, id, orig, dest, val):

        if orig not in self.vertices:
            raise ValueError(f"o vertice '{orig}' nao existe.")

        if dest not in self.vertices:
            raise ValueError(f"o vertice '{dest}' nao existe.")

        if id in self.arcos:
            raise ValueError(f"o arco '{id}' ja existe.")

        arco = Arco(id, orig, dest, val)

        self.arcos[id] = arco

        self.lista_adjacencia[orig].append(arco)

        if not self.direcionado and orig != dest:
            self.lista_adjacencia[dest].append(arco)


    def remover_arco(self, id):

        if id not in self.arcos:
            raise ValueError(f"o arco '{id}' nao existe.")

        arco = self.arcos[id]

        self.lista_adjacencia[arco.orig].remove(arco) #remove o arco da lista de adj

        if not self.direcionado and arco.orig != arco.dest: #verifica se nao eh direcionado e nem os verts iguais
            self.lista_adjacencia[arco.dest].remove(arco)
                                                                #senao, remove o arco
        del self.arcos[id]


    def remover_vertice(self, id):

        if id not in self.vertices:
            raise ValueError(f"o vertice '{id}' nao existe.")

        arcos_remover = []

        for arco in self.arcos.values(): #procura se tem arcos ligados esse vertice

            if arco.orig == id or arco.dest == id:
                arcos_remover.append(arco.id)  #adiciona o arco em uma lista pra remover dps

        for id_arco in arcos_remover:
            self.remover_arco(id_arco) #chama a def pra remover os arcos dessa lista

        del self.vertices[id]
        del self.lista_adjacencia[id] 


    def outro_extremo(self, arco, id):

        if arco.orig == id: #se a origem for igual o vertice passado, retorna o outro vert do arco
            return arco.dest

        return arco.orig #senao, vai retornar a origem


    def texto_lista_adjacencia(self): #transforma a lista de adj em um texto formatado pro user

        if len(self.vertices) == 0:
            return "LISTA DE ADJACENCIA\n\nGrafo vazio."

        seta = "->" if self.direcionado else "--" 

        texto = "LISTA DE ADJACENCIA\n\n"

        for id in self.vertices:

            texto += f"{id} :"

            for arco in self.lista_adjacencia[id]:

                vizinho = self.outro_extremo(arco, id)

                texto += f"  {seta} {vizinho} [{arco.id}, peso={arco.val}]"

            texto += "\n"

        return texto


    def matriz_adjacencia(self):

        vertices = list(self.vertices) #pega cada vertice e bota numa lista

        posicao = {id: i for i, id in enumerate(vertices)} #cria um dicionario com o vertice e a posicao dele  

        matriz = [[0 for _ in vertices] for _ in vertices] #preenhe a matriz toda com 0  

        for arco in self.arcos.values():  #vai passar pelos arcos e colocar 1 onde tem a orig e dest

            i = posicao[arco.orig]
            j = posicao[arco.dest]

            matriz[i][j] = 1 #representa de uma lado

            if not self.direcionado:
                matriz[j][i] = 1 #se nao for direcionado, representa do outro lado tbm

        return vertices, matriz


    def matriz_incidencia(self):

        vertices = list(self.vertices) #pega cada vertice e bota numa lista
        arcos = list(self.arcos.values()) #pega cado arco e bota numa lista

        posicao = {id: i for i, id in enumerate(vertices)} #cria um dicionario com o vertice e a posicao dele

        matriz = [[0 for _ in arcos] for _ in vertices] #preenche a matriz toda com 0

        for j, arco in enumerate(arcos): #percorre todas os arcos

            i_orig = posicao[arco.orig]
            i_dest = posicao[arco.dest]

            if arco.orig == arco.dest: #se for laco - coloca 2

                matriz[i_orig][j] = 2

            elif self.direcionado: #se for direcionado - 1 pra orig e -1 pra dest

                matriz[i_orig][j] = 1
                matriz[i_dest][j] = -1

            else:                   #se for nao direcionado - 1 pros dois

                matriz[i_orig][j] = 1
                matriz[i_dest][j] = 1

        return vertices, [a.id for a in arcos], matriz


    def formatar_matriz(self, titulo, linhas, colunas, matriz):

        if len(linhas) == 0:
            return f"{titulo}\n\nGrafo vazio."

        if len(colunas) == 0:
            return f"{titulo}\n\nO grafo nao possui arcos."

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

        vertices, arcos, matriz = self.matriz_incidencia()

        return self.formatar_matriz(
            "MATRIZ DE INCIDENCIA", vertices, arcos, matriz
        )