import numpy as np
from unidecode import unidecode

# clave normalizada: (nombre a mostrar, estado, latitud, longitud)
CIUDADES = {
    "irapuato":       ("Irapuato", "Guanajuato", 20.6767, -101.3563),
    "moroleon":       ("Moroleón", "Guanajuato", 20.1286, -101.1887),
    "morelia":        ("Morelia", "Michoacán", 19.7060, -101.1950),
    "apaseo":         ("Apaseo el Grande", "Guanajuato", 20.5467, -100.6869),
    "queretaro":      ("Querétaro", "Querétaro", 20.5888, -100.3899),
    "celaya":         ("Celaya", "Guanajuato", 20.5235, -100.8157),
    "cortazar":       ("Cortazar", "Guanajuato", 20.4825, -100.9640),
    "cdmx":           ("Ciudad de México", "Ciudad de México", 19.4326, -99.1332),
    "aculco":         ("Aculco", "Estado de México", 20.0986, -99.8336),
    "penjamo":        ("Pénjamo", "Guanajuato", 20.4306, -101.7200),
    "xalapa":         ("Xalapa", "Veracruz", 19.5438, -96.9102),
    "jilotepec":      ("Jilotepec", "Estado de México", 19.9525, -99.5311),
    "salamanca":      ("Salamanca", "Guanajuato", 20.5719, -101.1957),
    "toluca":         ("Toluca", "Estado de México", 19.2826, -99.6557),
    "tepeji del rio": ("Tepeji del Río", "Hidalgo", 19.9047, -99.3440),
}

def clave(ciudad):
    return unidecode(str(ciudad)).strip().lower()

def info(ciudad):
    return CIUDADES.get(clave(ciudad))

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp, dl = p2 - p1, np.radians(lon2 - lon1)
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))