import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import math

from grafo import Grafo
from prim import Prim
from dsatur import DSATUR
from astar import AStar
from mapa_parana import carregar_mapa_parana
from carregador_grafo import carregar_grafo_arquivo


class Interface:

    def __init__(self):

        self.grafo = Grafo(direcionado=False)

        self.janela = tk.Tk()

        self.janela.title("Sistema de Grafos")
        self.janela.geometry("700x700")
        self.janela.resizable(False, False)

        self.criar_interface()


    def criar_interface(self):

      
        titulo = tk.Label(
            self.janela,
            text="SISTEMA DE GRAFOS",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            self.janela,
            text="Trabalho de Teoria dos Grafos",
            font=("Arial", 11)
        )

        subtitulo.pack()


        moldura = tk.Frame(
            self.janela,
            bd=2,
            relief="groove"
        )

        moldura.pack(
            padx=40,
            pady=25,
            fill="both",
            expand=True
        )



        self.criar_botao(
            moldura,
            "1 - Inserir vertice",
            self.inserir_vertice
        )

        self.criar_botao(
            moldura,
            "2 - Inserir arco",
            self.inserir_arco
        )

        self.criar_botao(
            moldura,
            "3 - Remover vertice",
            self.remover_vertice
        )

        self.criar_botao(
            moldura,
            "4 - Remover arco",
            self.remover_arco
        )

        self.criar_botao(
            moldura,
            "5 - Mostrar matriz de adjacencia",
            self.mostrar_matriz_adjacencia
        )

        self.criar_botao(
            moldura,
            "6 - Mostrar matriz de incidencia",
            self.mostrar_matriz_incidencia
        )

        self.criar_botao(
            moldura,
            "7 - Executar Prim",
            self.executar_prim
        )

        self.criar_botao(
            moldura,
            "8 - Mostrar informacoes do grafo",
            self.mostrar_grafo
        )

        self.criar_botao(
            moldura,
            "9 - Executar DSATUR",
            self.executar_dsatur
        )

        self.criar_botao(
            moldura,
            "10 - Carregar grafo de arquivo",
            self.carregar_grafo
        )

        self.criar_botao(
            moldura,
            "11 - Carregar mapa do Parana",
            self.carregar_parana
        )

        self.criar_botao(
            moldura,
            "12 - Executar A*",
            self.executar_astar
        )

        self.criar_botao(
            moldura,
            "13 - Sair",
            self.sair
        )


    def criar_botao(self, moldura, texto, comando):

        botao = tk.Button(
            moldura,
            text=texto,
            command=comando,
            width=40,
            height=1
        )

        botao.pack(pady=4)



    def inserir_vertice(self):

        id_vertice = simpledialog.askstring(
            "Inserir vertice",
            "Digite o ID do vertice:"
        )

        if not id_vertice:
            return


        informar_coordenadas = messagebox.askyesno(
            "Coordenadas geograficas",
            "Deseja informar latitude e longitude?\n\n"
            "As coordenadas sao necessarias caso "
            "o vertice seja utilizado no algoritmo A*."
        )


        latitude = None
        longitude = None


        if informar_coordenadas:

            latitude = simpledialog.askfloat(
                "Latitude",
                "Digite a latitude do vertice:"
            )

            if latitude is None:
                return


            longitude = simpledialog.askfloat(
                "Longitude",
                "Digite a longitude do vertice:"
            )

            if longitude is None:
                return


            if latitude < -90 or latitude > 90:

                messagebox.showerror(
                    "Erro",
                    "A latitude deve estar entre -90 e 90."
                )

                return


            if longitude < -180 or longitude > 180:

                messagebox.showerror(
                    "Erro",
                    "A longitude deve estar entre -180 e 180."
                )

                return


        try:

            self.grafo.inserir_vertice(
                id_vertice,
                latitude,
                longitude
            )


            if informar_coordenadas:

                mensagem = (
                    f"Vertice '{id_vertice}' inserido.\n\n"
                    f"Latitude: {latitude}\n"
                    f"Longitude: {longitude}"
                )

            else:

                mensagem = (
                    f"Vertice '{id_vertice}' inserido."
                )


            messagebox.showinfo(
                "Sucesso",
                mensagem
            )


        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )


 
    def inserir_arco(self):

        id_arco = simpledialog.askstring(
            "Inserir arco",
            "Digite o ID do arco:"
        )

        if not id_arco:
            return


        origem = simpledialog.askstring(
            "Inserir arco",
            "Digite o vertice de origem:"
        )

        if not origem:
            return


        destino = simpledialog.askstring(
            "Inserir arco",
            "Digite o vertice de destino:"
        )

        if not destino:
            return


        peso = simpledialog.askfloat(
            "Inserir arco",
            "Digite o peso:"
        )

        if peso is None:
            return


        try:

            self.grafo.inserir_arco(
                id_arco,
                origem,
                destino,
                peso
            )

            messagebox.showinfo(
                "Sucesso",
                f"Arco '{id_arco}' inserido."
            )

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )



    def remover_vertice(self):

        id_vertice = simpledialog.askstring(
            "Remover vertice",
            "Digite o ID do vertice:"
        )

        if not id_vertice:
            return


        try:

            self.grafo.remover_vertice(
                id_vertice
            )

            messagebox.showinfo(
                "Sucesso",
                f"Vertice '{id_vertice}' removido."
            )

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )



    def remover_arco(self):

        id_arco = simpledialog.askstring(
            "Remover arco",
            "Digite o ID do arco:"
        )

        if not id_arco:
            return


        try:

            self.grafo.remover_arco(
                id_arco
            )

            messagebox.showinfo(
                "Sucesso",
                f"Arco '{id_arco}' removido."
            )

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )


    def mostrar_matriz_adjacencia(self):

        texto = self.grafo.texto_matriz_adjacencia()

        messagebox.showinfo(
            "Matriz de adjacencia",
            texto
        )


    def mostrar_matriz_incidencia(self):

        texto = self.grafo.texto_matriz_incidencia()

        messagebox.showinfo(
            "Matriz de incidencia",
            texto
        )


    def executar_prim(self):

        if self.grafo.direcionado:

            messagebox.showerror(
                "Erro",
                "O algoritmo de Prim funciona "
                "em grafos nao direcionados."
            )

            return


        if not self.grafo.vertices:

            messagebox.showerror(
                "Erro",
                "O grafo nao possui vertices."
            )

            return


        inicio = simpledialog.askstring(
            "Algoritmo de Prim",
            "Digite o vertice inicial:"
        )

        if not inicio:
            return


        prim = Prim(
            self.grafo
        )


        try:

            resultado = prim.executar(
                inicio
            )

        except ValueError as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

            return


        if resultado:

            texto = "ARVORE GERADORA MINIMA\n\n"


            for arco in prim.agm:

                texto += (
                    f"{arco.id}: "
                    f"{arco.orig} -- "
                    f"{arco.dest} "
                    f"| peso = {arco.val}\n"
                )


            texto += (
                f"\nCusto total da AGM: "
                f"{prim.custo}"
            )


            messagebox.showinfo(
                "Resultado do Prim",
                texto
            )


        else:

            messagebox.showerror(
                "Erro",
                "Nao foi possivel gerar a AGM."
            )


    def mostrar_grafo(self):

        texto = "INFORMACOES DO GRAFO\n\n"


        if self.grafo.direcionado:

            texto += "Tipo: Direcionado\n\n"

        else:

            texto += "Tipo: Nao direcionado\n\n"


        texto += "Vertices:\n"


        if self.grafo.vertices:

            for id_vertice, vertice in self.grafo.vertices.items():

                texto += f"- {id_vertice}"

                if (
                    vertice.latitude is not None
                    and vertice.longitude is not None
                ):

                    texto += (
                        f" | lat={vertice.latitude}, "
                        f"lon={vertice.longitude}"
                    )

                texto += "\n"

        else:

            texto += "Nenhum vertice.\n"


        texto += "\nArcos:\n"


        if self.grafo.arcos:

            for arco in self.grafo.arcos.values():

                if self.grafo.direcionado:

                    texto += (
                        f"- {arco.id}: "
                        f"{arco.orig} -> "
                        f"{arco.dest} "
                        f"(peso={arco.val})\n"
                    )

                else:

                    texto += (
                        f"- {arco.id}: "
                        f"{arco.orig} -- "
                        f"{arco.dest} "
                        f"(peso={arco.val})\n"
                    )

        else:

            texto += "Nenhum arco.\n"


        messagebox.showinfo(
            "Informacoes do grafo",
            texto
        )


    # DSATUR
    def executar_dsatur(self):

        if not self.grafo.vertices:

            messagebox.showerror(
                "Erro",
                "O grafo nao possui vertices."
            )

            return


        dsatur = DSATUR(
            self.grafo
        )

        cores = dsatur.executar()

        self.mostrar_resultado_dsatur(
            cores
        )

    # RESULTADO GRAFICO DO DSATUR
    def mostrar_resultado_dsatur(
        self,
        cores
    ):

        janela_resultado = tk.Toplevel(
            self.janela
        )

        janela_resultado.title(
            "Resultado do DSATUR"
        )

        janela_resultado.geometry(
            "1100x650"
        )

        janela_resultado.resizable(
            False,
            False
        )


        titulo = tk.Label(
            janela_resultado,
            text="COLORACAO DE GRAFO - DSATUR",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )


        moldura_grafos = tk.Frame(
            janela_resultado
        )

        moldura_grafos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # GRAFO ORIGINAL
        moldura_original = tk.Frame(
            moldura_grafos
        )

        moldura_original.pack(
            side="left",
            padx=10
        )


        tk.Label(
            moldura_original,
            text="Grafo original",
            font=("Arial", 14, "bold")
        ).pack(
            pady=5
        )


        canvas_original = tk.Canvas(
            moldura_original,
            width=500,
            height=500,
            bg="white",
            bd=2,
            relief="solid"
        )

        canvas_original.pack()

        # GRAFO COLORIDO
        moldura_colorido = tk.Frame(
            moldura_grafos
        )

        moldura_colorido.pack(
            side="right",
            padx=10
        )


        tk.Label(
            moldura_colorido,
            text="Grafo colorido - DSATUR",
            font=("Arial", 14, "bold")
        ).pack(
            pady=5
        )


        canvas_colorido = tk.Canvas(
            moldura_colorido,
            width=500,
            height=500,
            bg="white",
            bd=2,
            relief="solid"
        )

        canvas_colorido.pack()


        self.desenhar_grafo(
            canvas_original
        )


        self.desenhar_grafo(
            canvas_colorido,
            cores=cores
        )

    # CARREGAR GRAFO DE ARQUIVO
    def carregar_grafo(self):

        caminho = filedialog.askopenfilename(
            title="Selecionar arquivo do grafo",
            filetypes=[
                (
                    "Arquivos de texto",
                    "*.txt"
                ),
                (
                    "Todos os arquivos",
                    "*.*"
                )
            ]
        )


        if not caminho:
            return


        direcionado = messagebox.askyesno(
            "Tipo do grafo",
            "O grafo do arquivo e direcionado?\n\n"
            "Sim = grafo direcionado\n"
            "Nao = grafo nao direcionado"
        )


        try:

            novo_grafo = carregar_grafo_arquivo(
                caminho,
                direcionado=direcionado
            )

            self.grafo = novo_grafo


            if direcionado:

                tipo = "Direcionado"

            else:

                tipo = "Nao direcionado"


            messagebox.showinfo(
                "Grafo carregado",
                "Grafo carregado com sucesso.\n\n"
                f"Tipo: {tipo}\n"
                f"Vertices: {len(self.grafo.vertices)}\n"
                f"Arcos: {len(self.grafo.arcos)}"
            )


        except Exception as erro:

            messagebox.showerror(
                "Erro",
                "Nao foi possivel carregar o grafo.\n\n"
                f"{erro}"
            )

    # CARREGAR MAPA DO PARANA
    def carregar_parana(self):

        try:

            self.grafo = carregar_mapa_parana()


            messagebox.showinfo(
                "Mapa do Parana",
                "Mapa do Parana carregado com sucesso.\n\n"
                f"Vertices: {len(self.grafo.vertices)}\n"
                f"Arcos: {len(self.grafo.arcos)}"
            )


        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Nao foi possivel carregar o mapa.\n\n{erro}"
            )

    # EXECUTAR A*
    def executar_astar(self):

        if not self.grafo.vertices:

            messagebox.showerror(
                "Erro",
                "O grafo nao possui vertices."
            )

            return

        # VERIFICAR COORDENADAS
        vertices_sem_coordenadas = []


        for id_vertice, vertice in self.grafo.vertices.items():

            if (
                vertice.latitude is None
                or vertice.longitude is None
            ):

                vertices_sem_coordenadas.append(
                    id_vertice
                )


        if vertices_sem_coordenadas:

            texto = (
                "Nao e possivel executar o A*.\n\n"
                "Os seguintes vertices nao possuem "
                "latitude e longitude:\n\n"
            )


            for id_vertice in vertices_sem_coordenadas:

                texto += (
                    f"- {id_vertice}\n"
                )


            texto += (
                "\nPara utilizar o A*, todos os vertices "
                "devem possuir coordenadas geograficas."
            )


            messagebox.showerror(
                "Coordenadas ausentes",
                texto
            )

            return


        vertices = list(
            self.grafo.vertices.keys()
        )

        # JANELA DE SELECAO
        janela_selecao = tk.Toplevel(
            self.janela
        )

        janela_selecao.title(
            "Executar A*"
        )

        janela_selecao.geometry(
            "420x300"
        )

        janela_selecao.resizable(
            False,
            False
        )


        titulo = tk.Label(
            janela_selecao,
            text="ALGORITMO A*",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=20
        )


        tk.Label(
            janela_selecao,
            text="Vertice de origem:",
            font=("Arial", 11)
        ).pack()


        combo_origem = ttk.Combobox(
            janela_selecao,
            values=vertices,
            state="readonly",
            width=30
        )

        combo_origem.pack(
            pady=5
        )


        if vertices:

            combo_origem.current(
                0
            )


        tk.Label(
            janela_selecao,
            text="Vertice de destino:",
            font=("Arial", 11)
        ).pack(
            pady=(10, 0)
        )


        combo_destino = ttk.Combobox(
            janela_selecao,
            values=vertices,
            state="readonly",
            width=30
        )

        combo_destino.pack(
            pady=5
        )


        if len(vertices) > 1:

            combo_destino.current(
                len(vertices) - 1
            )

        elif vertices:

            combo_destino.current(
                0
            )


        def confirmar():

            origem = combo_origem.get()
            destino = combo_destino.get()


            if not origem or not destino:

                messagebox.showerror(
                    "Erro",
                    "Selecione a origem e o destino.",
                    parent=janela_selecao
                )

                return


            if origem == destino:

                messagebox.showerror(
                    "Erro",
                    "A origem e o destino devem ser diferentes.",
                    parent=janela_selecao
                )

                return


            try:

                astar = AStar(
                    self.grafo
                )

                caminho = astar.executar(
                    origem,
                    destino
                )


            except ValueError as erro:

                messagebox.showerror(
                    "Erro",
                    str(erro),
                    parent=janela_selecao
                )

                return


            if caminho is None:

                messagebox.showerror(
                    "A*",
                    "Nao foi encontrado um caminho "
                    "entre os vertices selecionados.",
                    parent=janela_selecao
                )

                return


            janela_selecao.destroy()


            self.mostrar_resultado_astar(
                astar,
                origem,
                destino,
                caminho
            )


        botao_executar = tk.Button(
            janela_selecao,
            text="Executar A*",
            command=confirmar,
            width=20
        )

        botao_executar.pack(
            pady=20
        )

    # RESULTADO DO A*
    def mostrar_resultado_astar(
        self,
        astar,
        origem,
        destino,
        caminho
    ):

        janela_resultado = tk.Toplevel(
            self.janela
        )

        janela_resultado.title(
            "Resultado do A*"
        )

        janela_resultado.geometry(
            "1200x720"
        )

        janela_resultado.resizable(
            False,
            False
        )


        titulo = tk.Label(
            janela_resultado,
            text="CAMINHO MINIMO - A*",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        # INFORMACOES
        moldura_info = tk.Frame(
            janela_resultado,
            bd=2,
            relief="groove"
        )

        moldura_info.pack(
            padx=20,
            pady=5,
            fill="x"
        )


        texto_caminho = (
            " -> ".join(caminho)
        )


        tk.Label(
            moldura_info,
            text=f"Origem: {origem}",
            font=("Arial", 11, "bold")
        ).pack(
            anchor="w",
            padx=10,
            pady=(8, 2)
        )


        tk.Label(
            moldura_info,
            text=f"Destino: {destino}",
            font=("Arial", 11, "bold")
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )


        tk.Label(
            moldura_info,
            text=f"Caminho: {texto_caminho}",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )


        tk.Label(
            moldura_info,
            text=f"Custo total: {astar.custo:.2f} km",
            font=("Arial", 11, "bold")
        ).pack(
            anchor="w",
            padx=10,
            pady=(2, 8)
        )

        # CONTEUDO
        moldura_conteudo = tk.Frame(
            janela_resultado
        )

        moldura_conteudo.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # GRAFO
        moldura_grafo = tk.Frame(
            moldura_conteudo
        )

        moldura_grafo.pack(
            side="left",
            padx=10
        )


        tk.Label(
            moldura_grafo,
            text="Grafo com caminho minimo destacado",
            font=("Arial", 13, "bold")
        ).pack(
            pady=5
        )


        canvas = tk.Canvas(
            moldura_grafo,
            width=760,
            height=480,
            bg="white",
            bd=2,
            relief="solid"
        )

        canvas.pack()

        # HEURISTICAS
        moldura_heuristicas = tk.Frame(
            moldura_conteudo,
            bd=2,
            relief="groove"
        )

        moldura_heuristicas.pack(
            side="right",
            fill="y",
            padx=10
        )


        tk.Label(
            moldura_heuristicas,
            text="HEURISTICAS h(n)",
            font=("Arial", 13, "bold")
        ).pack(
            pady=10
        )


        tk.Label(
            moldura_heuristicas,
            text=f"Destino: {destino}",
            font=("Arial", 10)
        ).pack(
            pady=(0, 10)
        )


        texto_heuristicas = tk.Text(
            moldura_heuristicas,
            width=31,
            height=23,
            font=("Courier", 11)
        )

        texto_heuristicas.pack(
            padx=10,
            pady=5
        )


        for vertice, heuristica in astar.heuristicas.items():

            linha = (
                f"{vertice:<20} "
                f"{heuristica:>7.2f} km\n"
            )

            texto_heuristicas.insert(
                tk.END,
                linha
            )


        texto_heuristicas.config(
            state="disabled"
        )


        self.desenhar_grafo(
            canvas,
            caminho=caminho,
            largura=760,
            altura=480,
            usar_coordenadas=True
        )

    # CALCULAR POSICOES GEOGRAFICAS
    def calcular_posicoes_geograficas(
        self,
        largura,
        altura
    ):

        vertices = list(
            self.grafo.vertices.values()
        )


        if not vertices:
            return None


        for vertice in vertices:

            if (
                vertice.latitude is None
                or vertice.longitude is None
            ):

                return None


        latitudes = [
            vertice.latitude
            for vertice in vertices
        ]

        longitudes = [
            vertice.longitude
            for vertice in vertices
        ]


        latitude_minima = min(
            latitudes
        )

        latitude_maxima = max(
            latitudes
        )

        longitude_minima = min(
            longitudes
        )

        longitude_maxima = max(
            longitudes
        )


        margem_x = 80
        margem_y = 60


        largura_util = (
            largura - 2 * margem_x
        )

        altura_util = (
            altura - 2 * margem_y
        )


        diferenca_longitude = (
            longitude_maxima
            - longitude_minima
        )

        diferenca_latitude = (
            latitude_maxima
            - latitude_minima
        )


        if diferenca_longitude == 0:

            diferenca_longitude = 1


        if diferenca_latitude == 0:

            diferenca_latitude = 1


        posicoes = {}


        for id_vertice, vertice in self.grafo.vertices.items():

            proporcao_x = (
                (
                    vertice.longitude
                    - longitude_minima
                )
                /
                diferenca_longitude
            )


            proporcao_y = (
                (
                    latitude_maxima
                    - vertice.latitude
                )
                /
                diferenca_latitude
            )


            x = (
                margem_x
                + proporcao_x
                * largura_util
            )


            y = (
                margem_y
                + proporcao_y
                * altura_util
            )


            posicoes[id_vertice] = (
                x,
                y
            )


        return posicoes

    # CALCULAR POSICOES CIRCULARES
    def calcular_posicoes_circulares(
        self,
        largura,
        altura
    ):

        vertices = list(
            self.grafo.vertices.keys()
        )

        quantidade = len(
            vertices
        )


        centro_x = largura / 2
        centro_y = altura / 2

        raio_grafo = min(
            largura,
            altura
        ) * 0.36


        posicoes = {}


        for i, id_vertice in enumerate(
            vertices
        ):

            angulo = (
                2 * math.pi * i / quantidade
                - math.pi / 2
            )


            x = (
                centro_x
                + raio_grafo
                * math.cos(angulo)
            )


            y = (
                centro_y
                + raio_grafo
                * math.sin(angulo)
            )


            posicoes[id_vertice] = (
                x,
                y
            )


        return posicoes

    # DESENHAR GRAFO
    def desenhar_grafo(
        self,
        canvas,
        cores=None,
        caminho=None,
        largura=500,
        altura=500,
        usar_coordenadas=False
    ):

        vertices = list(
            self.grafo.vertices.keys()
        )


        if not vertices:
            return


        raio_vertice = 22

        # POSICOES DOS VERTICES
        posicoes = None


        if usar_coordenadas:

            posicoes = (
                self.calcular_posicoes_geograficas(
                    largura,
                    altura
                )
            )


        if posicoes is None:

            posicoes = (
                self.calcular_posicoes_circulares(
                    largura,
                    altura
                )
            )

        # ARCOS DO CAMINHO A*
        arcos_caminho = set()


        if caminho is not None:

            for i in range(
                len(caminho) - 1
            ):

                origem = caminho[i]
                destino = caminho[i + 1]


                if self.grafo.direcionado:

                    arcos_caminho.add(
                        (
                            origem,
                            destino
                        )
                    )

                else:

                    arcos_caminho.add(
                        frozenset(
                            [
                                origem,
                                destino
                            ]
                        )
                    )

        # DESENHAR ARCOS
        for arco in self.grafo.arcos.values():

            x1, y1 = posicoes[
                arco.orig
            ]

            x2, y2 = posicoes[
                arco.dest
            ]


            if self.grafo.direcionado:

                chave_arco = (
                    arco.orig,
                    arco.dest
                )

            else:

                chave_arco = frozenset(
                    [
                        arco.orig,
                        arco.dest
                    ]
                )


            if (
                caminho is not None
                and chave_arco in arcos_caminho
            ):

                cor_arco = "red"
                largura_arco = 5

            else:

                cor_arco = "black"
                largura_arco = 2

            # GRAFO DIRECIONADO
            if self.grafo.direcionado:

                dx = x2 - x1
                dy = y2 - y1

                distancia = math.sqrt(
                    dx ** 2 + dy ** 2
                )


                if distancia > 0:

                    deslocamento_x = (
                        raio_vertice
                        * dx
                        / distancia
                    )

                    deslocamento_y = (
                        raio_vertice
                        * dy
                        / distancia
                    )


                    inicio_x = (
                        x1 + deslocamento_x
                    )

                    inicio_y = (
                        y1 + deslocamento_y
                    )

                    fim_x = (
                        x2 - deslocamento_x
                    )

                    fim_y = (
                        y2 - deslocamento_y
                    )

                else:

                    inicio_x = x1
                    inicio_y = y1
                    fim_x = x2
                    fim_y = y2


                canvas.create_line(
                    inicio_x,
                    inicio_y,
                    fim_x,
                    fim_y,
                    width=largura_arco,
                    fill=cor_arco,
                    arrow=tk.LAST,
                    arrowshape=(12, 15, 5)
                )


            # GRAFO NAO DIRECIONADO
            else:

                canvas.create_line(
                    x1,
                    y1,
                    x2,
                    y2,
                    width=largura_arco,
                    fill=cor_arco
                )

            # PESO DO ARCO
            meio_x = (
                x1 + x2
            ) / 2

            meio_y = (
                y1 + y2
            ) / 2


            canvas.create_rectangle(
                meio_x - 20,
                meio_y - 10,
                meio_x + 20,
                meio_y + 10,
                fill="white",
                outline=""
            )


            canvas.create_text(
                meio_x,
                meio_y,
                text=str(arco.val),
                fill=cor_arco,
                font=("Arial", 9, "bold")
            )

        # PALETA DO DSATUR
        paleta = [
            "#ff6b6b",
            "#4dabf7",
            "#69db7c",
            "#ffd43b",
            "#b197fc",
            "#ffa94d",
            "#66d9e8",
            "#f783ac",
            "#a9e34b",
            "#ced4da"
        ]

        # DESENHAR VERTICES
        for id_vertice in vertices:

            x, y = posicoes[
                id_vertice
            ]


            cor_vertice = "white"


            if cores is not None:

                numero_cor = cores[
                    id_vertice
                ]

                indice_cor = (
                    numero_cor - 1
                ) % len(paleta)

                cor_vertice = paleta[
                    indice_cor
                ]


            contorno = "black"
            largura_contorno = 2


            if (
                caminho is not None
                and id_vertice in caminho
            ):

                contorno = "red"
                largura_contorno = 4


            canvas.create_oval(
                x - raio_vertice,
                y - raio_vertice,
                x + raio_vertice,
                y + raio_vertice,
                fill=cor_vertice,
                outline=contorno,
                width=largura_contorno
            )

            # ID DO VERTICE
            if usar_coordenadas:

                canvas.create_text(
                    x,
                    y - raio_vertice - 9,
                    text=str(id_vertice),
                    font=("Arial", 9, "bold")
                )

            else:

                canvas.create_text(
                    x,
                    y,
                    text=str(id_vertice),
                    font=("Arial", 9, "bold")
                )


    # SAIR
    def sair(self):

        self.janela.destroy()

    # INICIAR INTERFACE
    def executar(self):

        self.janela.mainloop()