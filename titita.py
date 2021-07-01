from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import PhotoImage
from tkinter import LabelFrame
from tkinter import messagebox
from tkinter import Frame
from tkinter import Label
from tkinter import Scrollbar
from tkinter import Spinbox
from validar_campos import Validacion
from configurar import configuracion
from buscar import busqueda
from prints import imprimir
from base import BaseDatos
from factura import boleta
import tkinter.ttk as ttk
import sys
import os


sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)


class MiVistas(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.saliendo)
        self.vivista()
        self.valid = Validacion()

    def vivista(self):
        # Titulo
        self.parent.title("Titita")
        # Tamaño y pocision de la ventana
        self.parent.geometry("1050x480+100+100")
        # Redimensionable
        self.parent.resizable(False, False)
        # Color de fondo
        self.parent.config(background="lavender")
        #  Elegimos el icono del programa en base al OS
        if sistema == "linux":
            logo = PhotoImage(file=ruta2[0] + "/imagenes/titita.gif")
            self.parent.call("wm", "iconphoto", self.parent._w, logo)
        else:
            self.parent.iconbitmap(ruta2[0] + "\\imagenes\\titita.ico")

        #######################################################################
        # Define los distintos widgets

        # Frame de los entry
        entry_frame = LabelFrame(
            self.parent,
            text="Datos del cliente y el aparato",
            bg="lavender",
        )
        entry_frame.place(x=10, y=0)

        # Frame de los entry2
        entry2_frame = LabelFrame(
            self.parent,
            text="Datos sobre la reparacion",
            bg="lavender",
        )
        entry2_frame.place(x=550, y=0)

        # Frame de los botones
        button_frame = LabelFrame(self.parent, text="Comandos", bg="lavender")
        button_frame.place(x=920, y=0)

        # Frame del treeview
        tree_frame = Frame(self.parent)
        tree_frame.place(x=9, y=245)

        #######################################################################
        # Labels y Entrys
        self.nombre_label = Label(
            entry_frame,
            text="Nombre: ",
            bg="lavender",
        )
        self.nombre_entry = Entry(entry_frame, width=50)
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry.grid(row=0, column=1)

        self.apellido_label = Label(
            entry_frame,
            text="Apellido: ",
            bg="lavender",
        )
        self.apellido_entry = Entry(entry_frame, width=50)
        self.apellido_label.grid(row=1, column=0)
        self.apellido_entry.grid(row=1, column=1)

        self.telefono_label = Label(
            entry_frame,
            text="Telefono: ",
            bg="lavender",
        )
        self.telefono_entry = Entry(entry_frame, width=50)
        self.telefono_label.grid(row=2, column=0)
        self.telefono_entry.grid(row=2, column=1)

        self.direccion_label = Label(
            entry_frame,
            text="Direccion:",
            bg="lavender",
        )
        self.direccion_entry = Entry(entry_frame, width=50)
        self.direccion_label.grid(row=3, column=0)
        self.direccion_entry.grid(row=3, column=1)

        self.tipo_label = Label(
            entry_frame,
            text="Tipo:",
            bg="lavender",
        )
        self.tipo_spinbox = Spinbox(
            entry_frame,
            width=48,
            values=(
                "",
                "Amplificador",
                "Auricular",
                "Auto estereo",
                "Decodificador",
                "Camara",
                "Celular",
                "Centro Musical",
                "Consola de video juegos",
                "Consola portatil",
                "Estabilizador de tension",
                "Fuente de alimentacion",
                "Fuente inversora",
                "Impresora",
                "Mixer",
                "Monitor",
                "Netbook",
                "Notebook",
                "Parlante Bluetooth",
                "PC",
                "Potencia de audio",
                "Radio",
                "Reproductor de DVD",
                "Tablet",
                "Teclado",
                "Teclado musical",
                "Tv",
                "UPS",
                "Otro",
            ),
        )
        self.tipo_label.grid(row=4, column=0)
        self.tipo_spinbox.grid(row=4, column=1, sticky="w")

        self.marca_label = Label(
            entry_frame,
            text="Marca: ",
            bg="lavender",
        )
        self.marca_entry = Entry(entry_frame, width=50)
        self.marca_label.grid(row=5, column=0)
        self.marca_entry.grid(row=5, column=1)

        self.modelo_label = Label(
            entry_frame,
            text="Modelo:",
            bg="lavender",
        )
        self.modelo_entry = Entry(entry_frame, width=50)
        self.modelo_label.grid(row=6, column=0)
        self.modelo_entry.grid(row=6, column=1)

        self.falla_label = Label(
            entry_frame,
            text="Falla: ",
            bg="lavender",
        )
        self.falla_entry = Entry(entry_frame, width=50)
        self.falla_label.grid(row=7, column=0)
        self.falla_entry.grid(row=7, column=1)

        self.otros_label = Label(
            entry_frame,
            text="Otros:",
            bg="lavender",
        )
        self.otros_entry = Entry(entry_frame, width=50)
        self.otros_label.grid(row=8, column=0, pady=5)
        self.otros_entry.grid(row=8, column=1, pady=5)

        ##################################################################

        self.estado_spin = Spinbox(
            entry2_frame,
            values=("En reparacion", "Presupuestado", "Entrgado"),
        )
        self.estado_label = Label(
            entry2_frame,
            text="Estado",
            bg="lavender",
        )
        self.estado_spin.grid(row=0, column=1, sticky="w")
        self.estado_label.grid(row=0, column=0, sticky="w")

        self.costo_label = Label(
            entry2_frame,
            text="Costos",
            bg="lavender",
        )
        self.costo_entry = Entry(entry2_frame, width=30)
        self.costo_label.grid(row=1, column=0, pady=10, sticky="w")
        self.costo_entry.grid(row=1, column=1, pady=10, sticky="w")

        self.total_label = Label(
            entry2_frame,
            text="Total",
            bg="lavender",
        )
        self.total_entry = Entry(entry2_frame, width=30)
        self.total_label.grid(row=2, column=0, pady=10, sticky="w")
        self.total_entry.grid(row=2, column=1, pady=10, sticky="w")

        self.descripcion_label = Label(
            entry2_frame,
            text="Descripcion",
            bg="lavender",
        )
        self.descripcion_entry = Entry(entry2_frame, width=30)
        self.descripcion_label.grid(row=3, column=0, pady=10, sticky="w")
        self.descripcion_entry.grid(row=3, column=1, pady=10, sticky="w")

        self.notificacion_spin = Spinbox(
            entry2_frame,
            width=5,
            values=("No", "Si"),
        )
        self.notificacion_label = Label(
            entry2_frame,
            text="Se notifico",
            bg="lavender",
        )
        self.notificacion_spin.grid(row=4, column=1, sticky="w")
        self.notificacion_label.grid(row=4, column=0, sticky="w")

        #######################################################################
        # Buttons
        # Boton insertar
        self.submit_button = Button(
            button_frame, text="Guardar", command=self.insert_data
        )
        # Esto es para el enter
        self.submit_button.bind("<Return>", self.insert_data)
        self.submit_button.grid(row=0, column=0)

        # Boton Buscar en db
        self.search_button = Button(
            button_frame, text="Buscar", command=self.search_data
        )
        # Esto es para el enter
        self.search_button.bind("<Return>", self.search_data)
        self.search_button.grid(row=1, column=0, padx=10, pady=10)

        # Boton de borrado de campos
        self.rm_button = Button(
            button_frame,
            text="Borrar",
            command=self.rm_data,
        )
        # Esto es para el enter
        self.rm_button.bind("<Return>", self.rm_data)
        self.rm_button.grid(row=2, column=0, padx=10, pady=10)

        # Boton de configuraciones
        self.config_button = Button(
            button_frame, text="Configurar", command=self.config_data
        )
        # Esto es para el enter
        self.config_button.bind("<Return>", self.config_data)
        self.config_button.grid(row=3, column=0)

        ##########################
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        #######################################################################

        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            columns=(
                "Fecha",
                "Nombre",
                "Apellido",
                "Telefono",
                "Direccion",
                "Tipo",
                "Marca",
                "Modelo",
                "Falla",
                "Otros",
            ),
        )
        tree_scroll.config(command=self.tree.yview)
        self.tree.heading("#0", text="Orden")
        self.tree.heading("#1", text="Fecha")
        self.tree.heading("#2", text="Nombre")
        self.tree.heading("#3", text="Apellido")
        self.tree.heading("#4", text="Telefono")
        self.tree.heading("#5", text="Direccion")
        self.tree.heading("#6", text="Tipo")
        self.tree.heading("#7", text="Marca")
        self.tree.heading("#8", text="Modelo")
        self.tree.heading("#9", text="Falla")
        self.tree.heading("#10", text="Otros")
        self.tree.column("#0", stretch="YES", width=70)
        self.tree.column("#1", stretch="YES", width=87)
        self.tree.column("#2", stretch="YES", width=110)
        self.tree.column("#3", stretch="YES", width=110)
        self.tree.column("#4", stretch="YES", width=100)
        self.tree.column("#5", stretch="YES", width=100)
        self.tree.column("#6", stretch="YES", width=80)
        self.tree.column("#7", stretch="YES", width=80)
        self.tree.column("#8", stretch="YES", width=90)
        self.tree.column("#9", stretch="YES", width=100)
        self.tree.column("#10", stretch="YES", width=90)

        self.tree.pack()
        # Esto es para seleccionar con el click
        self.tree.bind("<ButtonRelease-1>", self.select_data)
        self.treeview = self.tree
        self.ver_data()

    # Esta funcion se encarga de borrar los datos de la pantalla del treeview
    def rm_data(self):
        self.nombre_entry.delete(0, "end")
        self.apellido_entry.delete(0, "end")
        self.telefono_entry.delete(0, "end")
        self.direccion_entry.delete(0, "end")
        self.tipo_spinbox.delete(0, "end")
        self.marca_entry.delete(0, "end")
        self.modelo_entry.delete(0, "end")
        self.falla_entry.delete(0, "end")
        self.otros_entry.delete(0, "end")
        self.estado_spin.delete(0, "end")
        self.costo_entry.delete(0, "end")
        self.total_entry.delete(0, "end")
        self.descripcion_entry.delete(0, "end")
        self.notificacion_spin.delete(0, "end")

    # Esta funcion se encarga de insertar los datos de la base en el treeview
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
                    fila.tipo,
                    fila.marca,
                    fila.modelo,
                    fila.falla,
                    fila.otros,
                    fila.estado,
                    fila.costo,
                    fila.total,
                    fila.descripcion,
                    fila.notificacion,
                    fila.orden,
                ),
            )

    #  Esta funcion se encarga de guardar los datos y de actualizarlos
    def insert_data(self, *argus):
        # Verifica que los campos no esten vacios.
        seleccionad = self.tree.focus()
        # Toma los items del campo seleccionado del treeview
        valore = self.tree.item(seleccionad, "values")
        try:
            # Controlo que el campo del nombre este completo antes de continuar
            namae = self.valid.vali(self.nombre_entry.get())
            if not namae:
                messagebox.showinfo(
                    title="Campos incompletos",
                    message="Debe completar el nombre como minimo.",
                )
            else:
                # Acutualizo la base de datos
                print("Orden:", valore[15], "actualizada")
                actualizar = BaseDatos.update(
                    nombre=self.nombre_entry.get(),
                    apellido=self.apellido_entry.get(),
                    telefono=self.telefono_entry.get(),
                    direccion=self.direccion_entry.get(),
                    tipo=self.tipo_spinbox.get(),
                    marca=self.marca_entry.get(),
                    modelo=self.modelo_entry.get(),
                    falla=self.falla_entry.get(),
                    otros=self.otros_entry.get(),
                    estado=self.estado_spin.get(),
                    costo=self.costo_entry.get(),
                    total=self.total_entry.get(),
                    descripcion=self.descripcion_entry.get(),
                    notificacion=self.notificacion_spin.get(),
                ).where(BaseDatos.orden == valore[15])
                actualizar.execute()
                # Limpia los campos del entry
                self.rm_data()
                # Imprimo por pantalla los datos
                self.ver_data()
        except:
            # Controlo que el campo del nombre este completo antes de continuar
            namae = self.valid.vali(self.nombre_entry.get())
            if not namae:
                messagebox.showinfo(
                    title="Campos incompletos",
                    message="Debe completar el nombre como minimo.",
                )
            else:
                # Guardo los datos en la base de datos
                guard = BaseDatos()
                guard.guardar(
                    self.nombre_entry.get(),
                    self.apellido_entry.get(),
                    self.telefono_entry.get(),
                    self.direccion_entry.get(),
                    self.tipo_spinbox.get(),
                    self.marca_entry.get(),
                    self.modelo_entry.get(),
                    self.falla_entry.get(),
                    self.otros_entry.get(),
                    self.estado_spin.get(),
                    self.costo_entry.get(),
                    self.total_entry.get(),
                    self.descripcion_entry.get(),
                    self.notificacion_spin.get(),
                )
                # Mando a imprimir los datos
                self.print_data2()
                # Limpia los campos del entry
                self.rm_data()
                # Imprimo por pantalla los datos
                self.ver_data()

    #  Esta funcion se encarga de hacer la busqueda en nuestra base de datos
    def search_data(self, *argus):
        busqueda()

    #  Esta funcion se encarga de mandar los datos a imprimir
    def print_data2(self, *argus):
        # Creamos una lista, guardamos los datos y se los mandamos
        # a factura.py para generar el pdf
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
        mi_lisu.append(str(self.tipo_spinbox.get()))
        boleta(mi_lisu)
        bole = messagebox.askyesno(message="¿Imprimir boleta?", title="Boleta")
        if bole:
            # Mandamos el numero de orden a imprimir
            imprimir(str(orde).zfill(5))

    #  Esta funcion se encarga de la configuracion
    def config_data(self, *argus):
        configuracion()

    #  Esta funcion se encarga de cargar el valor seleccionado en el treeview
    def select_data(self, *argus):
        # Borro todos los campos
        self.rm_data()
        # Selecciona la fila del treeview
        seleccionado = self.tree.focus()
        # Toma los items del campo seleccionado del treeview
        valores = self.tree.item(seleccionado, "values")
        # Inserta los valores en los campos
        self.nombre_entry.insert(0, valores[1])
        self.apellido_entry.insert(0, valores[2])
        self.telefono_entry.insert(0, valores[3])
        self.direccion_entry.insert(0, valores[4])
        self.tipo_spinbox.insert(0, valores[5])
        self.marca_entry.insert(0, valores[6])
        self.modelo_entry.insert(0, valores[7])
        self.falla_entry.insert(0, valores[8])
        self.otros_entry.insert(0, valores[9])
        self.estado_spin.insert(0, valores[10])
        self.costo_entry.insert(0, valores[11])
        self.total_entry.insert(0, valores[12])
        self.descripcion_entry.insert(0, valores[13])
        self.notificacion_spin.insert(0, valores[14])

    #  Esta funcion se ejecuta al cerrar la ventada
    def saliendo(self):
        self.parent.quit()
        self.parent.destroy()
        print("Saliendo del programa")


if __name__ == "__main__":
    root = Tk()
    MiVistas(root)
    root.mainloop()
