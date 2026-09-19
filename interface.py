import math
import tkinter as tk
from tkinter import messagebox, simpledialog

from grafo import Grafo
from prim import Prim
from busca import Busca
from roy import Roy


RAIO = 20

CORES_COMPONENTES = [
    "lightblue", "lightgreen", "lightyellow", "lightpink",
    "orange", "plum", "lightgray", "khaki",
]

EXEMPLO_NAO_DIRECIONADO = [
    ("E1", "A", "B", 4),
    ("E2", "A", "C", 2),
    ("E3", "B", "C", 1),
    ("E4", "B", "D", 5),
    ("E5", "C", "D", 8),
    ("E6", "D", "E", 3),
    ("E7", "E", "F", 6),
    ("E8", "D", "F", 7),
]

EXEMPLO_DIRECIONADO = [
    ("E1", "A", "B", 1),
    ("E2", "B", "C", 2),
    ("E3", "C", "A", 3),
    ("E4", "C", "D", 4),
    ("E5", "D", "E", 5),
    ("E6", "E", "D", 6),
    ("E7", "E", "F", 7),
]


class Interface:

    def __init__(self):

        self.grafo = Grafo()
        self.cores_vertices = {}
        self.cores_arestas = {}

        self.janela = tk.Tk()
        self.janela.title("Grafos - T1")
        self.janela.geometry("1000x700")

        self.criar_menu()
        self.criar_telas()

        self.desenhar()


    def iniciar(self):

        self.janela.mainloop()


    def criar_menu(self):

        barra = tk.Menu(self.janela)

        menu_grafo = tk.Menu(barra, tearoff=0)
        menu_grafo.add_command(
            label="Novo grafo nao direcionado",
            command=lambda: self.novo_grafo(False)
        )
        menu_grafo.add_command(
            label="Novo grafo direcionado",
            command=lambda: self.novo_grafo(True)
        )
        menu_grafo.add_separator()
        menu_grafo.add_command(
            label="Exemplo nao direcionado",
            command=lambda: self.carregar_exemplo(False)
        )
        menu_grafo.add_command(
            label="Exemplo direcionado",
            command=lambda: self.carregar_exemplo(True)
        )
        menu_grafo.add_separator()
        menu_grafo.add_command(label="Sair", command=self.janela.destroy)
        barra.add_cascade(label="Grafo", menu=menu_grafo)

        menu_editar = tk.Menu(barra, tearoff=0)
        menu_editar.add_command(
            label="Inserir vertice", command=self.inserir_vertice
        )
        menu_editar.add_command(
            label="Inserir aresta/arco", command=self.inserir_aresta
        )
        menu_editar.add_command(
            label="Remover vertice", command=self.remover_vertice
        )
        menu_editar.add_command(
            label="Remover aresta/arco", command=self.remover_aresta
        )
        barra.add_cascade(label="Editar", menu=menu_editar)

        menu_mostrar = tk.Menu(barra, tearoff=0)
        menu_mostrar.add_command(
            label="Lista de adjacencia", command=self.mostrar_lista
        )
        menu_mostrar.add_command(
            label="Matriz de adjacencia", command=self.mostrar_matriz_adj
        )
        menu_mostrar.add_command(
            label="Matriz de incidencia", command=self.mostrar_matriz_inc
        )
        menu_mostrar.add_separator()
        menu_mostrar.add_command(
            label="Limpar destaque do desenho", command=self.limpar_destaque
        )
        barra.add_cascade(label="Mostrar", menu=menu_mostrar)

        menu_algoritmos = tk.Menu(barra, tearoff=0)
        menu_algoritmos.add_command(
            label="Prim (AGM)", command=self.aplicar_prim
        )
        menu_algoritmos.add_command(
            label="Busca em profundidade", command=self.aplicar_busca
        )
        menu_algoritmos.add_command(
            label="Roy (componentes)", command=self.aplicar_roy
        )
        barra.add_cascade(label="Algoritmos", menu=menu_algoritmos)

        self.janela.config(menu=barra)


    def criar_telas(self):

        self.moldura_grafo = tk.LabelFrame(
            self.janela, text="Grafo ativo", bd=3, relief="groove"
        )
        self.moldura_grafo.pack(fill="both", expand=True, padx=8, pady=8)

        self.canvas = tk.Canvas(self.moldura_grafo, bg="white")
        self.canvas.pack(fill="both", expand=True, padx=4, pady=4)
        self.canvas.bind("<Configure>", lambda evento: self.desenhar())

        moldura_texto = tk.LabelFrame(
            self.janela, text="Resultados", bd=3, relief="groove"
        )
        moldura_texto.pack(fill="x", padx=8, pady=(0, 8))

        self.texto = tk.Text(
            moldura_texto, height=12, font=("Courier", 11), state="disabled"
        )
        self.texto.pack(fill="x", padx=4, pady=4)


    def escrever(self, conteudo):

        self.texto.config(state="normal")
        self.texto.delete("1.0", "end")
        self.texto.insert("end", conteudo)
        self.texto.config(state="disabled")


    def erro(self, mensagem):

        messagebox.showerror("Erro", mensagem, parent=self.janela)


    def perguntar(self, titulo, pergunta, inicial=""):

        resposta = simpledialog.askstring(
            titulo, pergunta, initialvalue=inicial, parent=self.janela
        )

        if resposta is None:
            return None

        resposta = resposta.strip()

        if resposta == "":
            return None

        return resposta


    def posicoes(self):

        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()

        centro_x = largura / 2
        centro_y = altura / 2
        raio = max(min(largura, altura) / 2 - 60, 30)

        quantidade = len(self.grafo.vertices)

        posicao = {}

        for i, id in enumerate(self.grafo.vertices):

            angulo = 2 * math.pi * i / quantidade - math.pi / 2

            x = centro_x + raio * math.cos(angulo)
            y = centro_y + raio * math.sin(angulo)

            posicao[id] = (x, y)

        return posicao


    def ponto_na_borda(self, x, y, alvo_x, alvo_y):

        dx = alvo_x - x
        dy = alvo_y - y

        distancia = math.hypot(dx, dy)

        return x + dx / distancia * RAIO, y + dy / distancia * RAIO


    def tem_inversa(self, aresta):

        for outra in self.grafo.arestas.values():

            if outra.orig == aresta.dest and outra.dest == aresta.orig:
                return True

        return False


    def desenhar_aresta(self, aresta, posicao):

        destacando = self.cores_arestas or self.cores_vertices

        if aresta.id in self.cores_arestas:
            cor = self.cores_arestas[aresta.id]
            largura = 4
        elif destacando:
            cor = "lightgray"
            largura = 1
        else:
            cor = "black"
            largura = 2

        x1, y1 = posicao[aresta.orig]
        x2, y2 = posicao[aresta.dest]

        rotulo = f"{aresta.id} ({aresta.val})"

        if aresta.orig == aresta.dest:

            self.canvas.create_oval(
                x1 - 15, y1 - RAIO - 30, x1 + 15, y1 - RAIO + 2,
                outline=cor, width=largura
            )

            self.escrever_rotulo(x1, y1 - RAIO - 40, rotulo)

            return

        meio_x = (x1 + x2) / 2
        meio_y = (y1 + y2) / 2

        controle_x = meio_x
        controle_y = meio_y

        if self.grafo.direcionado and self.tem_inversa(aresta):

            distancia = math.hypot(x2 - x1, y2 - y1)

            controle_x = meio_x - (y2 - y1) / distancia * 40
            controle_y = meio_y + (x2 - x1) / distancia * 40

        ax, ay = self.ponto_na_borda(x1, y1, controle_x, controle_y)
        bx, by = self.ponto_na_borda(x2, y2, controle_x, controle_y)

        seta = tk.LAST if self.grafo.direcionado else tk.NONE

        self.canvas.create_line(
            ax, ay, controle_x, controle_y, bx, by,
            smooth=True, arrow=seta, arrowshape=(14, 16, 6),
            fill=cor, width=largura
        )

        self.escrever_rotulo(
            (meio_x + controle_x) / 2, (meio_y + controle_y) / 2, rotulo
        )


    def escrever_rotulo(self, x, y, rotulo):

        texto = self.canvas.create_text(
            x, y, text=rotulo, fill="blue", font=("Arial", 9)
        )

        fundo = self.canvas.create_rectangle(
            self.canvas.bbox(texto), fill="white", outline=""
        )

        self.canvas.tag_lower(fundo, texto)


    def desenhar(self):

        self.canvas.delete("all")

        posicao = self.posicoes()

        for aresta in self.grafo.arestas.values():
            self.desenhar_aresta(aresta, posicao)

        for id in self.grafo.vertices:

            x, y = posicao[id]

            cor = self.cores_vertices.get(id, "white")

            self.canvas.create_oval(
                x - RAIO, y - RAIO, x + RAIO, y + RAIO,
                fill=cor, outline="black", width=2
            )

            self.canvas.create_text(
                x, y, text=id, font=("Arial", 11, "bold")
            )

        if self.grafo.direcionado:
            tipo = "direcionado"
        else:
            tipo = "nao direcionado"

        self.moldura_grafo.config(
            text=(
                f"Grafo ativo - {tipo} - "
                f"{len(self.grafo.vertices)} vertice(s) - "
                f"{len(self.grafo.arestas)} aresta(s)/arco(s)"
            )
        )


    def limpar_destaque(self):

        self.cores_vertices = {}
        self.cores_arestas = {}

        self.desenhar()


    def novo_grafo(self, direcionado):

        self.grafo = Grafo(direcionado)

        self.escrever("")
        self.limpar_destaque()


    def carregar_exemplo(self, direcionado):

        self.grafo = Grafo(direcionado)

        for id in "ABCDEF":
            self.grafo.inserir_vertice(id)

        if direcionado:
            arestas = EXEMPLO_DIRECIONADO
        else:
            arestas = EXEMPLO_NAO_DIRECIONADO

        for id, orig, dest, val in arestas:
            self.grafo.inserir_aresta(id, orig, dest, val)

        self.escrever("")
        self.limpar_destaque()


    def inserir_vertice(self):

        id = self.perguntar("Inserir vertice", "Identificador do vertice:")

        if id is None:
            return

        try:
            self.grafo.inserir_vertice(id)
        except ValueError as e:
            self.erro(str(e))
            return

        self.limpar_destaque()


    def inserir_aresta(self):

        id = self.perguntar("Inserir aresta/arco", "Identificador da aresta:")

        if id is None:
            return

        orig = self.perguntar("Inserir aresta/arco", "Vertice de origem:")

        if orig is None:
            return

        dest = self.perguntar("Inserir aresta/arco", "Vertice de destino:")

        if dest is None:
            return

        valor = self.perguntar("Inserir aresta/arco", "Peso (numero):")

        if valor is None:
            return

        try:
            val = float(valor.replace(",", "."))
        except ValueError:
            self.erro("o peso deve ser um numero.")
            return

        if val.is_integer():
            val = int(val)

        try:
            self.grafo.inserir_aresta(id, orig, dest, val)
        except ValueError as e:
            self.erro(str(e))
            return

        self.limpar_destaque()


    def remover_vertice(self):

        id = self.perguntar("Remover vertice", "Identificador do vertice:")

        if id is None:
            return

        try:
            self.grafo.remover_vertice(id)
        except ValueError as e:
            self.erro(str(e))
            return

        self.limpar_destaque()


    def remover_aresta(self):

        id = self.perguntar("Remover aresta/arco", "Identificador da aresta:")

        if id is None:
            return

        try:
            self.grafo.remover_aresta(id)
        except ValueError as e:
            self.erro(str(e))
            return

        self.limpar_destaque()


    def mostrar_lista(self):

        self.escrever(self.grafo.texto_lista_adjacencia())


    def mostrar_matriz_adj(self):

        self.escrever(self.grafo.texto_matriz_adjacencia())


    def mostrar_matriz_inc(self):

        self.escrever(self.grafo.texto_matriz_incidencia())


    def aplicar_prim(self):

        if len(self.grafo.vertices) == 0:
            self.erro("o grafo esta vazio.")
            return

        primeiro = next(iter(self.grafo.vertices))

        inicio = self.perguntar(
            "Prim", "Vertice inicial:", inicial=primeiro
        )

        if inicio is None:
            return

        prim = Prim(self.grafo)

        try:
            prim.executar(inicio)
        except ValueError as e:
            self.erro(str(e))
            return

        self.cores_vertices = {id: "lightgreen" for id in self.grafo.vertices}
        self.cores_arestas = {a.id: "red" for a in prim.agm}

        self.desenhar()

        self.escrever(prim.texto())


    def aplicar_busca(self):

        if len(self.grafo.vertices) == 0:
            self.erro("o grafo esta vazio.")
            return

        saida = self.perguntar("Busca em profundidade", "Vertice de saida:")

        if saida is None:
            return

        chegada = self.perguntar("Busca em profundidade", "Vertice de chegada:")

        if chegada is None:
            return

        busca = Busca(self.grafo)

        try:
            busca.executar(saida, chegada)
        except ValueError as e:
            self.erro(str(e))
            return

        self.cores_vertices = {id: "lightyellow" for id in busca.visitados}
        self.cores_vertices[saida] = "lightgreen"
        self.cores_vertices[chegada] = "salmon"

        self.cores_arestas = {a.id: "blue" for a in busca.arvore}

        for aresta in busca.caminho:
            self.cores_arestas[aresta.id] = "red"

        self.desenhar()

        self.escrever(busca.texto(saida, chegada))


    def aplicar_roy(self):

        roy = Roy(self.grafo)

        try:
            roy.executar()
        except ValueError as e:
            self.erro(str(e))
            return

        self.cores_vertices = {}
        self.cores_arestas = {}

        numero = {}

        for i, componente in enumerate(roy.componentes):

            cor = CORES_COMPONENTES[i % len(CORES_COMPONENTES)]

            for id in componente:
                self.cores_vertices[id] = cor
                numero[id] = i

        for aresta in self.grafo.arestas.values():

            if numero[aresta.orig] == numero[aresta.dest]:
                self.cores_arestas[aresta.id] = "black"

        self.desenhar()

        self.escrever(roy.texto())
