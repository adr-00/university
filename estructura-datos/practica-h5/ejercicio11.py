from lib.graph import Graph
from lib.shortest_paths import shortest_path_lengths, shortest_path_tree

def leerGrafo(name):
    f = open(name,'r', encoding="utf-8")
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


def imprimir_grafo(grafo):
    lista = ["D" if grafo.is_directed() else "U"]
    for e in grafo.edges():
        cadena2 = ""
        cadena2 += (e.endpoints()[0].element()) + " "
        cadena2 += (e.endpoints()[1].element()) + " "
        cadena2 += str(e.element())
        lista.append(cadena2)
    cadena = ""
    for i in lista:
        cadena += i + "\n"
    return cadena

def buscar_ele(g,ele): 
    for v in g.vertices():
        if v.element() == ele:
            return v

def print_file(g, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        contenido = imprimir_grafo(g)
        file.write(contenido)

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



if __name__ == "__main__":
    g = leerGrafo("grafo-entregable-casa.txt") # Leemos el grafo
    print_file(g, "grafo-generado.txt") # Lo reescribimos en un fichero nuevo

    print("Ciudades disponibles: ")
    ciudades = []
    for i, v in enumerate(g.vertices()):
        #ciudades.append(v)
        print(f"{i}. {v}")


    a = input("Introduce lugar de salida: ")
    b = input("Introduce destino: ")
    
    # Buscamos los vértices con el origen y el destino como elementos
    v_salida = buscar_ele(g, a) 
    v_destino = buscar_ele(g, b)

    D = shortest_path_lengths(g, v_salida) # Obtenemos las distancias más cortas a cada vertice desde v_salida

    tree = shortest_path_tree(g, v_salida, D) # Obtenemos los vértices por los que pasan

    camino = construct_path(v_salida, v_destino, tree) # Obtenemos el camino de v_salida a v_destino
    print(f"Camino desde {a} a {b}: ")
    for i, s in enumerate(camino):
        print(f"{i+1}. {s}")


