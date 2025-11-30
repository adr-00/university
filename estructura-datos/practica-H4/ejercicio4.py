from ejercicio1 import texto_a_arbol
from os.path import getsize 

TEXTO = 'texto2.txt'

T = texto_a_arbol(TEXTO)
def espacio_disco(T):
    sum = 0
    for i in T.breadthfirst():
        i = i.element().split('. ')[1].strip()
        sum += getsize(i)
    return f"{sum} bytes"


print(espacio_disco(T))
    


