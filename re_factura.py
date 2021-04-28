from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Toplevel
from base import BaseDatos
from factura import boleta


contador = True


def re_boleta():

    toor = Toplevel()  # Creamos una ventana
    toor.title("Generar boleta")  # Titulo de la ventana
    toor.geometry("280x100")  # Tamaño de la ventana
    toor.resizable(False, False)  # Impide redimensiones de la ventana
    mi_lista = []

    def valor_boton(*args):
        global contador
        valor = entra.get()
        verifica = BaseDatos.select().where(BaseDatos.orden == valor)
        if verifica.exists():
            if contador:
                # Negamos la variable contador para no volver
                # a reimprimir la boleta
                contador = not contador
                # Agregamos todos los valores a la lista
                mi_lista.append(valor.zfill(5))
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).nombre)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).apellido)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).direccion)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).telefono)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).marca)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).modelo)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).falla)
                mi_lista.append(BaseDatos.get(BaseDatos.orden == valor).otros)
                boleta(mi_lista)
                texto_abajo = Label(toor, text="Boleta generada")
                texto_abajo.place(x=10, y=60)
            else:
                texto_abajo = Label(toor, text="Boleta ya generada")
                texto_abajo.place(x=10, y=60)
        else:
            texto_abajo = Label(toor, text="Numero de orden no encontrado")
            texto_abajo.place(x=10, y=60)

    texto = Label(toor, text="Volver a generar boleta de orden N°:")
    texto.place(x=10, y=0)
    entra = Entry(toor, width=10, bd=3)
    entra.place(x=10, y=30)
    boton = Button(toor, text="Generar", command=valor_boton)
    boton.place(x=155, y=30)
    boton.bind("<Return>", valor_boton)  # Esto es para el enter

    toor.mainloop()
