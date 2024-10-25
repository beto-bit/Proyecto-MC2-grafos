from collections import deque

from tkinter import *
from tkinter import ttk

import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 700


# Configuración de la ventana principal
root = Tk()
root.title("Proyecto de MC2")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")


#icono = PhotoImage(file="icono.png")  # Reemplaza con la ruta de tu archivo
#raiz.iconphoto(False, icono)


# Canvas principal
canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='green')
canvas.pack(fill="both", expand=True)
frame = Frame(canvas, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="green")
frame.place(x=0, y=0)


# Estilo de botones y etiquetas
style = ttk.Style()
style.configure(
    "Rounded.TButton",
    background="#87ceeb",
    foreground="black",
    borderwidth=0,
    relief="flat"
)
style.configure(
    "Rounded.TLabel",
    background="#87ceeb",
    foreground="black",
    borderwidth=2,
    relief="flat"
)


# Variables
new_vertex = StringVar()
out_vertex = StringVar()
in_vertex = StringVar()
visit_order = StringVar()
visit_order_depth = StringVar()
vertices: list[str] = []
G = nx.Graph()


# Funciones principales
def AddVertex():
    vertex_new_val = new_vertex.get().upper()

    # Sanity check
    if not vertex_new_val:
        return

    if vertex_new_val in vertices:
        return

    # Appending
    vertices.append(vertex_new_val)
    G.add_node(vertex_new_val)

    new_vertex.set("")
    vertices_field.delete("1.0", END)

    for vertex in vertices:
        vertices_field.insert(END, f"{vertex}\n")


def AgregarArista():
    verticeSalidaNuevo = out_vertex.get().upper()
    verticeLlegadaNuevo = in_vertex.get().upper()
    if verticeSalidaNuevo in vertices and verticeLlegadaNuevo in vertices and verticeSalidaNuevo != verticeLlegadaNuevo:
        G.add_edge(verticeSalidaNuevo, verticeLlegadaNuevo)
        out_vertex.set("")
        in_vertex.set("")
        graficar_grafo(G, None, 40)


def color_degradado(num_nodos, total_nodos):
    cmap = plt.colormaps['Oranges']
    norm = mcolors.Normalize(vmin=0, vmax=total_nodos - 1)
    return cmap(norm(num_nodos))


def BusquedaAncho(grafo, inicio):
    queue = deque([inicio])
    visited = set()
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            order.append(node)
            visited.add(node)
            neighbors = sorted(grafo.neighbors(node))
            queue.extend(neighbors)
    return order


def BusquedaProfundidad(grafo, inicio):
    stack = [inicio]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            order.append(node)
            visited.add(node)
            neighbors = sorted(grafo.neighbors(node), reverse=True)
            stack.extend(neighbors)
    return order


def graficar_grafo(grafo, order=None, posY=None):
    pos = nx.planar_layout(grafo)
    fig, ax = plt.subplots(figsize=(4, 3))
    node_colors = [color_degradado(i, len(grafo)) for i in range(len(grafo))]
    nx.draw(
        grafo,
        pos,
        ax=ax,
        with_labels=True,
        node_color='lightblue',
        edge_color='gray',
        node_size=600,
        font_size=8
    )
    if order:
        for i in range(len(order)):
            nx.draw_networkx_nodes(
                grafo,
                pos,
                nodelist=[order[i]],
                node_color=[node_colors[i]],
                ax=ax
            )
        for i in range(len(order)-1):
            if (order[i], order[i + 1]) in grafo.edges or (order[i + 1], order[i]) in grafo.edges:
                nx.draw_networkx_edges(
                    grafo,
                    pos,
                    edgelist=[(order[i], order[i + 1])],
                    width=1,
                    edge_color='r',
                    style='dashed',
                    ax=ax
                )

            #nx.draw_networkx_edges(grafo, pos, edgelist=[(order[i], order[i+1])], width=2, edge_color='r', style='dashed', ax=ax)
    canvas_fig = FigureCanvasTkAgg(fig, master=frame)
    canvas_fig.draw()
    canvas_fig.get_tk_widget().place(x=640, y=posY)


def iniciar_busqueda_ancho():
    if vertices:
        order = BusquedaAncho(G, vertices[0])
        visit_order.set(", ".join(order))
        graficar_grafo(G, order, 370)


def iniciar_busqueda_profundidad():
    if vertices:
        order = BusquedaProfundidad(G, vertices[0])
        visit_order_depth.set(", ".join(order))
        graficar_grafo(G, order, 370)


# Elementos de la interfaz
Entry(frame, textvariable=new_vertex, bg="#9370DB").place(x=250, y=50, width=150)

ttk.Label(
    frame,
    text="Coloca la etiqueta para un vértice:",
    style="Rounded.TLabel"
).place(x=50, y=50)

ttk.Button(
    frame,
    text="Guardar Vértice",
    command=AddVertex,
    style="Rounded.TButton"
).place(x=420, y=40, width=150, height=40)

vertices_field = Text(frame, width=16, height=6)
vertices_field.place(x=250, y=100)
ttk.Label(frame, text="Vértices disponibles:", style="Rounded.TLabel").place(x=50, y=100)

Entry(frame, textvariable=out_vertex, bg="#9370DB").place(x=250, y=220, width=150)
ttk.Label(frame, text="Vértice de salida:", style="Rounded.TLabel").place(x=50, y=220)
Entry(frame, textvariable=in_vertex, bg="#9370DB").place(x=250, y=250, width=150)
ttk.Label(frame, text="Vértice de llegada:", style="Rounded.TLabel").place(x=50, y=250)
ttk.Button(
    frame,
    text="Guardar Arista",
    command=AgregarArista,
    style="Rounded.TButton"
).place(x=420, y=225, width=150, height=40)

# Botones de búsqueda y etiquetas de resultado
ttk.Button(
    frame,
    text="Búsqueda a lo Ancho",
    command=iniciar_busqueda_ancho,
    style="Rounded.TButton"
).place(x=250, y=320, width=150, height=40)

ttk.Label(frame, textvariable=visit_order, style="Rounded.TLabel").place(x=420, y=320)

ttk.Button(
    frame,
    text="Búsqueda a lo Profundo",
    command=iniciar_busqueda_profundidad,
    style="Rounded.TButton"
).place(x=250, y=370, width=150, height=40)
ttk.Label(frame, textvariable=visit_order_depth, style="Rounded.TLabel").place(x=420, y=370)

#------------------- LÍNEAS DIVISORIAS ------------------------
ttk.Separator(frame, orient='vertical').place(x=600, y=0, relheight=80)  # Línea vertical divisoria
# ttk.Separator(miFrame, orient='horizontal').place(x=0, y=250, relwidth=1)  # Línea horizontal divisoria


root.mainloop()