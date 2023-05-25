from tda_cola import Cola, cola_vacia, arribo, atencion
from tda_heap import Heap, arribo as arribo_h, heap_vacio, atencion as atencion_h
from tda_heap import cambiar_prioridad, buscar as buscar_h
from tda_lista_lista import Lista, barrido, eliminar, insertar
from tda_pila_dinamico import Pila, apilar, pila_vacia, desapilar
from math import inf


class nodoArista(object):
    """Clase nodo vértice."""

    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info, datos=None):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.datos = datos
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista() # lista de aristas


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de arsitas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato, datos=None):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato, datos)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregrar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregrar_arista(destino.adyacentes, dato, origen.info)

def agregrar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                quitar_arista(aux.adyacentes, clave)
            aux = aux.sig
        # aca terminar eliminar aristas adyacenes grafo no dirigido
    return x


def quitar_arista(vertice, destino):
    x = None
    if(vertice.adyacentes.inicio.destino == destino):
        x = vertice.adyacentes.inicio.info
        vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.inicio
        act = vertice.adyacentes.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1
    return x

def eliminar_arista(grafo, vertice, destino):
    """Elimina una arsita del vertice y lo devuelve si lo encuentra."""
    x = quitar_arista(vertice, destino)    
    
    if(not grafo.dirigido):
        ori = buscar_vertice(grafo, destino)
        quitar_arista(ori, vertice.info)

    return x

def barrido_vertices(grafo):
    """Realiza un barrido de la grafo mostrando sus valores."""
    aux = grafo.inicio
    while(aux is not None):
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes(aux)
        aux = aux.sig


def buscar_vertice(grafo, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def tamanio(grafo):
    """Devuelve el numero de vertices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo esta vacio."""
    return grafo.inicio is None

def distancia_maxima(grafo):
    """Devuelve la distancia maxima entre dos vertices del grafo."""
    maximo = 0
    aux = grafo.inicio
    while(aux is not None):
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            if(adyacentes.info > maximo):
                maximo = adyacentes.info
            adyacentes = adyacentes.sig
        aux = aux.sig
    return maximo


def adyacentes(vertice):
    """Muestra los adyacents del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig

def marcar_no_visitado(grafo):
    """Marca todos losvertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux.visitado = False
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if(not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_distancia(grafo, distancia):
    """Barrido en profundidad del grafo."""
    aux = grafo.inicio
    while(aux is not None):
        if(aux.adyacentes.inicio is not None):
            adyacentes = aux.adyacentes.inicio
            while(adyacentes is not None):
                if(adyacentes.info == distancia):
                    print(aux.info, str("-"), adyacentes.destino)
                adyacentes = adyacentes.sig
        aux = aux.sig

def barrido_profundidad_distancia(grafo, distancia):
    # dado una distnaica, mostrar todos los vertices que se encuentran a esa distancia
    lista = []
    """Barrido en profundidad del grafo."""
    aux = grafo.inicio
    while(aux is not None):
        if(aux.adyacentes.inicio is not None):
            adyacentes = aux.adyacentes.inicio
            while(adyacentes is not None):
                if(adyacentes.info == distancia) and (aux.info not in lista):
                    lista.append(aux.info)
                adyacentes = adyacentes.sig
        aux = aux.sig
    return barrido_lista(lista)

def barrido_lista(lista):
    for i in range(len(lista)):
        print(lista[i])








def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    cola = Cola()
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino



def prim(grafo):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while(adyac is not None):
        arribo_h(aristas, [grafo.inicio.info, adyac.destino], adyac.info)
        adyac = adyac.sig
    while(len(bosque) // 2 < tamanio(grafo) and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        if(len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque))):
            bosque += dato[1]
            destino = buscar_vertice(grafo, dato[1][1])
            adyac = destino.adyacentes.inicio
            while(adyac is not None):
                arribo_h(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque

def prim_ultmo_nodo(g, nodo):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo, dado un nodo que es siempre el ultimo nodo del grafo."""
    bosque=[]
    aristas=Heap(tamanio(g)**2)
    adyacentes=nodo.adyacentes.inicio
    while(adyacentes is not None):
        arribo_h(aristas,[nodo.info,adyacentes.destino],adyacentes.info)
        adyacentes=adyacentes.sig
    while(len(bosque)//2<tamanio(g) and not heap_vacio(aristas)):
        dato=atencion_h(aristas)
        if(len(bosque)==0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque))):
            bosque+=dato[1]
            destino=buscar_vertice(g,dato[1][1])
            adyacentes=destino.adyacentes.inicio
            while(adyacentes is not None):
                arribo_h(aristas,[destino.info,adyacentes.destino],adyacentes.info)
                adyacentes=adyacentes.sig
    return bosque[::-1]





def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyac = aux.adyacentes.inicio
        while(adyac is not None):
            arribo_h(aristas, [aux.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        aux = aux.sig
    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if(dato[1][0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if(dato[1][1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
                break
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[1][0], dato[1][1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[1][0], dato[1][1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]

def existe_paso(grafo, origen, destino):
    """Barrido en profundidad del grafo."""
    resultado = False
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while(vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if(adyacente.info == destino.info):
                return True
            elif(not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

g= Grafo(False)

Tareas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M',"FIN"]
for i in range(len(Tareas)):
    insertar_vertice(g, Tareas[i])

peso_arista=[20,5,40,10,5,10,20,25,35,25,15,5,25]

A=buscar_vertice(g,'A')
B=buscar_vertice(g,'B')
C=buscar_vertice(g,'C')
D=buscar_vertice(g,'D')
E=buscar_vertice(g,'E')
F=buscar_vertice(g,'F')
G=buscar_vertice(g,'G')
H=buscar_vertice(g,'H')
I=buscar_vertice(g,'I')
J=buscar_vertice(g,'J')
K=buscar_vertice(g,'K')
L=buscar_vertice(g,'L')
M=buscar_vertice(g,'M')
FIN=buscar_vertice(g,'FIN')


# la duracion de las taresa es el peso de cada arista. Algunas tareas se debe reaizar antes que otras, los nodos no estan todos conectados entre sí.
# peso toral = 100
# B-c-h-M
# G-H
#A-D-E-F

# I-K-L
# J
insertar_arista(g,20,A,D)
insertar_arista(g,20,A,E)
insertar_arista(g,5,E,F)
insertar_arista(g,10,D,F)
insertar_arista(g,10,F,M)

insertar_arista(g,5,B,C)
insertar_arista(g,35,C,H)
insertar_arista(g,5,B,G)
insertar_arista(g,15,G,H)
insertar_arista(g,25,H,M)

insertar_arista(g,35,I,K)
insertar_arista(g,25,K,L)
insertar_arista(g,25,I,M)

insertar_arista(g,15,M,FIN)



# arbol de expansion minima
print('Arbol de expansion minima')
# FIN siempre es el ultimo nodo
print('Prim con FIN como ultimo nodo')
print(prim_ultmo_nodo(g,FIN))

