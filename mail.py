from smtplib import SMTP_SSL
from smtplib import SMTPException
from ssl import create_default_context
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from base_exp import exportacion
from decri import decriptar
from os import remove
from os import path


"""
La siguiente secuencia de comandos le permitirá enviar un correo electrónico a
través del servidor SMTP de Gmail. Sin embargo, Google no permitirá el inicio
de sesión a través de smtplib porque ha marcado este tipo de inicio de sesión
como "menos seguro". Para solucionar este problema, vaya a
https://www.google.com/settings/security/lesssecureapps
mientras está conectado a su cuenta de Google y a
"Permitir aplicaciones menos seguras".
"""


# Lectura del archivo de configuracion
def lectura():
    #  Lectura del archivo de configuracion
    a = open(archivo, "r")
    dato = a.readlines()
    a.close()
    return dato


# Leemos el usuario y el pass del mail
ruta1 = path.abspath(__file__)
ruta2 = path.split(ruta1)
archivo = ruta2[0] + "/config"
atur = lectura()
user = atur[11].lstrip("usuario:").rstrip("\n")
atur12 = atur[12].lstrip("passwd:").rstrip("\n")
pasw = decriptar(atur12)


asuntos = "Copia de seguridad de la base de datos"


def mails():

    # Nombre del archivo creado que vamos a enviar
    archivo = exportacion(False)

    # Pedir datos para el inicio de sesion
    username = user
    password = pasw
    destinatario = user
    asunto = asuntos

    # Crear el mensaje
    mensaje = MIMEMultipart("alternative")  # estandar
    mensaje["Subject"] = asunto
    mensaje["From"] = username
    mensaje["To"] = destinatario

    html = f"""
    <html>
    <body>
        Hola {destinatario}<br>
        Se adjunta una copia de su base de datos en formato exel<br>
        con el nombre {archivo}
    </body>
    </html>
    """

    # El contenido del mansaje como html
    parte_html = MIMEText(html, "html")
    # Agregar ese contenido al mensaje
    mensaje.attach(parte_html)

    with open(archivo, "rb") as adjunto:
        contenido_adjunto = MIMEBase("application", "octet-stream")
        contenido_adjunto.set_payload(adjunto.read())

    encoders.encode_base64(contenido_adjunto)

    contenido_adjunto.add_header(
        "Content-Disposition",
        f"attachment; filename= {archivo}",
    )
    mensaje.attach(contenido_adjunto)
    mensaje_final = mensaje.as_string()

    context = create_default_context()

    mensaje_error = f"""
    Error a tratar de envial el mail.
    Por favor revise que el correo: {username}
    este configurado correctamente.
    """

    try:
        with SMTP_SSL("smtp.gmail.com", 465, context=context) as se:
            se.login(username, password)
            print("Sesion iniciada.")
            se.sendmail(username, destinatario, mensaje_final)
            print("Mensaje enviado.")

    except SMTPException:
        print(mensaje_error)

    # Eliminamos el archivo ya enviado
    remove(archivo)
