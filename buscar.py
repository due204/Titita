from tkinter import Label
from tkinter import Entry
from tkinter import IntVar
from tkinter import Button
from tkinter import Listbox
from tkinter import Toplevel
from tkinter import Radiobutton
from base import BaseDatos


def busqueda():

    toor = Toplevel()  # Creamos una ventana
    toor.title("Busqueda")  # Titulo de la ventana
    toor.geometry("425x420")  # Tamaño de la ventana
    parame = []
    numoer = IntVar()

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
        elif nume == 4:
            lisbo.delete(0, "end")
            busqueda_g("marca")
        else:
            lisbo.delete(0, "end")
            lisbo.insert(0, "Seleccione una opcion")

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

    # posicionamiento de los widget de tkinter
    texto = Label(toor, text="Buscar por:")
    texto.place(x=10, y=0)
    busq1 = Radiobutton(toor, text="Orden", value=1, variable=numoer)
    busq1.place(x=0, y=25)
    busq2 = Radiobutton(toor, text="Apellido", value=2, variable=numoer)
    busq2.place(x=70, y=25)
    busq3 = Radiobutton(toor, text="Telefono", value=3, variable=numoer)
    busq3.place(x=155, y=25)
    busq4 = Radiobutton(toor, text="Marca", value=4, variable=numoer)
    busq4.place(x=250, y=25)
    entra = Entry(toor, width=10, bd=3)
    entra.place(x=150, y=50)
    boton = Button(toor, text="Aceptar", command=valor_boton)
    boton.place(x=155, y=80)
    boton.bind("<Return>", valor_boton)  # Esto es para el enter
    lisbo = Listbox(toor, borderwidth=5, width=50, height=15)
    lisbo.place(x=5, y=120)

    toor.mainloop()
