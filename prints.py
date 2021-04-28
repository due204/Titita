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
        ruta = ruta3 + "/Orden" + argu + ".pdf"
        # Comando GNU/Linux para la impresion
        # Necesita tener cups instalado en su sistema
        # Y configurado su impresora a traves de cups
        ruta_l = "lp -o media=A4" + " " + ruta
        os.system(ruta_l)
        if not naveg:
            webbrowser.open(ruta, new=2, autoraise=True)
    elif sistema == "win32" or "win64":
        import win32api

        if not naveg:
            ruta = ruta3 + "\Orden" + argu + ".pdf"
            webbrowser.open(ruta, new=2, autoraise=True)
            try:
                win32api.ShellExecute(0, "print", ruta, None, ".", 0)
            except:
                print("Impresora no encontrada")
    else:
        print("Sistema no reconocido")
