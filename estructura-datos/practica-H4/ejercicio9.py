from lib.avl_tree import AVLTreeMap
def escritura_arbol(T,node,d):
    print(2*d*' '+str(node.element()))
    for c in T.children(node):
        escritura_arbol(T,c,d+1)

T = AVLTreeMap()
T[62] = 62
T[78] = 78 
T[44] = 44 
T[17] = 17 
T[88] = 88 
T[48] = 48 
T[54] = 54

escritura_arbol(T, T.root(), 0)

