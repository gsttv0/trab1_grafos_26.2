from grafo import Grafo


def carregar_grafo_arquivo(caminho_arquivo, direcionado=False):

    grafo = Grafo(direcionado=direcionado)

    secao = None

    with open( #abre o arquivo pra leitura
        caminho_arquivo,
        "r",
        encoding="utf-8"
    ) as arquivo:

        for numero_linha, linha in enumerate( #percorre cada linha dele
            arquivo,
            start=1
        ):

            linha = linha.strip()

            #ignora linhas vazias
            if not linha:
                continue

            #ignora comentarios
            if linha.startswith("#"):
                continue


            if linha.upper() == "VERTICES": #identifica o inicio da secao de vertices

                secao = "VERTICES"
                continue

            if linha.upper() in ("ARCOS", "ARESTAS"): #identifica a secao de arcos ou arestas

                secao = "ARCOS"
                continue



            if secao == "VERTICES": #le o vertice e identifica se tem latitude e longitude

                dados = [
                    dado.strip()
                    for dado in linha.split(";")
                ]

                if len(dados) == 1: #se tamanho for 1, pega so o vertice  

                    id_vertice = dados[0]

                    grafo.inserir_vertice(
                        id_vertice
                    )

                elif len(dados) == 3: #se tamanho for 3, pega o vertice, latitude e longitude

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




            elif secao == "ARCOS": #le os arcos/arestas 

                dados = [
                    dado.strip()
                    for dado in linha.split(";")
                ]

                if len(dados) != 4:

                    raise ValueError(
                        f"Linha {numero_linha}: "
                        "formato de arco invalido."
                    )

                id_arco = dados[0]
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

                grafo.inserir_arco(
                    id_arco,
                    origem,
                    destino,
                    peso
                )


            else:

                raise ValueError(
                    f"Linha {numero_linha}: "
                    "defina VERTICES ou ARCOS "
                    "antes dos dados."
                )


    if not grafo.vertices:

        raise ValueError(
            "O arquivo nao possui vertices."
        )


    return grafo