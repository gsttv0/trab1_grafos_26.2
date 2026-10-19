from grafo import Grafo


def carregar_mapa_parana():

    grafo = Grafo(direcionado=False)


    # ==========================================
    # VERTICES / CIDADES
    # ==========================================

    grafo.inserir_vertice(
        "Umuarama",
        -23.8061,
        -53.3207
    )

    grafo.inserir_vertice(
        "Maringa",
        -23.42,
        -51.94
    )

    grafo.inserir_vertice(
        "Londrina",
        -23.34,
        -51.15
    )

    grafo.inserir_vertice(
        "Toledo",
        -24.72,
        -53.74
    )

    grafo.inserir_vertice(
        "Cascavel",
        -24.96,
        -53.48
    )

    grafo.inserir_vertice(
        "Foz do Iguacu",
        -25.55,
        -54.59
    )

    grafo.inserir_vertice(
        "Francisco Beltrao",
        -26.08,
        -53.06
    )

    grafo.inserir_vertice(
        "Guarapuava",
        -25.39,
        -51.47
    )

    grafo.inserir_vertice(
        "Sao Mateus do Sul",
        -25.87,
        -50.39
    )

    grafo.inserir_vertice(
        "Ponta Grossa",
        -25.10,
        -50.17
    )

    grafo.inserir_vertice(
        "Curitiba",
        -25.41,
        -49.27
    )


    # ==========================================
    # ARCOS
    # ==========================================

    grafo.inserir_arco(
        "E1",
        "Umuarama",
        "Maringa",
        190
    )

    grafo.inserir_arco(
        "E2",
        "Umuarama",
        "Toledo",
        126
    )

    grafo.inserir_arco(
        "E3",
        "Toledo",
        "Cascavel",
        50
    )

    grafo.inserir_arco(
        "E4",
        "Cascavel",
        "Foz do Iguacu",
        143
    )

    grafo.inserir_arco(
        "E5",
        "Cascavel",
        "Francisco Beltrao",
        186
    )

    grafo.inserir_arco(
        "E6",
        "Cascavel",
        "Guarapuava",
        250
    )

    grafo.inserir_arco(
        "E7",
        "Maringa",
        "Londrina",
        114
    )

    grafo.inserir_arco(
        "E8",
        "Maringa",
        "Ponta Grossa",
        314
    )

    grafo.inserir_arco(
        "E9",
        "Londrina",
        "Ponta Grossa",
        273
    )

    grafo.inserir_arco(
        "E10",
        "Guarapuava",
        "Ponta Grossa",
        165
    )

    grafo.inserir_arco(
        "E11",
        "Francisco Beltrao",
        "Sao Mateus do Sul",
        354
    )

    grafo.inserir_arco(
        "E12",
        "Sao Mateus do Sul",
        "Ponta Grossa",
        114
    )

    grafo.inserir_arco(
        "E13",
        "Sao Mateus do Sul",
        "Curitiba",
        157
    )

    grafo.inserir_arco(
        "E14",
        "Ponta Grossa",
        "Curitiba",
        90
    )


    return grafo