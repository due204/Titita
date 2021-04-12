import os
import sys
import webbrowser

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)
archivo = ruta2[0] + "/config"

a = open(archivo, "r")
dato = a.readlines()
ruta3 = dato[0].lstrip("ruta_boleta:").rstrip("\n")
naveg = dato[6].lstrip("navegador_1:").rstrip("\n")
a.close()


# Determina en que OS estamos trabajando
def imprimir(argu):
    if sistema == "linux":
        if not naveg:
            ruta = ruta3 + "/Orden" + argu + ".pdf"
            webbrowser.open(ruta, new=2, autoraise=True)
    elif sistema == "win32" or "win64":
        if not naveg:
            ruta = ruta3 + argu + ".pdf"
            webbrowser.open(ruta, new=2, autoraise=True)
    else:
        print("Sistema no reconocido")
