from typing import Callable

import tkinter
from tkinter import ttk, Tk, StringVar


def create_vertices_ui(frame: ttk.Frame) -> StringVar:
    vertex_label = ttk.Label(frame, text="Nombre del Vértice")
    vertex_label.grid(row=2, column=1, sticky='e', padx=10)

    new_vertex = StringVar()
    vertex_entry = ttk.Entry(frame, textvariable=new_vertex)
    vertex_entry.grid(row=2, column=2)

    return new_vertex


def save_vertex_button(frame: ttk.Frame, func: Callable):
    vertex_btn = ttk.Button(frame, text="Añadir", command=func)
    vertex_btn.grid(row=2, column=3)


def add_vertex(vertex: str, vertices: set[str]):
    if vertex:
        vertices.add(vertex)


def add_vertex_ui(frame: ttk.Frame, vertices: set[str]):
    new_vertex = create_vertices_ui(frame)
    save_vertex_button(frame, lambda: add_vertex(new_vertex.get(), vertices))


def main():
    root = Tk()
    root.title("Proyecto de MC2")

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    # Add vertex functionality
    vertices = set()
    add_vertex_ui(frame, vertices)

    root.mainloop()
    print(vertices)

if __name__ == '__main__':
    print(f"Tkinter version {tkinter.TkVersion}")
    main()