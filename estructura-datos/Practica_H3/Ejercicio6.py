class Libro:
    def __init__(self, titulo, autor, genero, año):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._año = año
        self._ejemplares = 1
    
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, titulo):
        self._titulo = titulo
    
    def get_autor(self):
        return self._autor
    
    def set_autor(self, autor):
        self._autor = autor
    
    def get_genero(self):
        return self._genero
    
    def set_genero(self, genero):
        self._genero = genero
    
    def get_año(self):
        return self._año
    
    def set_año(self, año):
        self._año = año
    
    def get_ejemplares(self):
        return self._ejemplares
    
    def set_ejemplares(self, ejemplares):
        self._ejemplares = ejemplares
    
    def __str__(self):
        return (f"Nombre: {self._titulo}, Autor: {self._autor}, Año: {self._año}, Genero: {self._genero}, Ejemplares: {self._ejemplares}")

def listado_obras():
    for isbn, libro in biblioteca.items():
        print(f"ISBN: {isbn}. Libro: {libro}")

def añadir_obra():
    titulo = str(input("¿Cual es el titulo del libro?: "))
    autor = str(input("¿Quien es el autor?: "))
    genero = str(input("¿Cual es el genero?: "))
    año = str(input("¿Cual es el año?: "))
    isbn = str(input("¿Cual es el ISBN?: "))

    if isbn in biblioteca:
        libro_existente = biblioteca.get(isbn)
        libro_existente.set_ejemplares(libro_existente.get_ejemplares() + 1)
    else:
        libro_nuevo = Libro(titulo, autor, genero, año)
        biblioteca[isbn] = libro_nuevo
    print(f"Libro añadido: {biblioteca[isbn]}")

def eliminar_obra():
    isbn = str(input("¿Que isbn quieres eliminar?"))
    if isbn in biblioteca:
        print(f"Libro eliminado: {biblioteca[isbn]}")
        del biblioteca[isbn]
    else:
        print("No existe el isbn en la biblioteca")

def mostrar_obra():
    isbn = str(input("¿Que isbn quieres mostrar?"))
    if isbn in biblioteca:
        print(f"ISBN: {isbn}. Libro: {biblioteca[isbn]}")
    else:
        print("No existe el isbn en la biblioteca")

def decrementar_ejemplar():
    isbn = str(input("¿A que isbn quieres decrementar el ejemplar?"))
    if isbn in biblioteca:
        libro = biblioteca[isbn]
        libro.set_ejemplares(libro.get_ejemplares()-1)
        print(f"Ejemplares de {isbn} decremetados a {libro.get_ejemplares()}")
    else:
        print("No existe el isbn en la biblioteca")

def aumentar_ejemplar():
    isbn = str(input("¿A que isbn quieres aumentar el ejemplar?"))
    if isbn in biblioteca:
        libro = biblioteca[isbn]
        libro.set_ejemplares(libro.get_ejemplares()+1)
        print(f"Ejemplares de {isbn} aumentados a {libro.get_ejemplares()}")
    else:
        print("No existe el isbn en la biblioteca")
    

def obras_disponible():
    for isbn, libro in biblioteca.items():
        if libro.get_ejemplares() != 0:
            print(f"ISBN: {isbn}. Libro: {libro}")




if __name__ == "__main__":
    biblioteca = {}
    terminar = False
    while terminar == False:
        print("\nMenú de opciones:")
        print("1. Añadir obra")
        print("2. Eliminar obra")
        print("3. Mostrar obra")
        print("4. Decrementar ejemplar")
        print("5. Aumentar ejemplar")
        print("6. Listado de obras")
        print("7. Obras disponibles")
        print("8. Salir")

        opcion  = str(input("Dame un número:"))
        if opcion == "1":
            añadir_obra()
        elif opcion == "2":
            eliminar_obra()
        elif opcion == "3":
            mostrar_obra()
        elif opcion == "4":
            decrementar_ejemplar()
        elif opcion == "5":
            aumentar_ejemplar()
        elif opcion == "6":
            listado_obras()
        elif opcion == "7":
            obras_disponible()
        elif opcion == "8":
            terminar = True
        else:
            print("No existe esa opcion")



        