from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import IntVar
from tkinter import Button
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import BooleanVar
from tkinter import LabelFrame
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Radiobutton
from tkinter import Checkbutton
from tkcalendar import Calendar
from datetime import datetime
from base_exp import importacion
from base_exp import exportacion
from decri import encriptar
from os import path

ruta1 = path.abspath(__file__)
ruta2 = path.split(ruta1)
archivo = ruta2[0] + "/config"

textedu = """Por correccion de errores, dudas o sugerencias no duden en
contactarme al mail: due204@gmail.com"""


def configuracion():
    def lectura():
        #  Lectura del archivo de configuracion
        a = open(archivo, "r")
        dato = a.readlines()
        a.close()
        return dato

    def menu_uno():
        def guardar_datos():
            #  Guardamos los datos en el archico de configuracion
            a = open(archivo, "r").readlines()
            a[0] = "ruta_boleta:" + ruta.get() + "\n"
            a[1] = "nombre_1:" + nombre1.get() + "\n"
            a[2] = "nombre_2:" + nombre2.get() + "\n"
            a[3] = "direccion_1:" + direccion1.get() + "\n"
            a[4] = "direccion_2:" + direccion2.get() + "\n"
            a[5] = "celular_1:" + telefono.get() + "\n"
            a[6] = "navegadoor_1:" + navegador.get() + "\n"
            b = open(archivo, "w")
            b.writelines(a)
            b.close()
            toor.quit()
            toor.destroy()

        def guradar_ruta():
            # Seleccionamos el directorio
            directorio = filedialog.askdirectory()
            if directorio:
                print(directorio)
                # Seteamos el directiorio
                ruta.set(directorio)

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

        texto_b = Label(
            toor,
            text="Configuracion de la boleta generada en pdf",
        )
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
        pdfs.place(x=0, y=330)

        boton1 = Button(toor, text="Guardar", command=guardar_datos)
        boton1.bind("<Return>", guardar_datos)  # Esto es para el enter
        boton1.place(x=330, y=310)

        boton3 = Button(toor, text="Backup", command=menu_dos)
        boton3.bind("<Return>", menu_dos)  # Esto es para el enter
        boton3.place(x=330, y=348)

        texto7 = Label(toor, text=textedu)
        texto7.place(x=10, y=410)

        toor.mainloop()

    def menu_dos():
        frame1 = Frame(toor)
        frame1.config(width=425, height=500)
        label3 = Label(frame1, text="Backup...")
        label3.place(x=150, y=220)

        for i in range(-300, 1):
            frame1.place(x=i, y=0)
            frame1.update()
        label3.destroy()

        def guardar_dat(*argus):
            # Guardamos los datos en el archivo de configuracion
            a = open(archivo, "r").readlines()
            if fecha.get() == 3:
                fechaa = cal.get_date().split("/")
                a[7] = "dias:" + str(fechaa[0]) + "\n"
            else:
                a[7] = "dias:" + str(dias.get()) + "\n"
            a[8] = "fecha:" + str(fecha.get()) + "\n"
            a[9] = "guardar:" + str(chequeo1.get()) + "\n"
            a[10] = "enviar:" + str(chequeo2.get()) + "\n"
            a[11] = "usuario:" + str(usuario.get()) + "\n"
            if contras.get():
                a[12] = "passwd:" + encriptar(str(contras.get())) + "\n"
            out = open(archivo, "w")
            out.writelines(a)
            out.close()
            atur12 = atur[12].lstrip("passwd:").rstrip("\n")

            if chequeo2.get():
                # Enviar el mail
                if usuario.get() and contras.get():
                    if "@gmail.com" in usuario.get():
                        pasar_menu()
                    else:
                        messagebox.showinfo(
                            message=f"{usuario.get()}\nNo es correo de Gmail",
                            title="Correo invalido",
                        )
                elif usuario.get() and atur12:
                    if "@gmail.com" in usuario.get():
                        pasar_menu()
                    else:
                        messagebox.showinfo(
                            message=f"{usuario.get()}\nNo es correo de Gmail",
                            title="Correo invalido",
                        )
                else:
                    messagebox.showinfo(
                        message="Usuario y/o contraseña de Gmail incorrectas",
                        title="Error",
                    )
            else:
                pasar_menu()

        def pasar_menu():
            frame1 = Frame(toor)
            frame1.config(width=425, height=500)
            label3 = Label(frame1, text="Guardar...")
            label3.place(x=150, y=220)
            for i in range(-300, 1):
                frame1.place(x=i, y=0)
                frame1.update()
            label3.destroy()
            menu_uno()

        # Fechas para el calendario
        now = datetime.now()
        año = int(now.strftime("%Y"))
        mes = int(now.strftime("%m"))
        dia = int(now.strftime("%d"))

        # Leemos las variables desde el archivo
        atur = lectura()
        atur7 = atur[7].lstrip("dias:").rstrip("\n")
        atur8 = atur[8].lstrip("fecha:").rstrip("\n")
        atur9 = atur[9].lstrip("gurdar:").rstrip("\n")
        atur10 = atur[10].lstrip("enviar:").rstrip("\n")
        atur11 = atur[11].lstrip("usuario:").rstrip("\n")
        # atur12 = atur[12].lstrip("passwd:").rstrip("\n")

        # ############### Frames ###############3
        # #######################################
        frame_cal = LabelFrame(toor, text="Calendario", padx=50)
        frame_cal.place(x=40, y=0)

        frame_cuanto = LabelFrame(toor, text="¿Cuantas veces?")
        frame_cuanto.place(x=10, y=230)

        frame_dias = LabelFrame(toor, text="¿Que dias?", pady=11)
        frame_dias.place(x=190, y=230)

        frame_check = Frame(toor, padx=50)
        frame_check.place(x=10, y=330)

        frame_mail = Frame(toor)
        frame_mail.place(x=10, y=360)

        frame_db = LabelFrame(toor, text="Base de datos", padx=5)
        frame_db.place(x=10, y=440)

        # ############### Widgets ###############
        # #######################################
        # Calendario
        cal = Calendar(
            frame_cal,
            selectmode="day",
            year=año,
            month=mes,
            day=dia,
        )
        cal.pack(pady=20)

        # cantidad de veces en que se va a hacer la copia
        fecha = IntVar()
        fecha.set(atur8)

        fec1 = Radiobutton(
            frame_cuanto,
            text="Una vez al dia",
            variable=fecha,
            value=1,
        )
        fec1.pack(anchor="w")

        fec2 = Radiobutton(
            frame_cuanto,
            text="Una vez a la semana",
            variable=fecha,
            value=2,
        )
        fec2.pack(anchor="w")

        fec3 = Radiobutton(
            frame_cuanto,
            text="Una vez al mes",
            variable=fecha,
            value=3,
        )
        fec3.pack(anchor="w")

        # Dias en que se va a hacer la copia
        dias = IntVar()
        dias.set(atur7)

        dia1 = Radiobutton(frame_dias, text="Lun", value=0, variable=dias)
        dia1.grid(row=0, column=0)

        dia2 = Radiobutton(frame_dias, text="Mar", value=1, variable=dias)
        dia2.grid(row=0, column=1)

        dia3 = Radiobutton(frame_dias, text="Mie", value=2, variable=dias)
        dia3.grid(row=0, column=2)

        dia4 = Radiobutton(frame_dias, text="Jue", value=3, variable=dias)
        dia4.grid(row=0, column=3)

        dia5 = Radiobutton(frame_dias, text="Vie", value=4, variable=dias)
        dia5.grid(row=1, column=0)

        dia6 = Radiobutton(frame_dias, text="Sab", value=5, variable=dias)
        dia6.grid(row=1, column=1)

        dia7 = Radiobutton(frame_dias, text="Dom", value=6, variable=dias)
        dia7.grid(row=1, column=2)

        # Opciones de guardado y envio
        chequeo1 = BooleanVar()
        chequeo2 = BooleanVar()
        chequeo1.set(atur9)
        chequeo2.set(atur10)

        check1 = Checkbutton(
            frame_check,
            text="Guardar copia",
            variable=chequeo1,
        )
        check1.grid(row=0, column=0)

        check2 = Checkbutton(
            frame_check,
            text="Enviar copia al mail",
            variable=chequeo2,
        )
        check2.grid(row=0, column=1)

        # User y pass del mail
        usuario = StringVar()
        contras = StringVar()
        usuario.set(atur11)
        # contras.set(atur12)

        label_mail = Label(
            frame_mail,
            text="Utilice un correo de Gmail previamente configurado",
        )
        label_mail.grid(row=0, column=0, sticky="w", columnspan=4)

        label_user = Label(frame_mail, text="Usuario")
        label_user.grid(row=1, column=0, sticky="w")

        entri_user = Entry(frame_mail, textvariable=usuario)
        entri_user.grid(row=1, column=1, sticky="w")

        label_cont = Label(frame_mail, text="contraseña")
        label_cont.grid(row=2, column=0, sticky="w")

        entri_pass = Entry(frame_mail, show="*", textvariable=contras)
        entri_pass.grid(row=2, column=1, pady=3, sticky="w")

        # Importar y exportar copia de seguridad
        boton_exp = Button(frame_db, text="Exportar", command=exportacion)
        boton_exp.bind("<Return>", exportacion)  # Esto es para el enter
        boton_exp.pack(side="left")

        boton_imp = Button(frame_db, text="Importar", command=importacion)
        boton_imp.bind("<Return>", importacion)  # Esto es para el enter
        boton_imp.pack(side="right")

        boton_guar = Button(toor, text="Volver", command=pasar_menu)
        boton_guar.bind("<Return>", pasar_menu)  # Esto es para el enter
        boton_guar.place(x=330, y=420)

        boton_vole = Button(toor, text="Guardar", command=guardar_dat)
        boton_vole.bind("<Return>", guardar_dat)  # Esto es para el enter
        boton_vole.place(x=330, y=460)

        toor.mainloop()

    toor = Toplevel()  # Creamos una ventana
    toor.title("Configurar Titita")  # Titulo de la ventana
    toor.geometry("425x500")  # Tamaño de la ventana
    toor.resizable(False, False)  # Evitamos modificar la ventana
    menu_uno()
