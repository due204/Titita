from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import Checkbutton
from tkinter import filedialog
import os
import sys

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)
archivo = ruta2[0] + "/config"

textedu = """Por correccion de errores, dudas o sugerencias no duden en
contactarme al mail: due204@gmail.com"""


def configuracion():
    def lectura():
        #  Lectura del archivo de configuracion
        a = open(archivo, "r")
        dato = a.readlines()
        return dato
        a.close()

    def guardar_datos():
        #  Guardamos los datos en el archico de configuracion
        a = open(archivo, "w")
        a.write("ruta_boleta:" + ruta.get() + "\n")
        a.write("nombre_1:" + nombre1.get() + "\n")
        a.write("nombre_2:" + nombre2.get() + "\n")
        a.write("direccion_1:" + direccion1.get() + "\n")
        a.write("direccion_2:" + direccion2.get() + "\n")
        a.write("celular_1:" + telefono.get() + "\n")
        a.write("navegadoor_1:" + navegador.get() + "\n")
        a.close()
        toor.quit()
        toor.destroy()

    def guradar_ruta():
        # Seleccionamos el directorio
        directorio = filedialog.askdirectory()
        if directorio:
            print(directorio)
            # Seteamos el directiorio
            ruta.set(directorio)

    toor = Toplevel()  # Creamos una ventana
    toor.title("Configurar Titita")  # Titulo de la ventana
    toor.geometry("425x500")  # Tamaño de la ventana
    toor.resizable(False, False)  # Evitamos modificar la ventana

    # Variables
    ruta = StringVar()
    nombre1 = StringVar()
    nombre2 = StringVar()
    direccion1 = StringVar()
    direccion2 = StringVar()
    telefono = StringVar()
    navegador = StringVar()

    # Seateamos las variables
    atur = lectura()

    atur0 = atur[0].lstrip("ruta_boleta:").rstrip("\n")
    atur1 = atur[1].lstrip("nombre_1:").rstrip("\n")
    atur2 = atur[2].lstrip("nombre_2:").rstrip("\n")
    atur3 = atur[3].lstrip("direccion_1:").rstrip("\n")
    atur4 = atur[4].lstrip("direccion_2:").rstrip("\n")
    atur5 = atur[5].lstrip("celular_1:").rstrip("\n")
    atur6 = atur[6].lstrip("navegadorr_1:").rstrip("\n")
    ruta.set(atur0)
    nombre1.set(atur1)
    nombre2.set(atur2)
    direccion1.set(atur3)
    direccion2.set(atur4)
    telefono.set(atur5)
    navegador.set(atur6)

    texto_a = Label(toor, text="Configurar la ruta de las boletas en pdf")
    texto_a.place(x=50, y=0)

    entrada0 = Entry(toor, width=37, textvariable=ruta)
    entrada0.place(x=10, y=40)
    boton0 = Button(toor, text="Seleccionar", command=guradar_ruta)
    boton0.bind("<Return>", guradar_ruta)  # Esto es para el enter
    boton0.place(x=315, y=37)

    texto_b = Label(toor, text="Configuracion de la boleta generada en pdf")
    texto_b.place(x=50, y=80)

    texto1 = Label(toor, text="Nombre 1 de la orden: ")
    texto1.place(x=10, y=120)
    entrada1 = Entry(toor, width=30, textvariable=nombre1)
    entrada1.place(x=165, y=120)

    texto2 = Label(toor, text="Nombre 2 de la orden: ")
    texto2.place(x=10, y=160)
    entrada2 = Entry(toor, width=30, textvariable=nombre2)
    entrada2.place(x=165, y=160)

    texto3 = Label(toor, text="Direccion 1 de la orden")
    texto3.place(x=10, y=200)
    entrada3 = Entry(toor, width=30, textvariable=direccion1)
    entrada3.place(x=165, y=200)

    texto4 = Label(toor, text="Direccion 2 de la orden")
    texto4.place(x=10, y=240)
    entrada4 = Entry(toor, width=30, textvariable=direccion2)
    entrada4.place(x=165, y=240)

    texto5 = Label(toor, text="Numero de telefono")
    texto5.place(x=10, y=280)
    entrada5 = Entry(toor, width=30, textvariable=telefono)
    entrada5.place(x=165, y=280)

    pdfs = Checkbutton(
        toor,
        text="Abrir pdfs en el navegador",
        variable=navegador,
    )
    pdfs.place(x=0, y=310)

    boton1 = Button(toor, text="Guardar", command=guardar_datos)
    boton1.bind("<Return>", guardar_datos)  # Esto es para el enter
    boton1.place(x=330, y=310)

    texto6 = Label(toor, text=textedu)
    texto6.place(x=10, y=380)

    toor.mainloop()
