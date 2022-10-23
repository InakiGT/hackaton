import eel
from models.detection import *

eel.init('web')

@eel.expose
def detect_ear():
    is_ear, values = classify_ear()
    eel.get_result(is_ear, values)

eel.start('index.html')