"""
    TAD Empresa
    DESCRIPCIÓN: Guarda los datos de una empresa
    VALORES: Nombre (cadena), CIF (numero), Facturacion en euros (numero),
    Año de creación (numero), numero de empleados (numero).
    OPERACIONES:
        Constructor(nombre, cif, facturacion, año, empleados) -> Empresa
            Crea una instancia del TAD Empresa
        get_(atributo)() -> Vacio
            Obtiene la información de la empresa
        set_(atributos)() -> Vacio
            Modifica la informacion de la empresa
        incrementar_empleado() -> Vacio
            Incrementa el numero de empleados
        decrementar_empleado() -> Vacio
            Decrementa el numero de empleados
"""



class Empresa:
    def __init__(self, nombre, cif, facturacion, año, empleados):
        self.__nombre = nombre
        self.__cif = cif
        self.__facturacion = facturacion
        self.__año = año
        self.__empleados = empleados
    
    def get_nombre(self):
        return self.__nombre
    def get_cif(self):
        return self.__cif
    def get_facturacion(self):
        return self.__facturacion
    def get_año(self):
        return self.__año
    def get_empleados(self):
        return self.__empleados
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_cif(self, cif):
        self.__cif = cif
    def set_facturacion(self, facturacion):
        self.__facturacion = facturacion
    def set_año(self, año):
        self.__año = año
    def set_empleados(self, empleados):
        self.__empleados = empleados

    def incrementar_empleado(self, numero):
        self.__empleados += numero
    
    def decrementar_empleado(self, numero):
        self.__empleados -= numero

if __name__ == "__main__":
    ordenadoresJ = Empresa("OrdenadoresJ", 234, 200000, 2015, 150)
    print(ordenadoresJ.get_año())
    print(ordenadoresJ.get_empleados())
    ordenadoresJ.set_año(2014)
    ordenadoresJ.decrementar_empleado(3)
    print(ordenadoresJ.get_año())
    print(ordenadoresJ.get_empleados())