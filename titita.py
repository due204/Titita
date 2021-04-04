import tkinter as Tkinter
import tkinter.ttk as ttk
from buscar import busqueda
from tkinter import messagebox
from validar_campos import Validacion
from base import BaseDatos
from factura import boleta
from re_factura import re_boleta
from editar import estado
from prints import imprimir


class MiVistas(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.vivista()
        self.valid = Validacion()

    def vivista(self):
        self.parent.title("Titita")
        self.parent.geometry("1050x470")
        self.parent.resizable(False, False)
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        # Define los distintos widgets
        self.nombre_label = Tkinter.Label(
            self.parent,
            text="Nombre:",
            bg="lavender",
        )
        self.nombre_entry = Tkinter.Entry(self.parent, width=100)
        self.nombre_label.place(x=0, y=0)
        self.nombre_entry.place(x=100, y=0)

        self.apellido_label = Tkinter.Label(
            self.parent,
            text="Apellido:",
            bg="lavender",
        )
        self.apellido_entry = Tkinter.Entry(self.parent, width=100)
        self.apellido_label.place(x=0, y=25)
        self.apellido_entry.place(x=100, y=25)

        self.telefono_label = Tkinter.Label(
            self.parent,
            text="Telefono:",
            bg="lavender",
        )
        self.telefono_entry = Tkinter.Entry(self.parent, width=100)
        self.telefono_label.place(x=0, y=50)
        self.telefono_entry.place(x=100, y=50)

        self.direccion_label = Tkinter.Label(
            self.parent,
            text="Direccion:",
            bg="lavender",
        )
        self.direccion_entry = Tkinter.Entry(self.parent, width=100)
        self.direccion_label.place(x=0, y=75)
        self.direccion_entry.place(x=100, y=75)

        self.marca_label = Tkinter.Label(
            self.parent,
            text="Marca:",
            bg="lavender",
        )
        self.marca_entry = Tkinter.Entry(self.parent, width=100)
        self.marca_label.place(x=0, y=100)
        self.marca_entry.place(x=100, y=100)

        self.modelo_label = Tkinter.Label(
            self.parent,
            text="Modelo:",
            bg="lavender",
        )
        self.modelo_entry = Tkinter.Entry(self.parent, width=100)
        self.modelo_label.place(x=0, y=125)
        self.modelo_entry.place(x=100, y=125)

        self.falla_label = Tkinter.Label(
            self.parent,
            text="Falla:",
            bg="lavender",
        )
        self.falla_entry = Tkinter.Entry(self.parent, width=100)
        self.falla_label.place(x=0, y=150)
        self.falla_entry.place(x=100, y=150)

        self.otros_label = Tkinter.Label(
            self.parent,
            text="Otros:",
            bg="lavender",
        )
        self.otros_entry = Tkinter.Entry(self.parent, width=100)
        self.otros_label.place(x=0, y=175)
        self.otros_entry.place(x=100, y=175)
        # Boton insertar
        self.submit_button = Tkinter.Button(
            self.parent, text="Insertar", command=self.insert_data
        )
        # Esto es para el enter
        self.submit_button.bind("<Return>", self.insert_data)
        self.submit_button.place(x=930, y=0)
        # Boton Buscar en db
        self.search_button = Tkinter.Button(
            self.parent, text="Buscar", command=self.search_data
        )
        # Esto es para el enter
        self.search_button.bind("<Return>", self.search_data)
        self.search_button.place(x=935, y=55)
        # Boton editar db
        self.edit_button = Tkinter.Button(
            self.parent, text="Editar", command=self.edit_data
        )
        # Esto es para el enter
        self.edit_button.bind("<Return>", self.edit_data)
        self.edit_button.place(x=939, y=110)
        # Boton generar boleta
        self.print_button = Tkinter.Button(
            self.parent, text="Generar", command=self.print_data1
        )
        # Esto es para el enter
        self.print_button.bind("<Return>", self.print_data1)
        self.print_button.place(x=930, y=165)

        # Treeview
        self.tree = ttk.Treeview(
            self.parent,
            columns=(
                "Fecha",
                "Nombre",
                "Apellido",
                "Telefono",
                "Direccion",
                "Marca",
                "Modelo",
                "Falla",
                "Otros",
            ),
        )
        self.tree.heading("#0", text="Orden")
        self.tree.heading("#1", text="Fecha")
        self.tree.heading("#2", text="Nombre")
        self.tree.heading("#3", text="Apellido")
        self.tree.heading("#4", text="Telefono")
        self.tree.heading("#5", text="Direccion")
        self.tree.heading("#6", text="Marca")
        self.tree.heading("#7", text="Modelo")
        self.tree.heading("#8", text="Falla")
        self.tree.heading("#9", text="Otros")
        self.tree.column("#0", stretch=Tkinter.YES, width=70)
        self.tree.column("#1", stretch=Tkinter.YES, width=87)
        self.tree.column("#2", stretch=Tkinter.YES, width=110)
        self.tree.column("#3", stretch=Tkinter.YES, width=110)
        self.tree.column("#4", stretch=Tkinter.YES, width=100)
        self.tree.column("#5", stretch=Tkinter.YES, width=100)
        self.tree.column("#6", stretch=Tkinter.YES, width=90)
        self.tree.column("#7", stretch=Tkinter.YES, width=90)
        self.tree.column("#8", stretch=Tkinter.YES, width=120)
        self.tree.column("#9", stretch=Tkinter.YES, width=150)

        self.tree.place(x=9, y=220)
        self.treeview = self.tree
        self.ver_data()

    # Insertar los datos de la base en el treeview
    def ver_data(self):
        resultado = BaseDatos.select()
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        for fila in resultado:
            self.tree.insert(
                "",
                0,
                text=str(fila.orden).zfill(5),
                values=(
                    fila.fecha,
                    fila.nombre,
                    fila.apellido,
                    fila.telefono,
                    fila.direccion,
                    fila.marca,
                    fila.modelo,
                    fila.falla,
                    fila.otros,
                ),
            )

    def insert_data(self, *argus):
        # Verifica que los campos no esten vacios.
        namae = self.valid.vali(self.nombre_entry.get())
        myooji = self.valid.vali(self.apellido_entry.get())
        denwa = self.valid.vali(self.telefono_entry.get())
        hookoo = self.valid.vali(self.direccion_entry.get())
        burando = self.valid.vali(self.marca_entry.get())
        moderu = self.valid.vali(self.modelo_entry.get())
        shippai = self.valid.vali(self.falla_entry.get())
        sonohoka = self.valid.vali(self.otros_entry.get())
        if not namae or not myooji or not denwa or not burando:
            messagebox.showinfo(
                title="Campos incompletos",
                message="Debe completar todos los campos.",
            )
        elif not hookoo or not moderu or not shippai or not sonohoka:
            messagebox.showinfo(
                title="Campos incompletos",
                message="Debe completar todos los campos.",
            )
        else:
            # Guardo los datos
            guard = BaseDatos()
            guard.guardar(
                self.nombre_entry.get(),
                self.apellido_entry.get(),
                self.telefono_entry.get(),
                self.direccion_entry.get(),
                self.marca_entry.get(),
                self.modelo_entry.get(),
                self.falla_entry.get(),
                self.otros_entry.get(),
            )
            self.print_data2()
            # Limpia los campos del entry
            self.nombre_entry.delete(0, Tkinter.END)
            self.apellido_entry.delete(0, Tkinter.END)
            self.telefono_entry.delete(0, Tkinter.END)
            self.direccion_entry.delete(0, Tkinter.END)
            self.marca_entry.delete(0, Tkinter.END)
            self.modelo_entry.delete(0, Tkinter.END)
            self.falla_entry.delete(0, Tkinter.END)
            self.otros_entry.delete(0, Tkinter.END)
            # Imprimo los datos
            self.ver_data()

    def edit_data(self, *argus):
        estado()

    def search_data(self, *argus):
        busqueda()

    def print_data1(self, *argus):
        re_boleta()

    def print_data2(self, *argus):
        # Creamos una lista, guardamos los datos y se los mandamos
        # a boleta para generar el pdf
        mi_lisu = []
        orde = BaseDatos.select().order_by(BaseDatos.orden.desc()).get()
        mi_lisu.append(str(orde).zfill(5))
        mi_lisu.append(
            str(self.nombre_entry.get() + " " + self.apellido_entry.get()),
        )
        mi_lisu.append(str(self.direccion_entry.get()))
        mi_lisu.append(str(self.telefono_entry.get()))
        mi_lisu.append(str(self.marca_entry.get()))
        mi_lisu.append(str(self.modelo_entry.get()))
        mi_lisu.append(str(self.falla_entry.get()))
        mi_lisu.append(str(self.otros_entry.get()))
        boleta(mi_lisu)
        bole = messagebox.askyesno(message="¿Imprimir boleta?", title="Boleta")
        if bole:
            # Mandamos el numero de orden a imprimir
            imprimir(str(orde).zfill(5))


if __name__ == "__main__":
    root = Tkinter.Tk()
    MiVistas(root)
    root.mainloop()
