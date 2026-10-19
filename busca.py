class Busca:

    def __init__(self, grafo):

        self.grafo = grafo
        self.visitados = []
        self.arvore = [] #arcos que formam a arvore feita na busca
        self.caminho = [] #arcos usadados entre a saida e a chegada
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

            adjacentes = self.grafo.lista_adjacencia[atual] #recebe os arcos do vertice atual

            if indice[atual] == len(adjacentes):
                pilha.pop() # se ja os arcos desse vert, remove ele do topo da pilha
                continue

            arco = adjacentes[indice[atual]] #pega a proxim arco

            indice[atual] += 1

            vizinho = self.grafo.outro_extremo(arco, atual) #verifica qual o outro vertice do arco

            if vizinho in pai: #verifica se ja foi visitado  
                continue

            pai[vizinho] = arco #atribui o arco como pai do vizinho
            indice[vizinho] = 0 #reseta o indice do vizinho

            self.visitados.append(vizinho)
            self.arvore.append(arco)
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

        texto += "Arcos da arvore gerada:\n"

        if not self.arvore:
            texto += "  (nenhuma)\n"

        for arco in self.arvore:
            texto += f"  {arco.id}: {arco.orig} - {arco.dest}\n"

        texto += "\n"

        if not self.encontrou:
            return texto + f"Nao existe caminho de {saida} ate {chegada}.\n"

        custo = sum(arco.val for arco in self.caminho)

        texto += "Caminho encontrado:\n"

        atual = saida

        texto += f"  {atual}"

        for arco in self.caminho:
            atual = self.grafo.outro_extremo(arco, atual)
            texto += f" -[{arco.id}]-> {atual}"

        texto += f"\n\nCusto do caminho: {custo}\n"

        return texto
