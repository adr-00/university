from lib.binary_search_tree import TreeMap

def escritura_arbol(T,node,d):
    print(2*d*' '+str(node.element()))
    for c in T.children(node):
        escritura_arbol(T,c,d+1)
T = TreeMap()
T[1] = 'A'
T[2] = 'B'
T[3] = 'C'
T[4] = 'C'
T[5] = 'E'

escritura_arbol(T,T.root(), 0)

