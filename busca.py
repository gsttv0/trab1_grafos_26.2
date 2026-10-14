class Busca:

    def __init__(self, grafo):

        self.grafo = grafo
        self.visitados = []
        self.arvore = [] #arestas que formam a arvore feita na busca
        self.caminho = [] #aresstas usadados entre a saida e a chegada
        self.encontrou = False #se encontrou o vertice de chegada ou nao


    def executar(self, saida, chegada):

        if saida not in self.grafo.vertices:
            raise ValueError(f"o vertice '{saida}' nao existe.")

        if chegada not in self.grafo.vertices:
            raise ValueError(f"o vertice '{chegada}' nao existe.")

        self.visitados = [saida] #saida ja entra como visitado 
        self.arvore = []
        self.caminho = []
        self.encontrou = saida == chegada #so verfica se tem possibilidade das duas serem iguais 

        pai = {saida: None} #saida tem pai none
        indice = {saida: 0} #vertice visitado e indice
        pilha = [saida] #vai empilhando os vertices  

        while pilha and not self.encontrou: #continua procurando se ainda tiver vert na pilha, ou se não encontrou  

            atual = pilha[-1] #pega o ultomo da pilha 

            adjacentes = self.grafo.lista_adjacencia[atual] #recebe as aresta do vertice atual  

            if indice[atual] == len(adjacentes):
                pilha.pop() # se ja as aresta desse vert, remove ele do topo da pilha  
                continue

            aresta = adjacentes[indice[atual]] #pega a proxim aresta

            indice[atual] += 1

            vizinho = self.grafo.outro_extremo(aresta, atual) #verifica qual o outro vertice da aresta 

            if vizinho in pai: #verifica se ja foi visitado  
                continue

            pai[vizinho] = aresta #atribui a aresta como pai do vizinho
            indice[vizinho] = 0 #reseta o indice do vizinho

            self.visitados.append(vizinho)
            self.arvore.append(aresta)
            pilha.append(vizinho)

            if vizinho == chegada:
                self.encontrou = True

        if self.encontrou:

            atual = chegada

            while pai[atual] is not None: #enquanto o vert tiver um pai, vai fazendo  
                self.caminho.append(pai[atual])
                atual = self.grafo.outro_extremo(pai[atual], atual)

            self.caminho.reverse() #apenas reverte o caminho feito


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
