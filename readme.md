Este es un proyecto destinado a los pequeños y medianos telleres de reparacion en electronica.

El proyecto trata de ser lo mas simple y directo para el usuario, sin tantas opciones y complicaciones
que traen los grandes programas SAT.

Con este proyecto podran ingresar los datos del aparato, cliente y gurdarlos en una base
de datos a su vez se generara una boleta que es la orden de reparacion del aparato con todos
los datos del cliente y del aparato con la posibilidad de imprimir la orden de reparacion o
guardar la orden de reparacion en un pdf. Tambien dispone de una segunda base de datos para
llevar un control mas personal de las reparaciones como lo son costos de reparacion, presupuesto
total, estado de la reparacion, falla, reparacion, notificacion al cliente, etc.

La orden de reparacion puede ser personalizada con los datos del taller o del reparador al estar echa
con reportlab. Los datos se guardan en una base de datos SQLite manejada a traves de peewee para
mayor simplicidad.
