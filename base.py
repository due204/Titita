from peewee import SqliteDatabase
from peewee import AutoField
from peewee import CharField
from peewee import DateField
from peewee import IntegerField
from peewee import Model
from datetime import datetime
import os
import sys

sistema = sys.platform
ruta1 = os.path.abspath(__file__)
ruta2 = os.path.split(ruta1)


# Determina en que OS estamos trabajando
if sistema == "linux":
    # if not os.path.isfile(ruta2[0] + "/" + "base_datos.db"):
    ruta3 = ruta2[0] + "/" + "base_datos.db"
elif sistema == "win32" or "win64":
    ruta3 = ruta2[0] + "\\" + "base_datos.db"
else:
    print("Sistema no reconocido")

print("OS:", sistema)
print("db:", ruta3)

# Nombre de la base de datos
db = SqliteDatabase(ruta3)


# Crear la base de datos y su tabla
class BaseDatos(Model):
    orden = AutoField()
    fecha = DateField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    direccion = CharField()
    tipo = CharField()
    marca = CharField()
    modelo = CharField()
    falla = CharField()
    otros = CharField()
    estado = IntegerField()  # IntegerField para numeros
    costo = IntegerField()
    total = IntegerField()
    descripcion = CharField()  # CharField para caracteres
    notificacion = CharField()

    class Meta:
        database = db

    def guardar(
        self,
        nomb,
        apel,
        tele,
        dire,
        tipo,
        marc,
        mode,
        fall,
        otro,
        esta,
        cost,
        tota,
        decr,
        noti,
    ):
        datos = BaseDatos(
            fecha=datetime.now(),
            nombre=nomb,
            apellido=apel,
            telefono=tele,
            direccion=dire,
            tipo=tipo,
            marca=marc,
            modelo=mode,
            falla=fall,
            otros=otro,
            estado=esta,
            costo=cost,
            total=tota,
            descripcion=decr,
            notificacion=noti,
        )
        datos.save()


db.connect()
db.create_tables([BaseDatos])
