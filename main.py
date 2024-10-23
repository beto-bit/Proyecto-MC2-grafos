import tkinter
from tkinter import ttk, Tk, StringVar


def create_vertices_ui(frame: ttk.Frame) -> StringVar:
    vertex_label = ttk.Label(frame, text="Nombre del Vértice")
    vertex_label.grid(row=2, column=1, sticky='e', padx=10)

    new_vertex = StringVar()
    vertex_entry = ttk.Entry(frame, textvariable=new_vertex)
    vertex_entry.grid(row=2, column=2)

    return new_vertex



def main():
    root = Tk()
    root.title("Proyecto de MC2")

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    # ttk.Label(frame, text="Texto de Ejemplo").grid(column=0, row=0)
    # ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1)

    new_vertex = create_vertices_ui(frame)

    root.mainloop()

if __name__ == '__main__':
    print(f"Tkinter version {tkinter.TkVersion}")
    main()