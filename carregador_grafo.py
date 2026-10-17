from grafo import Grafo


def carregar_grafo_arquivo(caminho_arquivo, direcionado=False):

    grafo = Grafo(direcionado=direcionado)

    secao = None

    with open(
        caminho_arquivo,
        "r",
        encoding="utf-8"
    ) as arquivo:

        for numero_linha, linha in enumerate(
            arquivo,
            start=1
        ):

            linha = linha.strip()

            # Ignora linhas vazias
            if not linha:
                continue

            # Ignora comentarios
            if linha.startswith("#"):
                continue

            # ==========================================
            # SECOES
            # ==========================================

            if linha.upper() == "VERTICES":

                secao = "VERTICES"
                continue

            if linha.upper() == "ARESTAS":

                secao = "ARESTAS"
                continue


            # ==========================================
            # VERTICES
            # ==========================================

            if secao == "VERTICES":

                dados = [
                    dado.strip()
                    for dado in linha.split(";")
                ]

                if len(dados) == 1:

                    id_vertice = dados[0]

                    grafo.inserir_vertice(
                        id_vertice
                    )

                elif len(dados) == 3:

                    id_vertice = dados[0]

                    try:

                        latitude = float(
                            dados[1]
                        )

                        longitude = float(
                            dados[2]
                        )

                    except ValueError:

                        raise ValueError(
                            f"Linha {numero_linha}: "
                            "latitude ou longitude invalida."
                        )

                    grafo.inserir_vertice(
                        id_vertice,
                        latitude,
                        longitude
                    )

                else:

                    raise ValueError(
                        f"Linha {numero_linha}: "
                        "formato de vertice invalido."
                    )


            # ==========================================
            # ARESTAS
            # ==========================================

            elif secao == "ARESTAS":

                dados = [
                    dado.strip()
                    for dado in linha.split(";")
                ]

                if len(dados) != 4:

                    raise ValueError(
                        f"Linha {numero_linha}: "
                        "formato de aresta invalido."
                    )

                id_aresta = dados[0]
                origem = dados[1]
                destino = dados[2]

                try:

                    peso = float(
                        dados[3]
                    )

                except ValueError:

                    raise ValueError(
                        f"Linha {numero_linha}: "
                        "peso invalido."
                    )

                grafo.inserir_aresta(
                    id_aresta,
                    origem,
                    destino,
                    peso
                )


            else:

                raise ValueError(
                    f"Linha {numero_linha}: "
                    "defina VERTICES ou ARESTAS "
                    "antes dos dados."
                )


    if not grafo.vertices:

        raise ValueError(
            "O arquivo nao possui vertices."
        )


    return grafo