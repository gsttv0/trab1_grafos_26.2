class Prim:

    def __init__(self, grafo):

        self.grafo = grafo
        self.agm = []
        self.custo = 0


    def executar(self, inicio):

        if self.grafo.direcionado:

            print(
                "Erro: o algoritmo de Prim funciona "
                "em grafos nao direcionados."
            )

            return False


        if inicio not in self.grafo.vertices:

            print(
                f"Erro: o vertice '{inicio}' nao existe."
            )

            return False


        self.agm = []
        self.custo = 0

        visitados = set()

        visitados.add(inicio)


        while len(visitados) < len(self.grafo.vertices):

            menor_aresta = None


            for aresta in self.grafo.arestas.values():

                origem_visitada = aresta.orig in visitados

                destino_visitado = aresta.dest in visitados


                # Origem visitada e destino ainda nao visitado

                if origem_visitada and not destino_visitado:

                    if (
                        menor_aresta is None
                        or aresta.val < menor_aresta.val
                    ):

                        menor_aresta = aresta


                # Destino visitado e origem ainda nao visitada

                elif destino_visitado and not origem_visitada:

                    if (
                        menor_aresta is None
                        or aresta.val < menor_aresta.val
                    ):

                        menor_aresta = aresta


            # Nenhuma aresta encontrada
            # significa que o grafo nao eh conexo

            if menor_aresta is None:

                print("Erro: o grafo nao eh conexo.")

                self.agm = []

                self.custo = 0

                return False


            # Adiciona a menor aresta encontrada na AGM

            self.agm.append(menor_aresta)


            # Soma o peso da aresta

            self.custo += menor_aresta.val


            # Marca os vertices como visitados

            visitados.add(menor_aresta.orig)

            visitados.add(menor_aresta.dest)


        return True


    def mostrar_agm(self):

        print("\n" + "=" * 50)

        print("ARVORE GERADORA MINIMA - PRIM")

        print("=" * 50)


        if not self.agm:

            print("AGM vazia.")

            print("=" * 50)

            return


        for aresta in self.agm:

            print(
                f"{aresta.id}: "
                f"{aresta.orig} -- {aresta.dest} "
                f"| peso = {aresta.val}"
            )


        print("-" * 50)

        print(
            f"Custo total da AGM: {self.custo}"
        )

        print("=" * 50)