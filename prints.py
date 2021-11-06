import webbrowser
from tkinter import messagebox
from os import path
from os import system
from sys import platform

sistema = platform
ruta1 = path.abspath(__file__)
ruta2 = path.split(ruta1)
archivo = ruta2[0] + "/config"

a = open(archivo, "r")
dato = a.readlines()
ruta3 = dato[0].lstrip("ruta_boleta:").rstrip("\n")
naveg = dato[6].lstrip("navegador_1:").rstrip("\n")
a.close()


def imprimir(argu):
    # Determina en que OS estamos trabajando
    # Si estamos en GNU/Linux
    ####################################################################
    if sistema == "linux":
        if not ruta3:
            # Si no se a especificado la ruta se utiliza la default
            ruta = ruta2[0] + "/Boletas/Orden" + argu + ".pdf"
        else:
            ruta = ruta3 + "/Orden" + argu + ".pdf"
        # Preguntamos si queremos imprimir el pdf
        bole = messagebox.askyesno(message="¿Imprimir boleta?", title="Boleta")
        if bole:
            # Comando GNU/Linux para la impresion
            # Necesita tener cups instalado en su sistema
            # Y configurado su impresora a traves de cups
            ruta_l = "lp -o media=A4" + " " + ruta
            system(ruta_l)
        # Abrimos el pdf en el navegador
        if not naveg:
            webbrowser.open(ruta, new=2, autoraise=True)

    # Si estamos en Windows
    ####################################################################
    elif sistema == "win32" or "win64":
        from win32api import ShellExecute

        # Si no se a especificado la ruta se utiliza la default
        if not ruta3:
            ruta = ruta2[0] + "\\Boletas\\Orden" + argu + ".pdf"
        else:
            ruta = ruta3 + "\\Orden" + argu + ".pdf"
        # Preguntamos si queremos imprimir el pdf
        bole = messagebox.askyesno(message="¿Imprimir boleta?", title="Boleta")
        if bole:
            try:
                ShellExecute(0, "print", ruta, None, ".", 0)
            except:
                print("Impresora no encontrada")
        # Abrimos el pdf en el navegador
        if not naveg:
            webbrowser.open(ruta, new=2, autoraise=True)

    # Si no reconoce el sistema
    ####################################################################
    else:
        print("Sistema no reconocido")