from grafo import Grafo
from prim import Prim


# ==================================================
# TESTE DO GRAFO NAO DIRECIONADO
# ==================================================

print("=" * 50)
print("TESTE DO GRAFO NAO DIRECIONADO")
print("=" * 50)

grafo = Grafo(direcionado=False)


# ==========================================
# INSERINDO VERTICES
# ==========================================

print("\nInserindo vertices...")

grafo.inserir_vertice("A")
grafo.inserir_vertice("B")
grafo.inserir_vertice("C")


print("\nVertices:")
print(grafo.vertices)


# ==========================================
# INSERINDO ARESTAS
# ==========================================

print("\nInserindo arestas...")

grafo.inserir_aresta("E1", "A", "B", 10)
grafo.inserir_aresta("E2", "A", "C", 20)


print("\nArestas:")
print(grafo.arestas)


# ==========================================
# LISTA DE ADJACENCIA
# ==========================================

print("\nLista de adjacencia:")

for id in grafo.vertices:

    print(f"{id} -> ", end="")

    for aresta in grafo.lista_adjacencia[id]:

        print(
            f"{aresta.id} "
            f"({aresta.orig}-{aresta.dest}, "
            f"peso={aresta.val}) | ",
            end=""
        )

    print()


# ==========================================
# MATRIZ DE ADJACENCIA
# ==========================================

print("\nMatriz de adjacencia:")

grafo.mostrar_matriz_adjacencia()


# ==========================================
# MATRIZ DE INCIDENCIA
# ==========================================

print("\nMatriz de incidencia:")

grafo.mostrar_matriz_incidencia()


# ==================================================
# TESTE DO GRAFO DIRECIONADO
# ==================================================

print("\n")
print("=" * 50)
print("TESTE DO GRAFO DIRECIONADO")
print("=" * 50)

grafo_direcionado = Grafo(direcionado=True)


# ==========================================
# INSERINDO VERTICES
# ==========================================

print("\nInserindo vertices...")

grafo_direcionado.inserir_vertice("A")
grafo_direcionado.inserir_vertice("B")
grafo_direcionado.inserir_vertice("C")


# ==========================================
# INSERINDO ARCOS
# ==========================================

print("\nInserindo arcos...")

grafo_direcionado.inserir_aresta(
    "E1",
    "A",
    "B",
    10
)

grafo_direcionado.inserir_aresta(
    "E2",
    "A",
    "C",
    20
)


# ==========================================
# LISTA DE ADJACENCIA DIRECIONADA
# ==========================================

print("\nLista de adjacencia do grafo direcionado:")

for id in grafo_direcionado.vertices:

    print(f"{id} -> ", end="")

    for aresta in grafo_direcionado.lista_adjacencia[id]:

        print(
            f"{aresta.id} "
            f"({aresta.orig}->{aresta.dest}, "
            f"peso={aresta.val}) | ",
            end=""
        )

    print()


# ==========================================
# MATRIZ DE ADJACENCIA DIRECIONADA
# ==========================================

print("\nMatriz de adjacencia do grafo direcionado:")

grafo_direcionado.mostrar_matriz_adjacencia()


# ==========================================
# MATRIZ DE INCIDENCIA DIRECIONADA
# ==========================================

print("\nMatriz de incidencia do grafo direcionado:")

grafo_direcionado.mostrar_matriz_incidencia()


# ==================================================
# TESTE DE REMOCAO
# ==================================================

print("\n")
print("=" * 50)
print("TESTE DE REMOCAO")
print("=" * 50)


print("\nAntes da remocao:")


print("\nVertices:")
print(grafo.vertices)


print("\nArestas:")
print(grafo.arestas)


print("\nLista de adjacencia:")

for id in grafo.vertices:

    print(f"{id} -> ", end="")

    for aresta in grafo.lista_adjacencia[id]:

        print(
            f"{aresta.id} "
            f"({aresta.orig}-{aresta.dest}, "
            f"peso={aresta.val}) | ",
            end=""
        )

    print()


# ==========================================
# REMOVENDO VERTICE
# ==========================================

print("\nRemovendo o vertice A...")

grafo.remover_vertice("A")


# ==========================================
# RESULTADO APOS REMOCAO
# ==========================================

print("\nDepois da remocao:")


print("\nVertices:")
print(grafo.vertices)


print("\nArestas:")
print(grafo.arestas)


print("\nLista de adjacencia:")

for id in grafo.vertices:

    print(f"{id} -> ", end="")

    for aresta in grafo.lista_adjacencia[id]:

        print(
            f"{aresta.id} "
            f"({aresta.orig}-{aresta.dest}, "
            f"peso={aresta.val}) | ",
            end=""
        )

    print()


# ==================================================
# TESTE DO ALGORITMO DE PRIM
# ==================================================

print("\n")
print("=" * 50)
print("TESTE DO ALGORITMO DE PRIM")
print("=" * 50)


grafo_prim = Grafo(direcionado=False)


# ==========================================
# INSERINDO VERTICES
# ==========================================

print("\nInserindo vertices para o Prim...")

grafo_prim.inserir_vertice("A")
grafo_prim.inserir_vertice("B")
grafo_prim.inserir_vertice("C")
grafo_prim.inserir_vertice("D")


# ==========================================
# INSERINDO ARESTAS
# ==========================================

print("\nInserindo arestas para o Prim...")

grafo_prim.inserir_aresta(
    "E1",
    "A",
    "B",
    4
)

grafo_prim.inserir_aresta(
    "E2",
    "A",
    "C",
    2
)

grafo_prim.inserir_aresta(
    "E3",
    "B",
    "C",
    1
)

grafo_prim.inserir_aresta(
    "E4",
    "B",
    "D",
    5
)

grafo_prim.inserir_aresta(
    "E5",
    "C",
    "D",
    8
)


# ==========================================
# MOSTRANDO O GRAFO
# ==========================================

print("\nLista de adjacencia do grafo utilizado no Prim:")

for id in grafo_prim.vertices:

    print(f"{id} -> ", end="")

    for aresta in grafo_prim.lista_adjacencia[id]:

        if aresta.orig == id:
            vizinho = aresta.dest
        else:
            vizinho = aresta.orig

        print(
            f"{vizinho} "
            f"[{aresta.id}, peso={aresta.val}] | ",
            end=""
        )

    print()


# ==========================================
# EXECUTANDO PRIM
# ==========================================

print("\nExecutando Prim a partir do vertice A...")

prim = Prim(grafo_prim)

resultado = prim.executar("A")


# ==========================================
# MOSTRANDO AGM
# ==========================================

if resultado:

    prim.mostrar_agm()


# ==================================================
# FINAL
# ==================================================

print("\nPrograma finalizado.")