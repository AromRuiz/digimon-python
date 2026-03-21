# Constantes
CAZADORES_DE_VIRUS = "Cazadores de Virus"
"""
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

botamon = Digimon("Botamon", "Bebé I", "Baba", "Datos", [CAZADORES_DE_VIRUS])
botamon.mostrar()
koromon = Digimon("Koromon", "Bebé II", "Menor", "Datos", [CAZADORES_DE_VIRUS])
koromon.mostrar()
agumon = Digimon("Agumon", "Infantil", "Reptil", "Vacuna", ["Espíritus de la Naturaleza", CAZADORES_DE_VIRUS, "Imperio del Metal"])
agumon.mostrar()
greymon = Digimon("Greymon", "Adulto", "Dinosaurio", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón",CAZADORES_DE_VIRUS, "Imperio del Metal","Soldados de Pesadilla"])
greymon.mostrar()
metalgreymon = Digimon("MetalGreymon", "Perfecto", "Cyborg", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón",CAZADORES_DE_VIRUS, "Imperio del Metal","Soldados de Pesadilla"])
metalgreymon.mostrar()
aero_v_dramon = Digimon("AeroV-dramon", "Perfecto", "Dragón Volador", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón",CAZADORES_DE_VIRUS, "Imperio del Metal","Soldados de Pesadilla"])
aero_v_dramon.mostrar()

botamon.agregar_evolucion(koromon)
koromon.agregar_evolucion(agumon)
agumon.agregar_evolucion(greymon)
greymon.agregar_evolucion(metalgreymon)
greymon.agregar_evolucion(aero_v_dramon)
"""
import json
with open("digimon.JSON", "r",encoding="utf-8") as f:
    digimons_data = json.load(f)
print(digimons_data)