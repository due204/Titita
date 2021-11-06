from datetime import datetime
from datetime import date
from base_exp import exportacion
from mail import mails
from os import path

ruta1 = path.abspath(__file__)
ruta2 = path.split(ruta1)
archivo = ruta2[0] + "/config"


def lectura():
    #  Lectura del archivo de configuracion
    a = open(archivo, "r")
    dato = a.readlines()
    a.close()
    return dato


def backup():
    """
    Esta funcion se encarga de verificar si hay que hacer un backup y cuando
    """
    dia_b = lectura()
    si_no = dia_b[10].lstrip("enviar:").rstrip("\n")
    si_no2 = dia_b[9].lstrip("guardar:").rstrip("\n")
    cop = int(dia_b[8].lstrip("fecha:").rstrip("\n"))

    if si_no == "True" or si_no2 == "True":
        if cop == 1:
            copia_dia()
        elif cop == 2 or cop == 3:
            copia_sem_mes()
    else:
        print("Sin backup programado.")


def copia_dia():
    """
    Esta funcion crea una copia de nuestra base de datos una vez al dia
    """
    dt = datetime.now()
    dia_a = dt.timetuple()
    dia_b = lectura()
    dia_c = int(dia_b[13].lstrip("dia_c:").rstrip("\n"))
    if dia_c != dia_a.tm_yday:
        a = open(archivo, "r").readlines()
        a[13] = "dia_c:" + str(dia_a.tm_yday) + "\n"
        b = open(archivo, "w")
        b.writelines(a)
        b.close()
        si_no = dia_b[10].lstrip("enviar:").rstrip("\n")
        si_no2 = dia_b[9].lstrip("guardar:").rstrip("\n")
        if si_no == "True":
            mails()
        if si_no2 == "True":
            exportacion(False)
    else:
        print("Backup: Estas al dia.")


def copia_sem_mes():
    """
    Esta funcion crea una copia de nuestra base de datos una vez al la semana
    o una vez al mes.
    """
    dia_b = lectura()

    if int(dia_b[8].lstrip("fecha:").rstrip("\n")) == 2:
        dt = datetime.today().weekday()
    elif int(dia_b[8].lstrip("fecha:").rstrip("\n")) == 3:
        dt = date.today()
    elif not int(dia_b[8].lstrip("fecha:").rstrip("\n")):
        print("Sin copia")
    else:
        print("Copia al dia")

    dia_c = int(dia_b[7].lstrip("dias:").rstrip("\n"))
    dia_d = int(dia_b[14].lstrip("dia_d:").rstrip("\n"))

    if dt == dia_c:
        if dia_d == 0:
            a = open(archivo, "r").readlines()
            a[14] = "dia_d:" + "1" + "\n"
            b = open(archivo, "w")
            b.writelines(a)
            b.close()
            si_no = dia_b[10].lstrip("enviar:").rstrip("\n")
            si_no2 = dia_b[9].lstrip("guardar:").rstrip("\n")
            if si_no == "True":
                mails()
            if si_no2 == "True":
                exportacion(False)
        else:
            print("Estas al dia.")
    else:
        a = open(archivo, "r").readlines()
        a[14] = "dia_d:" + "0" + "\n"
        b = open(archivo, "w")
        b.writelines(a)
        b.close()
        print("Hoy no toca respaldo.")
