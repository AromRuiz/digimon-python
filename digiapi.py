import requests
import json
datos_api = requests.get("https://digi-api.com/api/v1/digimon/Agumon").json()
with open("digimon.JSON", "r", encoding="utf-8") as f:
    datos_locales = json.load(f)

    #NOMBRE
local_dict = {d["nombre"]: d for d in datos_locales}

name = datos_api.get("name") or local_dict.get(nombre_busqueda, {}).get("nombre")

nivel = datos_api.get("levels", [{}])[0].get("level", "Desconocido")
imagen = datos_api.get("images", [{}])[0].get("href")

evoluciones = datos_api.get("nextEvolutions", []) or local_dict.get(name, {}).get("evoluciones", [])