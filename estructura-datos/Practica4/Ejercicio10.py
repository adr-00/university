def bisect(palabra, l):
    ini = 0
    fin = len(l)
    while True:
        centro = ((fin - ini)//2) + ini
        if palabra == l[centro]:
            return centro
        elif ini == fin:
            return None
        elif palabra > l[centro]:
            ini = centro + 1
        else:
            ini = centro - 1

l = ["arbol", "casa", "elefante", "hola"]
palabra = "perro"

print(bisect(palabra, l))
