import os
import sys
import webbrowser

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)


# Determina en que OS estamos trabajando
def imprimir(argu):

    if sistema == "linux":
        ruta3 = ruta2[0] + "/Boletas/Orden" + argu + ".pdf"
        webbrowser.open(ruta3, new=2, autoraise=True)
    elif sistema == "win32" or "win64":
        ruta3 = ruta2[0] + "\\Boletas\\Orden" + argu + ".pdf"
        webbrowser.open(ruta3, new=2, autoraise=True)
    else:
        print("Sistema no reconocido")
