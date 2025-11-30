import sys
data = []
for k in range(40):
    a = len(data)
    b = sys.getsizeof(data)
    print('Longitud ', a, ' Tamaño en bytes ', b)
    data.append(None)   

    """La salida se debe al espacio que el interprete de python reserva para la 
    lista, conforme va aumentando el numero de elementos de la lista, se le 
    reserva mas memoria para no tener que reasignar. """