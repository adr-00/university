from lib.linked_binary_tree import LinkedBinaryTree
from lib.array_stack import ArrayStack
from lib.exceptions import EmptyException

class Atributos:
    def __init__(self, atr1, atr2, atr3):
        self._atr1 = atr1
        self._atr2 = atr2
        self._atr3 = atr3
    
    def __str__(self):
        return f"Atributos: {self._atr1}, {self._atr2}, {self._atr3}"

def calcular_indentacion(linea):
    return int(linea.count(' ')/4)

with open('texto1.txt', 'r', encoding='utf-8') as texto:
    lineas = [linea.rstrip('\n') for linea in texto.readlines()]

lineas = [linea for linea in lineas if linea.strip()]
if not lineas:
    raise EmptyException("El archivo está vacío")

indentaciones = [calcular_indentacion(linea) for linea in lineas]


arbol = LinkedBinaryTree()
root = arbol.add_root(lineas[0])
stack = ArrayStack()
stack.push(root)
id_prev = 0

for i in range(1, len(indentaciones)):
    id_cur = indentaciones[i]
    linea1 = (lineas[i].split('.')[-1]).split(',')
    linea = Atributos(linea1[0], linea1[1], linea1[2])
    
    while id_cur < id_prev:
        stack.pop()
        id_prev -= 1
    
    if id_cur > id_prev:
        parent = stack.top()
        nuevo_nodo = arbol.add_left(parent, linea)
        stack.push(nuevo_nodo)
        id_prev = id_cur
    elif id_cur == id_prev:
        stack.pop()
        parent = stack.top()
        nuevo_nodo = arbol.add_right(parent, linea)
        stack.push(nuevo_nodo)
        id_cur = id_prev

def escritura_arbol(T,node,d):
    print(2*d*' '+str(node.element()))
    for c in T.children(node):
        escritura_arbol(T,c,d+1)

escritura_arbol(arbol, arbol.root(), 1) 


