from peewee import SqliteDatabase, AutoField, BooleanField
from peewee import CharField, DateField, IntegerField
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

    class Meta:
        database = db

    def guardar(self, nomb, apel, tele, dire, tipo, marc, mode, fall, otro):
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
        )
        datos.save()
        BaseSecundaria.guardar2(0, 1, 0, 0, "Nuevo ingreso", False)


class BaseSecundaria(Model):
    orden = AutoField()
    estado = IntegerField()  # IntegerField para numeros
    costo = IntegerField()
    total = IntegerField()
    descripcion = CharField()  # CharField para caracteres
    notificacion = BooleanField(default=False)

    def guardar2(self, esta, cost, tota, decr, noti):
        datos2 = BaseSecundaria(
            estado=esta,
            costo=cost,
            total=tota,
            descripcion=decr,
            notificacion=noti,
        )
        datos2.save()

    class Meta:
        database = db


class Configuraciones(Model):
    boletas = CharField()
    nombre1 = CharField()
    nombre2 = CharField()
    direccion1 = CharField()
    direccion2 = CharField()
    celular = CharField()

    def guardar3(self, bole, nom1, nom2, dir1, dir2, cel):
        datos3 = Configuraciones(
            boleta=bole,
            nombre1=nom1,
            nombre2=nom2,
            direccion1=dir1,
            direccion2=dir2,
            celular=cel,
        )
        datos3.save()

    class Meta:
        database = db


db.connect()
db.create_tables([BaseDatos, BaseSecundaria])
