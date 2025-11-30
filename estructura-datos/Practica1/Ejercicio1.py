"""
    TAD Usuario
    DESCRIPCIÓN: Representa a un usuario del sistema almacenando sus datos.
    VALORES: Nombre (cadena), apellidos (cadena), edad (numero), direccion (cadena).
    OPERACIONES:
    Constructor(nombre, apellidos edad, direccion) -> Usuario
        Crea una instancia del TAD Usuario.

    describir_usuario() -> Vacio
        Escribe por pantalla los datos de un usuario.

    saludar_usuario() -> Vacio
        Muestra una cadena saludando e incluyendo el nombre del usuario.

    incrementar_edad() -> Vacio
        Suma uno a la edad del usuario. 
"""


class Usuario: 
    def __init__(self, nombre, apellidos, edad, direccion): 
        self.__nombre = nombre 
        self.__apellidos = apellidos 
        self.__edad = edad
        self.__direccion = direccion 
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def describir_usuario(self): 
        print("***Usuario***") 
        print("\tNombre: " + self.__nombre) 
        print("\tApellidos: " + self.__apellidos) 
        print(f"\tEdad: {self.__edad}")
        print(f"\tDireccion: {self.__direccion}") 
 
    def saludar_usuario(self): 
        print(f"Hola {self.__nombre}") 
 
    def incrementar_edad(self): 
        self.__edad += 1
    
    def clasifica_usuario(self):
        if self.__edad < 10:
            print("Niño")
        elif self.__edad < 18:
            print("Adolescente")
        elif self.__edad < 65:
            print("Adulto")
        else:
            print("Anciano")
    
if __name__ == '__main__': 
    jose = Usuario('Jose', 'Santa Lozano', 40, 'Mi direccion') 
    jose.describir_usuario() 
    jose.saludar_usuario() 
    jose.incrementar_edad() 
    jose.describir_usuario()
    jose.clasifica_usuario()


