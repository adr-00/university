import time
from E_AR_validador import validador_E_AR

def leer_datos():
    # Lee el archivo de entrada con los casos de prueba
    with open('./701c.in', "r") as f:
        lineas = f.read().strip().splitlines()  # Lee todas las líneas eliminando espacios vacíos

    # Número de casos de prueba (primera línea del archivo)
    P = int(lineas[0])
    casos = []  # Lista para almacenar todos los casos

    idx = 1  # Índice para recorrer las líneas (empieza en 1 porque la 0 ya se leyó)
    for _ in range(P):
        # Lee número de mecánicos (M) y número de averías (A)
        M, A = map(int, lineas[idx].split())
        idx += 1

        # Leer la matriz C de capacidades (M filas x A columnas)
        # C[i][j] = 1 si el mecánico i puede reparar la avería j, 0 si no
        C = []
        for _ in range(M):
            fila = list(map(int, lineas[idx].split()))
            C.append(fila)
            idx += 1

        casos.append((M, A, C))  # Almacena tupla (mecánicos, averías, matriz capacidades)

    return P, casos  # Retorna número de casos y lista de casos

def solucion(s: list):
    """Verifica si la solución está completa (todas las averías asignadas)"""
    return not 0 in s  # True si no hay ceros (todas las averías tienen mecánico asignado)

def seleccionar(candidatos: list):
    """Seleccionar mejor candidato"""
    return min(candidatos, key=lambda x: x[2])  # Selecciona el mecánico con MENOR capacidad total
    # x[2] = sum(c[i]) = total de averías que puede reparar el mecánico

def factible(s:list, x:list):
    """Verifica si el mecánico x puede reparar alguna avería no asignada"""
    # x = [n_mecanico, lista_averias_resolver, capacidad_total]
    for i in range(len(x[1])):
        if s[i] == 0 and x[1][i] == 1:  # Si avería i sin asignar Y mecánico puede repararla
            return True
    return False

def insertar(s:list, x:list):
    """Asigna al mecánico x la primera avería disponible que pueda reparar"""
    for i in range(len(x[1])):
        if s[i] == 0 and x[1][i] == 1:  # Encuentra primera avería sin asignar que pueda reparar
            s[i] = x[0] + 1  # Asigna mecánico (número +1 porque empieza en 1, no en 0)
            break  # Solo asigna UNA avería por mecánico

def objetivo(s:list):
    """Calcula el número total de averías reparadas"""
    return sum(1 for x in s if x != 0)  # Cuenta averías con mecánico asignado

def voraz(m:int, a:int, candidatos:list):
    """Algoritmo voraz para asignar mecánicos a averías"""
    s = [0] * a
    # Mientras haya candidatos y no se haya alcanzado solución completa
    while len(candidatos) > 0 and not solucion(s):
        x = seleccionar(candidatos)  # Selecciona mecánico con MENOR capacidad
        candidatos.remove(x)  # Elimina de candidatos
        
        if factible(s, x):  # Si puede reparar alguna avería sin asignar
            insertar(s, x)  # Asigna una avería a este mecánico
   
    return s, objetivo(s)  # Retorna asignaciones y número de averías reparadas

if __name__ == "__main__":
    p, problemas = leer_datos()
    tiempo_tamaño = []    
    # Abrir archivo de salida
    with open('./output_E_AR.out', 'w') as f:
        # Escribir número de casos de prueba
        f.write(str(p) + '\n')
        for problema in problemas:
            m, a, c = problema
            # Prepara lista de candidatos: [índice_mecánico, lista_capacidades, capacidad_total]
            candidatos = [[i, c[i], sum(c[i])] for i in range(m)]
            resultado = voraz(m, a, candidatos)
            