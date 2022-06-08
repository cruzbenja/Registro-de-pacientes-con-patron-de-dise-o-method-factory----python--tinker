# importamos libreria
# import requests
# coleccion= requests.get("http://tecnoprofe.com/api/cancion")
# print(coleccion.json())
# for dato in coleccion.json():
#     print(dato["artista"])    
import requests

# informacion={ "artista":"ok "}
# coleccion= requests.post("http://tecnoprofe.com/api/cancion",data=informacion)

coleccion= requests.get("http://tecnoprofe.com/api/cancion")

for dato in coleccion.json():
    print(dato["artista"])
