from ejercicio0 import Graph_str 
g = Graph_str()

v1 = g.insert_vertex("Garg")
v2 = g.insert_vertex("Goodrich")
v3 = g.insert_vertex("Snocynk")
v4 = g.insert_vertex("Goldwasser")
v5 = g.insert_vertex("Tamassia")
v6 = g.insert_vertex("Tollis")
v7 = g.insert_vertex("Vitter")
v8 = g.insert_vertex("Preparata")
v9 = g.insert_vertex("Chiang")

e1 = g.insert_edge(v1, v2, 3)
e2 = g.insert_edge(v3, v2, 2)
e3 = g.insert_edge(v4, v2, 5)
e4 = g.insert_edge(v2, v5, 1)
e5 = g.insert_edge(v2, v7, 4)
e6 = g.insert_edge(v2, v9, 9)
e7 = g.insert_edge(v1, v5, 1)
e8 = g.insert_edge(v4, v5, 6)
e9 = g.insert_edge(v6, v5, 6)
e10 = g.insert_edge(v6, v7, 1)
e11 = g.insert_edge(v5, v9, 8)
e12 = g.insert_edge(v5, v8, 9)
e13 = g.insert_edge(v5, v7, 7)
e14 = g.insert_edge(v8, v9, 7)
e15 = g.insert_edge(v7, v8, 4)

def print_file(g, file_name):
    with open(file_name, "w") as file:
        file.write(str(g))

print_file(g, "grafo100.txt")
