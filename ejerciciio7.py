import random

# Definición de los nodos
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

# Definición de la tabla hash
class HashTable:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def hash_func(self, key):
        return key % self.tamaño

    def insertar(self, key, valor):
        indice = self.hash_func(key)
        if not self.tabla[indice]:
            self.tabla[indice] = Nodo(valor)
        else:
            nodo_actual = self.tabla[indice]
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = Nodo(valor)

    def buscar(self, key):
        indice = self.hash_func(key)
        nodo_actual = self.tabla[indice]
        while nodo_actual:
            if nodo_actual.valor.endswith(str(key)):
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def eliminar(self, key):
        indice = self.hash_func(key)
        nodo_actual = self.tabla[indice]
        if nodo_actual and nodo_actual.valor.endswith(str(key)):
            self.tabla[indice] = nodo_actual.siguiente
        else:
            prev = None
            while nodo_actual and not nodo_actual.valor.endswith(str(key)):
                prev = nodo_actual
                nodo_actual = nodo_actual.siguiente
            if nodo_actual:
                prev.siguiente = nodo_actual.siguiente

    def obtener_valores(self, key):
        # Devuelve una lista con todos los valores que terminan en el key
        indice = self.hash_func(key)
        valores = []
        nodo_actual = self.tabla[indice]
        while nodo_actual:
            if nodo_actual.valor.endswith(str(key)):
                valores.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return valores

# TIPOS
# Agua, Fuego, Tierra, Electrico, Normal, Fantasma
tipos =["Agua", "Fuego", "Tierra", "Electrico", "Normal", "Fantasma"]

# generacion de 800 pokemones
pokemones= [f'{random.choice(tipos)}-{random.randint(100,9999)}' for _ in range(800)]


# Creación de la tabla hash
# primera lusta tres ultimos digitos del nivel
# segunda de sus tipos

hash_por_nivel = HashTable(1000)
hash_por_tipo = HashTable(6)

for pokemon in pokemones:
    tipo, nivel = pokemon.split('-')
    nivel= nivel[-3:]
    hash_por_nivel.insertar(int(nivel)%1000, pokemon)
    hash_por_tipo.insertar(tipo.index(tipo), pokemon)

#  determinar si el pokemon Fanstama-187 esta cargado y quitarlo
if hash_por_nivel.buscar(187):
    print(hash_por_nivel.buscar(187))
    hash_por_nivel.eliminar(187)
    print("El pokemon Fantasma-187 fue eliminado")

# mision asalto terminado en 78, y los exploracion terminados en 37
pokemon_mision_asalto=hash_por_nivel.obtener_valores(78)
pokemon_mision_exploracion=hash_por_nivel.obtener_valores(37)

# mision asalto
print("Mision Asalto:" ,pokemon_mision_asalto)
print("Mision Exploracion:" ,pokemon_mision_exploracion)

# obtenga pokemon tipo Tierra en misom exploracion
pokemon1_mision_exploracion=hash_por_tipo.obtener_valores(tipos.index("Tierra"))
pokemon1_mison_exterminio=hash_por_tipo.obtener_valores(tipos.index("Fuego"))

# mision exploracion
print("Mision Exploracion:" ,pokemon1_mision_exploracion)
print("Mision Exterminio:" ,pokemon1_mison_exterminio)