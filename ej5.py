#Suma todos los elementos que hay
def suma_elementos(lista):
    suma=0
    for i in range(len(lista)):
        suma+=len(lista[i])
    return suma

#Calcula los elementos de la siguiente lista en el árbol
def rama_siguiente(lista):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    b=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            b.append(a[lista[i][j]])
    return b


#Calcula los elementos del árbol hasta el n-ésimo nivel
def n_ramas(n):
    a=[[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    for i in range(n):
        b=rama_siguiente(a)
        print("{}:".format(i+1), suma_elementos(a))
        a=b

#Es un algoritmo bastante lento, por lo que aunque no es perfecto, funciona hasta cierto punto.
n_ramas(32)
"""
1: 20
2: 46
3: 104
4: 240
5: 544
6: 1256
7: 2848
8: 6576
9: 14912
10: 34432
11: 78080
12: 180288
13: 408832
14: 944000
15: 2140672
16: 4942848
17: 11208704
18: 25881088
19: 58689536
"""