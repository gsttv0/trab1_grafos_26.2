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

        self.lista_adjacencia[aresta.orig].remove(aresta) #remove a aresta da lista de adj  

        if not self.direcionado and aresta.orig != aresta.dest: #verifica se nao eh direcionado e nem os verts iguais 
            self.lista_adjacencia[aresta.dest].remove(aresta) 
                                                                #senao, remove a aresta  
        del self.arestas[id]


    def remover_vertice(self, id):

        if id not in self.vertices:
            raise ValueError(f"o vertice '{id}' nao existe.")

        arestas_remover = []

        for aresta in self.arestas.values(): #procura se tem arestas ligadas esse vertice 

            if aresta.orig == id or aresta.dest == id:
                arestas_remover.append(aresta.id)  #adiciona a aresta em uma lista pra remover dps

        for id_aresta in arestas_remover:
            self.remover_aresta(id_aresta) #chama a def pra remover as arestas dessa lista

        del self.vertices[id]
        del self.lista_adjacencia[id] 


    def outro_extremo(self, aresta, id):  

        if aresta.orig == id: #se a origem for igual o  vertice passado, retorna o outro vert da aresta
            return aresta.dest

        return aresta.orig #senao, vai retornar a origem  


    def texto_lista_adjacencia(self): #transforma a lista de adj em um texto formatado pro user

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

        vertices = list(self.vertices) #pega cada vertice e bota numa lista

        posicao = {id: i for i, id in enumerate(vertices)} #cria um dicionario com o vertice e a posicao dele  

        matriz = [[0 for _ in vertices] for _ in vertices] #preenhe a matriz toda com 0  

        for aresta in self.arestas.values():  #vai passar pelas arestas e colocar 1 onde tem a orig e dest 

            i = posicao[aresta.orig]
            j = posicao[aresta.dest]

            matriz[i][j] = 1 #representa de uma lado

            if not self.direcionado:
                matriz[j][i] = 1 #se nao for direcionado, representa do outro lado tbm

        return vertices, matriz


    def matriz_incidencia(self):

        vertices = list(self.vertices) #pega cada vertice e bota numa lista
        arestas = list(self.arestas.values()) #pega cada aresta e bota numa lista

        posicao = {id: i for i, id in enumerate(vertices)} #cria um dicionario com o vertice e a posicao dele

        matriz = [[0 for _ in arestas] for _ in vertices] #preenche a matriz toda com 0

        for j, aresta in enumerate(arestas): #percorre todas as arestas

            i_orig = posicao[aresta.orig]
            i_dest = posicao[aresta.dest]

            if aresta.orig == aresta.dest: #se for laco - coloca 2

                matriz[i_orig][j] = 2

            elif self.direcionado: #se for direcionado - 1 pra orig e -1 pra dest

                matriz[i_orig][j] = 1
                matriz[i_dest][j] = -1

            else:                   #se for nao direcionado - 1 pros dois

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
