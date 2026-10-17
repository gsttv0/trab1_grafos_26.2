from mapa_parana import carregar_mapa_parana
from astar import AStar


grafo = carregar_mapa_parana()

astar = AStar(grafo)

origem = "Umuarama"
destino = "Curitiba"

caminho = astar.executar(origem, destino)


print("=" * 60)
print("TESTE A*")
print("=" * 60)

print()
print(f"Origem: {origem}")
print(f"Destino: {destino}")

print()
print("HEURISTICAS H(N)")
print("-" * 60)

for vertice, heuristica in astar.heuristicas.items():
    print(
        f"{vertice}: {heuristica:.2f} km"
    )


print()
print("RESULTADO")
print("-" * 60)

if caminho is None:

    print("Nao foi encontrado um caminho.")

else:

    print(
        "Caminho:",
        " -> ".join(caminho)
    )

    print(
        f"Custo total: {astar.custo:.2f} km"
    )

print()
print("=" * 60)