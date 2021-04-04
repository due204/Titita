import dropbox
from datetime import datetime


clave_token = "sl.AuSe_jxi6VWdCiRMMtl6bwjvTlQhPCnzQhf-QKwbgbe2MkkCGAwgsNDvQS4ioHp6JvRx1PUOgdLSBq4j9oPI3FWE71gfLApGRR7IYHkbOVclHiKaQbYhnPT_kFF-lb_mAiN9VEbJ9z4"
archivo = "base_datos.db"
fecha = datetime.now()
subida = "/" + str(fecha) + "-" + archivo

dropboxy = dropbox.Dropbox(clave_token)
dropboxy.files_upload(open(archivo, "rb").read(), subida)
