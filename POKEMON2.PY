import unittest


class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        

    def __str__(self):
        return "Lo que quiero mostrar"

    def __repr__(self):
        return f"Pokemon: ({self.name},  Tipo: {self.tipo})"
    
    
    def calificacion(self, tipo):
        # puede ser PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad
        return f"La calificacion de {self.nombre} es {self.tipo}"
    

class TestPokemon(unittest.TestCase):
    # crear un numero arbitrario de pokemones
    def setUp(self):
        self.pikachu = Pokemon("Pikachu", "Electrico")
        self.charmander = Pokemon("Charmander", "Fuego")
        self.squirtle = Pokemon("Squirtle", "Agua")
        self.bulbasaur = Pokemon("Bulbasaur", "Planta")
        self.pidgey = Pokemon("Pidgey", "Volador")
        self.rattata = Pokemon("Rattata", "Norma")
