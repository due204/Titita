from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import sys

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)


# Determina en que OS estamos trabajando
if sistema == "linux":
    if not os.path.isdir(ruta2[0] + "/" + "Boletas"):
        os.mkdir(ruta2[0] + "/" + "Boletas")
    ruta3 = ruta2[0] + "/" + "Boletas/"
elif sistema == "win32" or "win64":
    if not os.path.isdir(ruta2[0] + "\\" + "Boletas"):
        os.mkdir(ruta2[0] + "\\" + "Boletas")
    ruta3 = ruta2[0] + "\\" + "Boletas" + "\\"
else:
    print("Sistema no reconocido")

print("Boletas:", ruta3)


nombre1 = "Estudio de"
nombre2 = "Computacion"
direccion1 = "Calle 845 N° 2590 - Solano"
direccion2 = "Telefonos: 4271-1279 -- 4212-4585"
celu = "Guasa 11-4946-4066"


def boleta(mi_lista):
    nom_bole = ruta3 + "Orden" + mi_lista[0] + ".pdf"
    fech = datetime.today()
    fecha = fech.strftime("Dia :%d, Mes: %m, Año: %Y")
    orden = mi_lista[0]
    nom_ape = "Nombre: " + mi_lista[1]
    domici = "Domicilio: " + mi_lista[2]
    telefo = "Telefono: " + mi_lista[3]
    marca = "Marca: " + mi_lista[4]
    modelo = "Modelo: " + mi_lista[5]
    falla = "Falla: " + mi_lista[6]
    otros = "Otros: " + mi_lista[7]

    w, h = A4
    c = canvas.Canvas(nom_bole, pagesize=A4)
    # Boleta 01
    # Textos y datos de la boleta
    c.saveState()
    c.translate(50, 670)
    c.rotate(90)
    c.setFont("Helvetica", 7)
    c.drawString(-220, 22, fecha)
    c.setFont("Helvetica", 7)
    c.drawString(35, 22, "Documento no valido como factura")
    c.setFont("Helvetica", 20)
    c.drawString(-180, -5, nombre1)
    c.setFont("Helvetica", 20)
    c.drawString(-195, -25, nombre2)
    c.setFont("Helvetica", 10)
    c.drawString(-200, -40, direccion1)
    c.setFont("Helvetica", 10)
    c.drawString(-215, -55, direccion2)
    c.setFont("Helvetica", 15)
    c.drawString(0, 0, "Orden de reparacion")
    c.setFont("Helvetica", 30)
    c.drawString(40, -40, orden)  # Numero de orden
    c.setFont("Helvetica", 10)
    c.drawString(-220, -90, nom_ape)
    c.setFont("Helvetica", 10)
    c.drawString(-220, -110, domici)
    c.setFont("Helvetica", 10)
    c.drawString(-220, -130, telefo)
    c.setFont("Helvetica", 15)
    c.drawString(-220, -170, "Detalles del equipo:")
    c.setFont("Helvetica", 10)
    c.drawString(-220, -190, marca)
    c.setFont("Helvetica", 10)
    c.drawString(-220, -210, modelo)
    c.setFont("Helvetica", 10)
    c.drawString(-220, -230, falla)
    c.setFont("Helvetica", 15)
    c.drawString(-220, -280, "Reparacion: ______________________________")
    c.setFont("Helvetica", 15)
    c.drawString(-220, -310, " ________________________________________")
    c.setFont("Helvetica", 15)
    c.drawString(-220, -340, " ________________________________________")
    c.setFont("Helvetica", 10)
    c.drawString(-220, -380, otros)
    c.setFont("Helvetica", 10)
    c.drawString(-190, -410, "Presupuesto")
    c.setFont("Helvetica", 10)
    c.drawString(-70, -410, "Anticipo")
    c.setFont("Helvetica", 10)
    c.drawString(50, -410, "Saldo")
    c.setFont("Helvetica", 7)
    c.drawString(
        -218,
        -440,
        "NOTA IMPORTANTE: Los equipos solo pueden ser retirados con su respectivo comprobante, de no tenerlo,",
    )
    c.setFont("Helvetica", 7)
    c.drawString(
        -218,
        -448,
        "se retiraran con el documento del titular. Pasado los 90 dias los equipos SERAN CONSIDERADOS AVANDONADOS",
    )
    c.setFont("Helvetica", 7)
    c.drawString(
        -218,
        -456,
        "respaldados por los terminos del articulo 2525 y 2526 del codigo civil.",
    )
    c.setFont("Helvetica", 10)
    c.drawString(-190, -495, "-------------------------------")
    c.setFont("Helvetica", 10)
    c.drawString(-150, -505, "Firma")
    c.setFont("Helvetica", 10)
    c.drawString(0, -495, "-------------------------------")
    c.setFont("Helvetica", 10)
    c.drawString(40, -505, "DNI")
    c.setFont("Helvetica", 10)
    c.drawString(-90, -530, celu)
    c.restoreState()
    # Cuadros y marcos
    c.rect(20, h - 410, 550, 400)  # Marco externo superior
    c.rect(30, h - 400, 530, 380)  # Marco interno superior
    c.rect(34, h - 184, 70, 160)  # Marco de orden
    c.rect(110, h - 400, 5, 380)  # Marco de separacion 1
    c.rect(190, h - 400, 10, 380)  # Marco de separacion 2
    c.rect(290, h - 400, 10, 380)  # Marco de separacion 3
    c.rect(450, h - 390, 15, 113)  # Marco de separacion presupuesto superior
    c.rect(450, h - 276, 15, 113)  # Marco de separacion anticipo superior
    c.rect(450, h - 164, 15, 113)  # Marco de separacion saldo superior
    c.rect(465, h - 390, 15, 113)  # Marco de separacion presupuesto inferior
    c.rect(465, h - 276, 15, 113)  # Marco de separacion anticipo inferior
    c.rect(465, h - 164, 15, 113)  # Marco de separacion saldo inferior

    #########################################################

    # Boleta 02
    # Textos y datos de la boleta
    c.saveState()
    c.translate(50, 670)
    c.rotate(90)
    c.setFont("Helvetica", 7)
    c.drawString(-640, 22, fecha)
    c.setFont("Helvetica", 7)
    c.drawString(-385, 22, "Documento no valido como factura")
    c.setFont("Helvetica", 20)
    c.drawString(-600, -5, nombre1)
    c.setFont("Helvetica", 20)
    c.drawString(-616, -25, nombre2)
    c.setFont("Helvetica", 10)
    c.drawString(-623, -40, direccion1)
    c.setFont("Helvetica", 10)
    c.drawString(-640, -55, direccion2)
    c.setFont("Helvetica", 15)
    c.drawString(-420, 0, "Orden de reparacion")
    c.setFont("Helvetica", 30)
    c.drawString(-380, -40, orden)  # Numero de orden
    c.setFont("Helvetica", 10)
    c.drawString(-640, -90, nom_ape)
    c.setFont("Helvetica", 10)
    c.drawString(-640, -110, domici)
    c.setFont("Helvetica", 10)
    c.drawString(-640, -130, telefo)
    c.setFont("Helvetica", 15)
    c.drawString(-640, -170, "Detalles del equipo:")
    c.setFont("Helvetica", 10)
    c.drawString(-640, -190, marca)
    c.setFont("Helvetica", 10)
    c.drawString(-640, -210, modelo)
    c.setFont("Helvetica", 10)
    c.drawString(-640, -230, falla)
    c.setFont("Helvetica", 15)
    c.drawString(-640, -280, "Reparacion: ______________________________")
    c.setFont("Helvetica", 15)
    c.drawString(-640, -310, " ________________________________________")
    c.setFont("Helvetica", 15)
    c.drawString(-640, -340, " ________________________________________")
    c.setFont("Helvetica", 10)
    c.drawString(-640, -380, otros)
    c.setFont("Helvetica", 10)
    c.drawString(-610, -410, "Presupuesto")
    c.setFont("Helvetica", 10)
    c.drawString(-490, -410, "Anticipo")
    c.setFont("Helvetica", 10)
    c.drawString(-370, -410, "Saldo")
    c.setFont("Helvetica", 7)
    c.drawString(
        -640,
        -440,
        "NOTA IMPORTANTE: Los equipos solo pueden ser retirados con su respectivo comprobante, de no tenerlo,",
    )
    c.setFont("Helvetica", 7)
    c.drawString(
        -640,
        -448,
        "se retiraran con el documento del titular. Pasado los 90 dias los equipos SERAN CONSIDERADOS AVANDONADOS",
    )
    c.drawString(
        -640,
        -456,
        "respaldados por los terminos del articulo 2525 y 2526 del codigo civil.",
    )
    c.setFont("Helvetica", 10)
    c.drawString(-610, -495, "-------------------------------")
    c.setFont("Helvetica", 10)
    c.drawString(-570, -505, "Firma")
    c.setFont("Helvetica", 10)
    c.drawString(-420, -495, "-------------------------------")
    c.setFont("Helvetica", 10)
    c.drawString(-380, -505, "DNI")
    c.setFont("Helvetica", 10)
    c.drawString(-510, -530, celu)
    c.restoreState()
    # Cuadros y marcos
    c.rect(20, h - 830, 550, 400)  # Marco externo inferior
    c.rect(30, h - 820, 530, 380)  # Marco interno superior
    c.rect(34, h - 604, 70, 160)  # Marco de orden
    c.rect(110, h - 820, 5, 380)  # Marco de separacion 1
    c.rect(190, h - 820, 10, 380)  # Marco de separacion 2
    c.rect(290, h - 820, 10, 380)  # Marco de separacion 3
    c.rect(450, h - 810, 15, 113)  # Marco de separacion presupuesto superior
    c.rect(450, h - 696, 15, 113)  # Marco de separacion anticipo superior
    c.rect(450, h - 584, 15, 113)  # Marco de separacion saldo superior
    c.rect(465, h - 810, 15, 113)  # Marco de separacion presupuesto inferior
    c.rect(465, h - 696, 15, 113)  # Marco de separacion anticipo inferior
    c.rect(465, h - 584, 15, 113)  # Marco de separacion saldo inferior

    #########################################################

    c.showPage()
    c.save()
