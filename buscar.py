from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import IntVar
from tkinter import Button
from tkinter import Listbox
from tkinter import Toplevel
from tkinter import Scrollbar
from tkinter import StringVar
from tkinter import Radiobutton
from base import BaseDatos


def busqueda():

    toor = Toplevel()  # Creamos una ventana
    toor.title("Busqueda")  # Titulo de la ventana
    toor.geometry("425x420")  # Tamaño de la ventana
    toor.resizable(False, False)
    parame = []
    numoer = IntVar()
    totales = StringVar()

    def valor_boton(*argus):
        nume = numoer.get()

        if nume == 1:
            lisbo.delete(0, "end")
            vali = entra.get()
            if vali.isdigit():
                bus_ord()
            else:
                lisbo.delete(0, "end")
                lisbo.insert(0, "Ingrese un numero de orden")
                totales.set("Encontrados: 0")
        elif nume == 2:
            lisbo.delete(0, "end")
            busqueda_g("apellido")
        elif nume == 3:
            vali = entra.get()
            if vali.isdigit():
                lisbo.delete(0, "end")
                busqueda_g("telefono")
            else:
                lisbo.delete(0, "end")
                lisbo.insert(0, "Ingrese un numero de telefono")
                totales.set("Encontrados: 0")
        elif nume == 4:
            lisbo.delete(0, "end")
            busqueda_g("tipo")
        elif nume == 5:
            lisbo.delete(0, "end")
            busqueda_g("marca")
        else:
            lisbo.delete(0, "end")
            lisbo.insert(0, "Seleccione una opcion")
            totales.set("Encontrados: 0")

    def busqueda_g(parametro):
        lisbo.delete(0, "end")
        parame.clear()
        cadena = entra.get()
        namae = str(BaseDatos.select().order_by(BaseDatos.orden.desc()).get())
        if not cadena:
            lisbo.delete(0, "end")
            lisbo.insert(0, "Seleccione una opcion")

        else:
            for i in range(1, int(namae) + 1):
                if parametro == "apellido":
                    verili = BaseDatos.get(BaseDatos.orden == i).apellido
                elif parametro == "telefono":
                    verili = BaseDatos.get(BaseDatos.orden == i).telefono
                elif parametro == "tipo":
                    verili = BaseDatos.get(BaseDatos.orden == i).tipo
                elif parametro == "marca":
                    verili = BaseDatos.get(BaseDatos.orden == i).marca
                else:
                    lisbo.delete(0, "end")
                    lisbo.insert(0, "Seleccione una opcion")

                if cadena in verili:
                    parame.append("---------------------------")
                    parame.append(
                        "Otros: " + BaseDatos.get(BaseDatos.orden == i).otros,
                    )
                    parame.append(
                        "Falla: " + BaseDatos.get(BaseDatos.orden == i).falla,
                    )
                    parame.append(
                        "Modelo: " + BaseDatos.get(BaseDatos.orden == i).modelo,
                    )
                    parame.append(
                        "Marca: " + BaseDatos.get(BaseDatos.orden == i).marca,
                    )
                    parame.append(
                        "Tipo: " + BaseDatos.get(BaseDatos.orden == i).tipo,
                    )
                    parame.append(
                        "Direccion: " + BaseDatos.get(BaseDatos.orden == i).direccion
                    )
                    parame.append(
                        "Telefono: " + BaseDatos.get(BaseDatos.orden == i).telefono,
                    )
                    parame.append(
                        "Apellido: " + BaseDatos.get(BaseDatos.orden == i).apellido,
                    )
                    parame.append(
                        "Nombre: " + BaseDatos.get(BaseDatos.orden == i).nombre,
                    )
                    parame.append(
                        "Fecha: " + str(BaseDatos.get(BaseDatos.orden == i).fecha),
                    )
                    parame.append("N° de Orden: " + str(i))

            totales.set("Encontrados: " + str(len(parame) // 12))

            for item in parame:  # Insertamos los items en un Listbox
                lisbo.insert(0, item)

    # valididar que el dato ingresado sea un numero y no este vacio
    def bus_ord(*argo):
        lisbo.delete(0, "end")
        vali = entra.get()
        if vali.isdigit():
            lisbo.delete(0, "end")
            veri = entra.get()
            veril = BaseDatos.select().where(BaseDatos.orden == veri)
            if veril.exists():
                insertar()
            else:
                lisbo.insert(0, "Orden de reparacion")
                lisbo.insert(1, " no encotrada.")
                totales.set("Encontrados: 0")
        else:
            lisbo.delete(0, "end")
            lisbo.insert(0, "Ingrese un numero")

    # creamos la lista y la insertamos en el listbox
    def insertar():
        lisbo.delete(0, "end")
        parame.clear()
        cadena = entra.get()
        # Agregamos los elementos a la lista
        parame.append(
            "Otros: " + BaseDatos.get(BaseDatos.orden == cadena).otros,
        )
        parame.append(
            "Falla: " + BaseDatos.get(BaseDatos.orden == cadena).falla,
        )
        parame.append(
            "Modelo: " + BaseDatos.get(BaseDatos.orden == cadena).modelo,
        )
        parame.append(
            "Marca: " + BaseDatos.get(BaseDatos.orden == cadena).marca,
        )
        parame.append(
            "Tipo: " + BaseDatos.get(BaseDatos.orden == cadena).tipo,
        )
        parame.append(
            "Direccion: " + BaseDatos.get(BaseDatos.orden == cadena).direccion
        )
        parame.append(
            "Telefono: " + BaseDatos.get(BaseDatos.orden == cadena).telefono,
        )
        parame.append(
            "Apellido: " + BaseDatos.get(BaseDatos.orden == cadena).apellido,
        )
        parame.append(
            "Nombre: " + BaseDatos.get(BaseDatos.orden == cadena).nombre,
        )
        parame.append(
            "Fecha: " + str(BaseDatos.get(BaseDatos.orden == cadena).fecha),
        )
        parame.append("N° de Orden: " + str(cadena))

        for item in parame:  # Insertamos los items en un Listbox
            lisbo.insert(0, item)

        totales.set("Encontrados: 1")

    # posicionamiento de los widget de tkinter
    frame1 = Frame(toor)
    frame1.place(x=0, y=0)
    frame2 = Frame(toor)
    frame2.place(x=0, y=120)
    texto = Label(frame1, text="Buscar por:")
    texto.grid(row=0, column=2)
    busq1 = Radiobutton(frame1, text="Orden", value=1, variable=numoer)
    busq1.grid(row=1, column=0)
    busq2 = Radiobutton(frame1, text="Apellido", value=2, variable=numoer)
    busq2.grid(row=1, column=1)
    busq3 = Radiobutton(frame1, text="Telefono", value=3, variable=numoer)
    busq3.grid(row=1, column=2)
    busq4 = Radiobutton(frame1, text="Tipo", value=4, variable=numoer)
    busq4.grid(row=1, column=3)
    busq5 = Radiobutton(frame1, text="Marca", value=5, variable=numoer)
    busq5.grid(row=1, column=4)
    entra = Entry(frame1, width=10, bd=3)
    entra.grid(row=2, column=1)
    boton = Button(frame1, text="Aceptar", command=valor_boton)
    boton.grid(row=2, column=2)
    boton.bind("<Return>", valor_boton)  # Esto es para el enter
    result = Label(frame1, textvariable=totales)
    result.grid(row=3, column=1)
    tree_scroll = Scrollbar(frame2)
    tree_scroll.pack(side="right", fill="y")
    lisbo = Listbox(
        frame2,
        borderwidth=5,
        width=50,
        height=15,
        yscrollcommand=tree_scroll.set,
    )
    lisbo.pack()
    tree_scroll.config(command=lisbo.yview)

    toor.mainloop()
