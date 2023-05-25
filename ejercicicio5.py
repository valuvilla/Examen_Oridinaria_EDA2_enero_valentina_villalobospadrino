class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.fin = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def suma_elementos(self):
        suma = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            suma += nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
        return suma

    def rama_siguiente(self):
        a = ListaEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            indice_lista = nodo_actual.valor
            lista_siguiente = [4, 6, 6, 8, 7, 9, 4, 8, 3, 9, 0, 1, 7, 0, 2, 6, 1, 3, 2, 4]
            for indice in indice_lista:
                a.agregar(lista_siguiente[indice])
            nodo_actual = nodo_actual.siguiente
        return a

    def n_ramas(self, n):
        for i in range(n):
            suma_actual = self.suma_elementos()
            print("{}:".format(i+1), suma_actual)
            self = self.rama_siguiente()

# Crear una instancia de ListaEnlazada y agregar el primer nivel del árbol
lista = ListaEnlazada()
lista.agregar([0])

# Ejecutar el algoritmo para calcular los elementos del árbol hasta el n-ésimo nivel
lista.n_ramas(32)
