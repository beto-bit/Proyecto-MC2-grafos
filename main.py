
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as mcolors
from collections import deque


raiz = Tk() 

raiz.title("Proyecto de MC2") 

miFrame = Frame(raiz, width=1200, height=600)
miFrame.config(bg="lightgrey")
miFrame.pack()

""" LabelTitulo = Label(miFrame, text="Proyecto MC2", font=("Leelawadee UI", 24))
LabelTitulo.place(x=220, y=5) """

#VARIABLES Y ARREGLOS DE LA FUNCIÓN 

verticeNuevo = StringVar() 

verticeSalida = StringVar()

verticeLlegada = StringVar()

listaCampoVertices = StringVar() 

ordenVisita = StringVar()

ListaVertices = []

ListaVerticesSalida = []

ListaVerticesLlegada = []

G = nx.Graph()

#FUNCIONES DEL PROGRAMA 


#------------------------FUNCIÓN QUE AGREGA VÉRTICES--------------------------
def AgregarVertice():
 verticeNuevoValor=verticeNuevo.get()
 if(verticeNuevoValor!=""):
    ListaVertices.append(verticeNuevoValor)
    G.add_node(verticeNuevoValor)
    verticeNuevo.set("")

    CampoVertices.delete("1.0", "{}.0".format(len(ListaVertices)))
    print(len(ListaVertices))

    for i in ListaVertices:
        CampoVertices.insert("1.0", "{} \n".format(i))
        print(i)

 else:
    print(0)

#------------------------FUNCIÓN QUE AGREGA ARISTAS--------------------------    
 
def AgregarArista():
    verticeSalidaNuevo=verticeSalida.get()
    verticeLlegadaNuevo=verticeLlegada.get()

    for ex in ListaVertices:
        if(ex == verticeSalidaNuevo):
            verticeValido1 = 1
            break
        else:
            verticeValido1 = 0

    for ed in ListaVertices:
        if(ed == verticeLlegadaNuevo):
            verticeValido2 = 1
            break
        else:
            verticeValido2 = 0

    if((verticeValido1==1) and (verticeValido2==1)):

        verticeSalida.set("")
        verticeLlegada.set("")
        
        G.add_edge(verticeSalidaNuevo, verticeLlegadaNuevo)


        fig, ax = plt.subplots(figsize=(4, 3))  # Ajustar el tamaño de la figura
        pos = nx.planar_layout(G)  # Posicionamiento plano
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=600, font_size=8)
    
        canvas = FigureCanvasTkAgg(fig, master=miFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=6, padx=10, pady=10)

        """ nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=16)
            .pack(side=TOP, fill=BOTH, expand=1)
        
        plt.show() """

        """ if(verticeSalidaNuevo!="" and verticeLlegadaNuevo!=""):
            if(verticeSalidaNuevo!=verticeLlegadaNuevo):
                ListaVerticesSalida.append(verticeSalidaNuevo)
                ListaVerticesLlegada.append(verticeLlegadaNuevo)
                CampoAristas.delete("1.0", "{}.0".format(len(ListaVerticesSalida)))

                print(ListaVerticesSalida)
                print(ListaVerticesLlegada)

                for j in ListaVerticesSalida:
                    for k in ListaVerticesLlegada:
                        if(ListaVerticesSalida.index(j)==ListaVerticesLlegada.index(k)):
                            CampoAristas.insert("1.0", "{} - {}\n".format(j, k))
                        else:
                            print(0)
            else:
                print(0)
        else:
            print(0) """
    else:
        print(0)    

def agregar_nodo_y_buscar():
    if 'A' not in G:
        G.add_node('A')
    order = BusquedaAncho(G, 'A')
    graficar_grafo(G, order)   

def graficar_grafo(grafo, order):
    pos = nx.planar_layout(grafo)
    fig, ax = plt.subplots(figsize=(4, 3))
    node_colors= [color_degradado(i, len(grafo)) for i in range(len(order))]
    
    nx.draw_networkx(grafo, pos, node_size=500, ax=ax)
    nx.draw_networkx_edges(grafo, pos, width=1, ax=ax)
    nx.draw_networkx_labels(grafo, pos, font_size=3, ax=ax)

    for i in range(len(order)):
        nx.draw_networkx_nodes(grafo, pos, nodelist=[order[i]], node_color=[node_colors[i]], ax=ax, edgecolors=None, linewidths=0)

    for i in range(len(order)-1):
        nx.draw_networkx_edges(grafo, pos, edgelist=[(order[i], order[i+1])], width=2, edge_color='r', style='dashed', ax=ax)
    
        

    canvas = FigureCanvasTkAgg(fig, master=miFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=6, padx=10, pady=10)

