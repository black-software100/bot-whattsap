# se instacai la libreria de whatsapp
import pywhatkit
# se intacia la libreria de de fecha
from datetime import datetime
# se instacia la libreria de tiempo
import time

#se crea una variable que tenga la fecha y hora + 60 para que tenga un minuto para complectar el proceso
seconds = time.time() + 60

#se crea una varibale para darle formato de fecha y hora 
data = datetime.fromtimestamp(seconds)

# se crea un objecto de mensaje con los siguentes parametros
#numero mas indicativo
#mensaje
#hora
#minuto
pywhatkit.sendwhatmsg("+57xxxxxxxxxxx","mensaje ",data.hour,data.minute)

# se crea un tiempo de espera de 5 segundos
time.sleep(5)

#se crea un objecto de para enviar fotos
pywhatkit.sendwhats_image("+57xxxxxxxxxxx","img.jpg")