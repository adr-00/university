from lib.graph import Graph

def buscar_ele(g,ele): #devuelve el vertice dado el elemento
    for v in g.vertices():
        if v.element() == ele:
            return v

def leerGrafo(name):

    f = open(name,'r')
    lineas = f.readlines()
    tipo = lineas[0].rstrip()

    g = Graph(tipo=='D')
    con = set()
    for i in range(1,len(lineas)):
        ver = lineas[i].rstrip().split(' ') # eje de ver[0] a ver[1]
        v1 = g.insert_vertex(ver[0]) if ver[0] not in con else buscar_ele(g,ver[0])
        v2 = g.insert_vertex(ver[1]) if ver[1] not in con else buscar_ele(g,ver[1])
        con.update((ver[0], ver[1]))
        #g.insert_edge(v1,v2,str(i-1))
        g.insert_edge(v1,v2,float(ver[2]))
    return g

def DFS(g,u,discovered):
  for e in g.incident_edges(u):
    v = e.opposite(u)
    if v not in discovered:
      discovered[v] = e
      DFS(g,v,discovered)

def BFS(g,s,discovered):
    level = [s]
    while len(level)>0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level

def construct_path(u,v,discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def DFS_paso2(g,u,discovered):
    for e in g.incident_edges(u,False):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS_paso2(g,v,discovered)

def DFS_complete(g):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g,u,forest)
    return forest


if __name__ == '__main__':

    # creo un grafo

    g = leerGrafo("grafo1.txt")

    print('Numero de vertices ',g.vertex_count())
    print('Numero de ejes',g.edge_count())

    # borro eje A D
    '''
    v1 = buscar_ele(g,'A')
    v2 = buscar_ele(g,'D')
    eje = g.get_edge(v1,v2)
    g.remove_edge(eje)
    '''

    # borro vertice G
    '''
    v1 = buscar_ele(g,'G')
    g.remove_vertex(v1)
    '''

    #imprimo los ejes

    CE = g.edges()
    for e in CE:
        print(e)

    print('Numero de vertices ',g.vertex_count())
    print('Numero de ejes',g.edge_count())

    # Recorrido primero en profundidad
    # Buscar vertice 'A'

    u = buscar_ele(g,'A') 
    result = {u:None}
    DFS(g,u,result)

    print('Busqueda en profundidad desde A')

    for v in result:
        print(v)

    # camino de D a I

    v1 = buscar_ele(g,'D')
    v2 = buscar_ele(g,'I')
    camino = construct_path(v1,v2,result)

    print('Camino desde D a I')

    for v in camino:
        print(v)

    # detectar conectividad en grafo no dirigido

    g2 = leerGrafo('grafo2.txt')

    u2 = buscar_ele(g2,'A') 
    result2 = {u2:None}
    DFS(g2,u2,result2)

    if len(result2) == g2.vertex_count():
        print('El grafo 2 no dirigido es conectado')
    else:
        print('El grafo 2 no dirigido no es conectado')

    # detectar conectividad en grafo dirigido
    # hacemos DFS normal y otro cambiando outgoing por incoming

    # PASO 1

    g3 = leerGrafo('grafo3.txt')

    u3 = buscar_ele(g3,'A') 
    result3 = {u3:None}
    DFS(g3,u3,result3)

    if (len(result3) == g3.vertex_count()): # hacemos paso 2
        result4 = {u3:None}
        DFS_paso2(g3,u3, result4)
        if (len(result4) == g3.vertex_count()):
            print('El grafo dirigido es fuertemente conectado')
    else:
        print('El grafo dirigido no es fuertemente conectado')

    # encontrar todos los componentes conectados no dirigido
        # cada elemento del diccionario con valor None es un componente

    g4 = leerGrafo('grafo4.txt')
    forest = DFS_complete(g4)

    cont = 0
    for u in forest:
        if forest[u] == None:
            cont += 1
    print('Numero de componentes',cont)

    # busqueda en anchura

    u4 = buscar_ele(g2,'A') 
    result4 = {u4:None}
    BFS(g2,u4,result4)

    print('Búsqueda en anchura:')

    for v in result4:
        print(v)
