from lib.graph import Graph
from lib.shortest_paths import shortest_path_lengths, shortest_path_tree, construct_path

def buscar_ele(g,ele): #devuelve el vertice dado el elemento
    for v in g.vertices():
        if v.element() == ele:
            return v

def leerGrafo(name):

    f = open(name,'r',encoding='utf-8')
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

def imprimir_grafo(g):
    result = "D\n" if g.is_directed() else "U\n"
    edges = []
    for edge in g.edges():
        u, v = edge.endpoints()
        edges.append(f"{u.element()} {v.element()} {edge.element()}")
    result += "\n".join(edges)
    print(result)

def ejercicio3_4(g):
    vertices = list(g.vertices())
    print("Lista de ciudades:")
    cont = 0
    for vertice in vertices:
        cont +=1
        print(f"{cont}. {vertice}")
    while True:
        try:
            origen = int(input("Introduce el NUMERO de la ciudad de ORIGEN: ")) - 1
            destino = int(input("Introduce el NUMERO de la ciudad de DESTINO: ")) - 1
            
            if 0 <= origen < len(vertices) and 0 <= destino < len(vertices):
                break
            print("Error: Los números deben estar entre 1 y", len(vertices))
        except ValueError:
            print("Error: Debes introducir un número válido")   

    distancias = shortest_path_lengths(g,vertices[origen])
    arbol = shortest_path_tree(g,vertices[origen],distancias)
    camino = construct_path(vertices[origen], vertices[destino], arbol)
    print(f"\nCamino más corto desde {vertices[origen].element()} hasta {vertices[destino].element()}:")
    print(" → ".join(v.element() for v in camino))
    print(f"Distancia total: {distancias[vertices[destino]]} metros")
    
g = leerGrafo("grafo-entregable-casa.txt")
imprimir_grafo(g)
ejercicio3_4(g)