"""
name="Botamon"
level="Bebe I"
attribute="Datos\nLibre\nNinguno"
type="Baba"
field="Cazadores de Virus\nEspíritus de la Naturaleza

def digimons_caract(name, level, type, attribute, field):
    print("Nombre:", name)
    print("Nivel:", level)
    print("Tipo:", type)
    print("Atributo:", attribute)
    print("Familia:", field)
digimons_caract("Botamon","Bebe I","Baba", "Datos\nLibre\nNinguno","Cazadores de Virus\nEspíritus de la Naturaleza")
digimons_caract("Koromon","Bebe II","Menor","Datos\nLibre\nNinguno","Cazadores de Virus")
digimons_caract("Agumon","Infantil","Reptil","Vacuna","Espíritus de la Naturaleza\nCazadores de Virus\nImperio del Metal")
"""
"""botamon = {
    "nombre": "Botamon",
    "nivel": "Bebé I",
    "tipo": "Baba",
    "atributo": "Datos",
    "familia": ["Cazadores de Virus", "Espíritus de la Naturaleza"]
}

koromon={
    "nombre":"Koromon",
    "nivel":"Bebe II",
    "tipo":"Menor",
    "atributo":"Datos",
    "familia":["Cazadores de Virus"]
}

agumon={
    "nombre":"Agumon",
    "nivel":"Infantil",
    "tipo":"Reptil",
    "atributo":"Vacuna",
    "familia":["Espíritus de la Naturaleza","Cazadores de Virus","Imperio del Metal"]
}

def digimons_caract(d):
    print("Nombre:",d["nombre"])
    print("Nivel:",d["nivel"])
    print("Tipo:", d["tipo"])
    print("Atributo:",d["atributo"])
    print("Familia:")
    for f in d["familia"]:
        print("-", f,sep="")
digimons_caract(botamon)
digimons_caract(koromon)
digimons_caract(agumon)"""

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

botamon = Digimon("Botamon", "Bebé I", "Baba", "Datos", ["Cazadores de Virus"])
botamon.mostrar()
koromon = Digimon("Koromon", "Bebé II", "Menor", "Datos", ["Cazadores de Virus"])
koromon.mostrar()
agumon = Digimon("Agumon", "Infantil", "Reptil", "Vacuna", ["Espíritus de la Naturaleza", "Cazadores de Virus", "Imperio del Metal"])
agumon.mostrar()
greymon = Digimon("Greymon", "Adulto", "Dinosaurio", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón","Cazadores de Virus", "Imperio del Metal","Soldados de Pesadilla"])
greymon.mostrar()
metalgreymon = Digimon("MetalGreymon", "Perfecto", "Cyborg", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón","Cazadores de Virus", "Imperio del Metal","Soldados de Pesadilla"])
metalgreymon.mostrar()
aero_v_dramon = Digimon("AeroV-dramon", "Perfecto", "Dragón Volador", "Vacuna", ["Espíritus de la Naturaleza","Guardián de las Profundidades","Rugido de Dragón","Cazadores de Virus", "Imperio del Metal","Soldados de Pesadilla"])
aero_v_dramon.mostrar()

botamon.agregar_evolucion(koromon)
koromon.agregar_evolucion(agumon)
agumon.agregar_evolucion(greymon)
greymon.agregar_evolucion(metalgreymon)
greymon.agregar_evolucion(aero_v_dramon)
