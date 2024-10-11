from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        
        G.add_edge(verticeSalidaNuevo, verticeLlegadaNuevo)


        fig, ax = plt.subplots(figsize=(4, 3))  # Ajustar el tamaño de la figura
        pos = nx.planar_layout(G)  # Posicionamiento plano
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=600, font_size=8)
    
        canvas = FigureCanvasTkAgg(fig, master=miFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=1, padx=10, pady=10)

        """ nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=16)
            .pack(side=TOP, fill=BOTH, expand=1)
        
        plt.show() """

        if(verticeSalidaNuevo!="" and verticeLlegadaNuevo!=""):
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
            print(0)
    else:
        print(0)        


   
 

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

CampoAristas=Text(miFrame, width=16, height=6)
CampoAristas.grid(row=4, column=7, padx=5, pady=10)

LabelAristasCampo=Label(miFrame, text="Aristas creadas: " )
LabelAristasCampo.grid(row=4, column=6, sticky="e", padx=10, pady=10)

scrollAristas=Scrollbar(miFrame, command=CampoVertices.yview)
scrollAristas.grid(row=4, column=8, sticky="nsew")

CampoAristas.config(yscrollcommand=scrollAristas.set)







raiz.mainloop()