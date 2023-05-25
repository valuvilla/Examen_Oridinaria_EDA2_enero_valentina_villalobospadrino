class NodoHuffman:
    def __init__(self, valor, frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
 
    def __lt__(self, otro):     
        return self.frecuencia < otro.frecuencia
 
    def __eq__(self, otro):    
        if otro == None:
            return False
        if not isinstance(otro, NodoHuffman):
            return False
        return self.frecuencia == otro.frecuencia
 

class Arbol:
    def calcular_frecuencias(mensaje):
        frecuencias = {}
        for caracter in mensaje:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        return frecuencias
    
    def construir_arbol_huffman(frecuencias):
        nodos = []
        for caracter, frecuencia in frecuencias.items():
            nodos.append(NodoHuffman(caracter, frecuencia))
        while len(nodos) > 1:
            nodos.sort()
            nodo_izq = nodos.pop(0)
            nodo_der = nodos.pop(0)
            nodo_padre = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
            nodo_padre.izquierda = nodo_izq
            nodo_padre.derecha = nodo_der
            nodos.append(nodo_padre)
        return nodos[0]
    
    def codificar_caracter(nodo, caracter, codigo_actual):
        if nodo == None:
            return None
        if nodo.valor == caracter:
            return codigo_actual
        codigo_izq = Arbol.codificar_caracter(nodo.izquierda, caracter, codigo_actual + "0")
        if codigo_izq != None:
            return codigo_izq
        codigo_der = Arbol.codificar_caracter(nodo.derecha, caracter, codigo_actual + "1")
        return codigo_der
    
    def codificar_mensaje(mensaje, arbol_huffman):
        mensaje_codificado = ""
        for caracter in mensaje:
            codigo = Arbol.codificar_caracter(arbol_huffman, caracter, "")
            mensaje_codificado += codigo
        return mensaje_codificado
    
    def decodificar_mensaje(mensaje_codificado, arbol_huffman):
        mensaje_decodificado = ""
        nodo_actual = arbol_huffman
        for bit in mensaje_codificado:
            if bit == "0":
                nodo_actual = nodo_actual.izquierda
            elif bit == "1":
                nodo_actual = nodo_actual.derecha
            if nodo_actual.valor != None:
                mensaje_decodificado += nodo_actual.valor
                nodo_actual = arbol_huffman
        return mensaje_decodificado
    

if __name__ == "__main__":

    frecuencias = {"T":0.15, "O":0.15, "A":0.12, "E": 0.10, "H":0.09, "S": 0.07, "P": 0.07}
    arbol_huffman = Arbol.construir_arbol_huffman(frecuencias)
    mensaje_coficado = "0011111010111001100110111010"
    mensaje_decodificado = Arbol.decodificar_mensaje(mensaje_coficado, arbol_huffman)
    print(mensaje_decodificado)
    # coficar mensaje
    mensaje = mensaje_decodificado
    mensaje_codificado2 = Arbol.codificar_mensaje(mensaje, arbol_huffman)
    print(mensaje_codificado2)