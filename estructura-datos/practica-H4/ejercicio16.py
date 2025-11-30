from lib.binary_search_tree import TreeMap
from lib.avl_tree import AVLTreeMap
from numpy import arange, delete
from random import shuffle
from lib.EscrituraArbol import escritura_arbol
import time

# Apartado 1
lista = arange(10000)
shuffle(lista)
print(lista)

# Apartado 2 y 3
arbol = TreeMap()
arbolAVL = AVLTreeMap()
for i in lista:
    arbol[i] = i
    arbolAVL[i] = i

# Apartado 4, 5 y 6
def busqueda_lista():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        for j in range(len(lista)):
            if lista[j] == i:
                print(f'Encontrado el número: {i}')
                print(f"Quedan {len(lista)-contador} para terminar")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

def busqueda_lista_eliminacion():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        for j in range(len(lista)):
            if lista[j] == i:
                print(f'Encontrado el número: {i}')
                print(f"Quedan {len(lista)-contador} para terminar")
                delete(lista, i)
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

def busqueda_binaria():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        if i in arbol:
          print(f'Encontrado el número: {i}')
          print(f"Quedan {len(lista)-contador} para terminar")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")


def busqueda_AVL():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        if i in arbolAVL:
            print(f'Encontrado el número: {i}')
            print(f"Quedan {len(lista)-contador} para terminar")
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

def busqueda_binaria_eliminacion():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        if i in arbol:
            print(f'Encontrado el número: {i}')
            print(f"Quedan {len(lista)-contador} para terminar")
            del arbol[i]
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")


def busqueda_AVL_eliminacion():
    inicio = time.perf_counter()
    contador = 0
    for i in lista:
        contador += 1
        if i in arbolAVL:
            print(f'Encontrado el número: {i}')
            print(f"Quedan {len(lista)-contador} para terminar")
            del arbolAVL[i]
    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

"""
    APARTADO 4

    El árbol AVL tiene un orden de complejidad de log n, conforme se aumenta
    el número de elementos, el orden de complejidad se vuelve estable. Al
    aumentar el número de elementos la diferencia con las otras estructuras
    se nota más.

    El árbol de búsqueda binaria tiene complejidad de h, que es la altura del
    árbol. Los número al estar desordenados podría ayudar a no tener desbalances
    que es lo que ocurriria si los elementos estuvieran ordenados, que el orden 
    de complejidad es de n. Pero a medida que crece el número de elementos, 
    aunque esten desordenados, es muy probable que se creen desbalances, que aumentan
    el h.

    Las listas tienen un orden de complejidad de n, conforme aumenta el número de 
    elementos el tiempo lo hace también.

    Esto hace que para un número de elementos pequeños apenas se note diferencia,
    pero conforme aumentos el nÚmero de elementos, el árbol AVL es el más estable.

    APARTADO 5

    Si eliminamos elementos, el n disminuye y los órdenes de complejidad de búsqueda 
    se reducen conforme disminuye el n, al igual que los de eliminación. Por lo 
    que tarda menos. Esto al igual que la búsqueda normal, se hace mas notable 
    cuanto mayor es el n. Para los árboles de búsqueda binaria, en ocasiones la 
    eliminacion de elementos padría crear mas desbalances, lo que no ayudaría 
    tanto al orden de complejidad.
    
    APARTADO 6
    Cuando se varían el número de elementos, se puede observar claramente los 
    órdenes de complejidad. En las lista conforme se aumenta el número de elementos,
    tarda cada vez mas, al igual que el árbol de básqueda binaria. Sin embargo, el 
    AVL esa diferencia de tiempo se va haciendo mas pequeña.

    En general, los tiempos cuando los elementos son pocos, son parecidos, pero 
    cuando ese número va aumentando la diferencia se va notando cada vez más a favor
    del arbol AVL.
"""