import pywhatkit

from datetime import datetime
import time

seconds = time.time() + 60

data = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg("+573206387022","Buenos dias caro como estas",data.hour,
                      data.minute)
time.sleep(5)

# pywhatkit.sendwhats_image("+573127251557","test.png")