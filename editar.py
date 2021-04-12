from tkinter import Label, Entry, Button, Spinbox, Toplevel
from tkinter import IntVar, StringVar, BooleanVar
from tkinter import Checkbutton, Radiobutton
from base import BaseSecundaria


def estado():
    toor = Toplevel()  # Creamos una ventana
    toor.title("Editar el estado de la reparacion")  # Titulo de la ventana
    toor.geometry("425x350")  # Tamaño de la ventana

    # Obtengo el utlimo reguistro de la base
    try:
        ultimo = BaseSecundaria.select().order_by(BaseSecundaria.orden.desc()).get()
    except:
        ultimo = 0
    # Variables
    numoer = IntVar()
    ordent = IntVar()
    costot = IntVar()
    totalt = IntVar()
    decrit = StringVar()
    notift = BooleanVar()

    # Cargo los datos de la base en pantalla
    def ichi():
        try:
            if numoer.get() == 0:
                numoer.set(1)
                costot.set(0)
                totalt.set(0)
                decrit.set("Nuevo ingreso")
                notift.set(False)
            else:
                conta = ordent.get()
                est_ado = BaseSecundaria.get(BaseSecundaria.orden == conta).estado
                cos_tot = BaseSecundaria.get(BaseSecundaria.orden == conta).costo
                tot_tal = BaseSecundaria.get(BaseSecundaria.orden == conta).total
                des_cri = BaseSecundaria.get(BaseSecundaria.orden == conta).descripcion
                not_tif = BaseSecundaria.get(BaseSecundaria.orden == conta).notificacion
                numoer.set(est_ado)
                costot.set(cos_tot)
                totalt.set(tot_tal)
                decrit.set(des_cri)
                notift.set(not_tif)
        except:
            print("No encontrado")

    def guardar_estado(*args):
        # Guardo los datos
        orden1 = ordent.get()
        estad1 = numoer.get()
        costo1 = costot.get()
        total1 = totalt.get()
        descr1 = decrit.get()
        notif1 = notift.get()
        # Actualizo el registro secundario
        actualizar = BaseSecundaria.update(
            estado=estad1,
            costo=costo1,
            total=total1,
            descripcion=descr1,
            notificacion=notif1,
        ).where(BaseSecundaria.orden == orden1)
        actualizar.execute()

    texto0 = Label(toor, text="Orden de reparacion N°")
    texto0.place(x=10, y=0)
    entrada0 = Spinbox(
        toor, from_=0, to=ultimo, width=6, textvariable=ordent, command=ichi
    )
    entrada0.place(x=180, y=0)
    texto1 = Label(toor, text="Estado de la reparacion:")
    texto1.place(x=10, y=38)
    busq1 = Radiobutton(toor, text="En reparacion", value=2, variable=numoer)
    busq1.place(x=0, y=65)
    busq2 = Radiobutton(toor, text="Presupuestado", value=3, variable=numoer)
    busq2.place(x=120, y=65)
    busq3 = Radiobutton(toor, text="Entregado", value=4, variable=numoer)
    busq3.place(x=260, y=65)
    texto2 = Label(toor, text="Costos")
    texto2.place(x=10, y=110)
    entrada1 = Entry(toor, width=30, textvariable=costot)
    entrada1.place(x=110, y=110)
    texto3 = Label(toor, text="Total")
    texto3.place(x=10, y=150)
    entrada2 = Entry(toor, width=30, textvariable=totalt)
    entrada2.place(x=110, y=150)
    texto4 = Label(toor, text="Descripcion")
    texto4.place(x=10, y=190)
    entrada3 = Entry(toor, width=30, textvariable=decrit)
    entrada3.place(x=110, y=190)
    notifi = Checkbutton(
        toor,
        text="Notificar al cliente",
        variable=notift,
        onvalue=1,
        offvalue=0,
    )
    notifi.place(x=15, y=230)
    boton = Button(toor, text="Guardar", command=guardar_estado)
    boton.bind("<Return>", guardar_estado)  # Esto es para el enter
    boton.place(x=275, y=230)

    toor.mainloop()
