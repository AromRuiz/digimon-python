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

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nivel:", self.nivel)
        print("Tipo:", self.tipo)
        print("Atributo:", self.atributo)
        print("Familia:")
        for f in self.familia:
            print("-", f,sep="")

botamon = Digimon("Botamon", "Bebé I", "Baba", "Datos", ["Cazadores de Virus"])
botamon.mostrar()
koromon = Digimon("Koromon", "Bebé II", "Menor", "Datos", ["Cazadores de Virus"])
koromon.mostrar()
agumon = Digimon("Agumon", "Infantil", "Reptil", "Vacuna", ["Espíritus de la Naturaleza", "Cazadores de Virus", "Imperio del Metal"])
agumon.mostrar()
