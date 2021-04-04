import os
import sys

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)


# Determina en que OS estamos trabajando
def imprimir(argu):

    if sistema == "linux":
        ruta3 = ruta2[0] + "/Boletas/Orden" + argu + ".pdf"
        # os.system("lpr" + ruta3)
        print(ruta3)
    elif sistema == "win32" or "win64":
        ruta3 = ruta2[0] + "\\Boletas\\Orden" + argu + ".pdf"
        # os.startfile(ruta3, "print")
        print(ruta3)
    else:
        print("Sistema no reconocido")


imprimir("00001")
