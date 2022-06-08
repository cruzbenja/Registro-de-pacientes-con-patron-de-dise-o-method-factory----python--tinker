import requests

coleccion = requests.get("http://tecnoprofe.com/api/paciente")

for dato in coleccion.json():
    print(dato)