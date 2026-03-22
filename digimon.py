class Digimon:
    def __init__(self, nombre, nivel, tipo, atributo, familia):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.atributo = atributo
        self.familia = familia
        self.evoluciones= []

    def agregar_evolucion(self, digimon):
        self.evoluciones.append(digimon)

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nivel:", self.nivel)
        print("Tipo:", self.tipo)
        print("Atributo:", self.atributo)
        print("Familia:")
        for f in self.familia:
            print("-", f,sep="")
        print("Evoluciona a:")
        for e in self.evoluciones:
            print("-", e.nombre, sep="")

import json
with open("digimon.JSON", "r",encoding="utf-8") as f:
    digimons_data = json.load(f)
"""print(json.dumps(digimons_data, indent=2))"""
digimons = {}

for d in digimons_data:
    digimons[d["nombre"]] = Digimon(
        d["nombre"],
        d["nivel"],
        d["tipo"],
        d["atributo"],
        d["familia"]
    )
for d in digimons_data:
    for evo in d.get("evoluciones", []):
        nombre_evo = evo["nombre"]
        tipo_evo = evo.get("tipo_evolucion")
        req_evo = evo.get("requisitos")
        if nombre_evo in digimons:
            digimons[d["nombre"]].agregar_evolucion(digimons[nombre_evo])

"""digimons["Botamon"].mostrar()"""
for digimon in digimons.values():
    digimon.mostrar()
    print(".........")
#for digimon in digimons.values():
#    if digimon.nivel == "Infantil":
#        digimon.mostrar()