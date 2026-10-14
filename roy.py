class Roy:

    def __init__(self, grafo):

        self.grafo = grafo
        self.componentes = [] #guarda o que foi encontrado  


    def alcancar(self, inicio, vizinhos):

        marcados = {inicio}
        pilha = [inicio] #

        while pilha: 

            atual = pilha.pop()

            for vizinho in vizinhos[atual]: #pro vertice atual, pega todos os vizinhos

                if vizinho not in marcados: #verifica se ja foi visitado 
                    marcados.add(vizinho)
                    pilha.append(vizinho) #coloca o novo vertice pra ser explorado tbm

        return marcados


    def executar(self):

        if len(self.grafo.vertices) == 0:
            raise ValueError("o grafo esta vazio.")

        self.componentes = []

        sucessores = {id: [] for id in self.grafo.vertices} #cria um dicionario pra cada vertice ter sucessor
        antecessores = {id: [] for id in self.grafo.vertices} #criar um dicionario pra cada vertice ter antecessor

        for id in self.grafo.vertices:

            for aresta in self.grafo.lista_adjacencia[id]: #pra cada vert, pega sua aresta

                vizinho = self.grafo.outro_extremo(aresta, id)

                sucessores[id].append(vizinho) #add vizinho como sucessor do vertice atual
                antecessores[vizinho].append(id) #add o vertice atual como antecessor do vizinho

        atribuidos = set()

        for id in self.grafo.vertices: #percorre o verticew dnv

            if id in atribuidos: #mas pula se ja foi atribuido a algum componente
                continue

            descendentes = self.alcancar(id, sucessores) #a partir desse vertice, quais consigo alcancar 
            ascendentes = self.alcancar(id, antecessores) #e quais conseguem chegar nesse vertice

            componente = []

            for outro in self.grafo.vertices:

                if outro in descendentes and outro in ascendentes: #verifica se vertice consegue sair e voltar nele 
                    componente.append(outro)

            atribuidos.update(componente)

            self.componentes.append(componente)


    def texto(self):

        if self.grafo.direcionado:
            nome = "FORTEMENTE CONEXAS"
        else:
            nome = "CONEXAS"

        texto = f"ALGORITMO DE ROY - COMPONENTES {nome}\n\n"

        texto += f"Quantidade de componentes: {len(self.componentes)}\n\n"

        for i, componente in enumerate(self.componentes, start=1):
            texto += f"C{i} = {{ " + ", ".join(componente) + " }\n"

        return texto
