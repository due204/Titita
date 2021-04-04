import dropbox
from datetime import datetime


clave_token = "sl.AuWbUmsUTlrduMkbZ6zvBSK9hjlfyCj7GB5p0OhMRHA1KhXCyLcicc9C8swRuAvyw1B7bc31GVHhb0xtocny_EEOtg_3Do5eDjYVjMXwkVb7V5oyAv8FPILZGlBOeVtElTq9MtGVSQo"
archivo = "base_datos.db"
fecha = datetime.now()
subida = "/" + str(fecha.date()) + "-" + archivo

dropboxy = dropbox.Dropbox(clave_token)
dropboxy.files_upload(open(archivo, "rb").read(), subida)