def BusquedaAncho(grafo, inicio):
    if inicio not in grafo:
        raise nx.NetworkXError(f"El nodo {inicio} no se encuentra en el grafo.")
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

def color_degradado(num_nodos, total_nodos):
    cmap = plt.cm.Oranges  # Colormap
    norm = mcolors.Normalize(vmin=0, vmax=total_nodos - 1)
    return cmap(norm(num_nodos))    

""" def BusquedaAncho(grafo, inicio):
    if inicio not in grafo:
        raise nx.NetworkXError(f"El nodo {inicio} no se encuentra en el grafo G.")
    stack = [inicio]
    visited = set()
    queue = deque([inicio])
    order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            order.append(node)
            visited.add(node)
            neighbors = sorted(grafo.neighbors(node))
            queue.extend(neighbors)
            #stack.extend(list(grafo.neighbors(node))[::-1])
        return order
    


    # Graficar el grafo
    pos = nx.planar_layout(grafo)
    fig, ax = plt.subplots(figsize=(4, 3))
    nx.draw_networkx(G, pos, node_size=600)
    nx.draw_networkx_edges(G, pos, width=5)
    nx.draw_networkx_labels(G, pos, font_size=15, ax=ax)

    for i in range(len(order)-1):
        nx.draw_networkx_edges(G, pos, edgelist=[(order[i], order[i+1])], width=5, edge_color='r', style='dashed', ax=ax)


    
    canvas = FigureCanvasTkAgg(fig, master=miFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=6, padx=10, pady=10)


    """
 

#----------------------Campos vertices------------------------------

CuadroVertice=Entry(miFrame, textvariable=verticeNuevo)
CuadroVertice.grid(row=2, column=2, padx=3, pady=10)

LabelVertice=Label(miFrame, text="Coloca la etiqueta para un vértice: " )
LabelVertice.grid(row=2, column=1, sticky="e", padx=10, pady=10)

BotonGuardarVertice=Button(miFrame, text="Guardar", command=AgregarVertice)
BotonGuardarVertice.grid(row=2, column=3, padx=10, pady=10)

#text area donde aparecen los vértices existentes
CampoVertices=Text(miFrame, width=16, height=6)
CampoVertices.grid(row=3, column=3, padx=5, pady=10)

LabelVerticeCampo=Label(miFrame, text="Vértices disponibles: " )
LabelVerticeCampo.grid(row=3, column=2, sticky="e", padx=10, pady=10)

scrollVertices=Scrollbar(miFrame, command=CampoVertices.yview)
scrollVertices.grid(row=3, column=4, sticky="nsew")

CampoVertices.config(yscrollcommand=scrollVertices.set)


#------------------------CAMPOS ARISTAS-----------------------

CuadroVerticeSalida=Entry(miFrame, textvariable=verticeSalida)
CuadroVerticeSalida.grid(row=2, column=6, padx=3, pady=10)

LabelVerticeSalida=Label(miFrame, text="Coloca el vértice de salida: " )
LabelVerticeSalida.grid(row=2, column=5, sticky="e", padx=10, pady=10) 

CuadroVerticeLlegada=Entry(miFrame, textvariable=verticeLlegada)
CuadroVerticeLlegada.grid(row=3, column=6, padx=3, pady=10)

LabelVerticeLlegada=Label(miFrame, text="Coloca el vértice de llegada: " )
LabelVerticeLlegada.grid(row=3, column=5, sticky="e", padx=10, pady=10) 

BotonGuardarArista=Button(miFrame, text="Guardar arista", command=AgregarArista)
BotonGuardarArista.grid(row=3, column=7, padx=10, pady=10)

#text area donde aparecen las aristas existentes

""" CampoAristas=Text(miFrame, width=16, height=6)
CampoAristas.grid(row=4, column=7, padx=5, pady=10)

LabelAristasCampo=Label(miFrame, text="Aristas creadas: " )
LabelAristasCampo.grid(row=4, column=6, sticky="e", padx=10, pady=10)

scrollAristas=Scrollbar(miFrame, command=CampoVertices.yview)
scrollAristas.grid(row=4, column=8, sticky="nsew")

CampoAristas.config(yscrollcommand=scrollAristas.set) """

#--------------------BOTÓN PARA EL ALGOTIMO DE BÚSQUEDA A LO ANCHO---------------------

BotonBusquedaAncho=Button(miFrame, text="Búsqueda a lo Ancho", command=agregar_nodo_y_buscar)
BotonBusquedaAncho.grid(row=4, column=7, padx=10, pady=10)

#--------------------LABEL PARA VER EL ORDEN DE BÚSQUEDA----------------
LabelBusquedaAncho=Label(miFrame, textvariable=ordenVisita)
LabelBusquedaAncho.grid(row=4, column=8, sticky="e", padx=10, pady=10) 






raiz.mainloop()