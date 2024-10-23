import tkinter
from tkinter import ttk, Tk



def main():
    root = Tk()
    root.title("Proyecto de MC2")

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    ttk.Label(frame, text="Texto de Ejemplo").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1)

    root.mainloop()

if __name__ == '__main__':
    print(f"Tkinter version {tkinter.TkVersion}")
    main()