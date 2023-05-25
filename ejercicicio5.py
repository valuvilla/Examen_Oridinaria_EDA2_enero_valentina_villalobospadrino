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

    def contador_por_dic(self, dic_prev, dic):
        contador = 0
        a = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            indice_lista = nodo_actual.valor
            for indice in indice_lista:
                for k in a[indice]:
                    dic[k] += dic_prev[nodo_actual.valor]
                    contador += dic_prev[nodo_actual.valor]
            nodo_actual = nodo_actual.siguiente
        return contador, dic

    def n_dic(self, n):
        dic_prevpar = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        dic_previmpar = {0: 2, 1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2}
        cont = 0
        for i in range(n-1):
            if i % 2 == 0:
                dicp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
                cont, dicp = self.contador_por_dic(dic_prevpar, dicp)
                print("{}:".format(i+2), cont)
                # print(dicp, "\n") #Descomentar para ver los diccionarios intermedios pares
                dic_prevpar = dicp
            else:
                dici = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
                cont, dici = self.contador_por_dic(dic_previmpar, dici)
                print("{}:".format(i+2), cont)
                # print(dici, "\n") #Descomentar para ver los diccionarios intermedios impares
                dic_previmpar = dici
        return cont

# Crear una instancia de ListaEnlazada y agregar el primer nivel del árbol
lista = ListaEnlazada()
lista.agregar([0])

print("Solución para el problema de los caballos:")
lista.n_dic(32)
