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
pokemones= [f'{random.choice(tipos)}-{random.randint(1000,9999)}' for _ in range(800)]


# Creación de la tabla hash
# primera lusta tres ultimos digitos del nivel
# segunda de sus tipos

hash