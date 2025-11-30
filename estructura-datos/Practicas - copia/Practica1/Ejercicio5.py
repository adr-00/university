"""
TAD Equipo informático
DESCIPCIÓN: Permite representar equipos informáticos y almacenar sus componentes más importantes.
VALORES: CPU (cadena), RAM (entero), targeta gráfica (entero), número de puertos (entero), fabricante (cadena), SO (cadena).
OPERACIONES:
    Constructor(CPU, RAM, targeta gráfica, número de puertos, fabricante, SO) -> Equipo
        Crea una instancia del TAD Equipo informático
    Cadena(equipo) -> Cadena
        Crea una cadena de un objeto
    get(atributo) -> Atributo
        Obtiene información del equipo
    set(atributo) -> Vacio
        Modifica valor de los atributos. Si se escribe el valor incorrecto da error.
    igual(equipo) -> Bool
        Nos dice si un equipo es igual que otro
    mayor(equipo) -> Bool
        Nos dice si un equipo es mejor que otro, en relación a la RAM(GB), targeta gráfica(número del modelo) y nº de puertos
    menor(equipo) -> Bool
        Nos dice si un equipo es peor que otro, en relación a la RAM(GB), targeta gráfica(número del modelo) y nº de puertos
"""

class ErrorValor(Exception):
    pass

class Equipo_informatico:

    # CONSTRUCTOR
    def __init__(self, cpu, ram, grafica, n_puertos, fabricante, so):
        # isintance nos permite ver si un objeto pertenece a una clase (True o False), lo utilizaremos para ver si
        # los atributos son objetos de las clases str o int, dependiendo del atributo.
        if not isinstance(cpu, str):
            raise ErrorValor("El valor CPU tiene que ser una cadena")
        self._cpu = cpu

        if not isinstance(ram, int):
            raise ErrorValor("El valor RAM tiene que ser un entero")
        self._ram = ram

        if not isinstance(grafica, int):
            raise ErrorValor("El valor targeta gráfica tiene que ser un entero")
        self._grafica = grafica

        if not isinstance(n_puertos, int) or (n_puertos < 0): # El número de puertos tiene que se positivo
            raise ErrorValor("El valor del número de puertos tiene que ser un entero")
        self._n_puertos = n_puertos

        if not isinstance(fabricante, str):
            raise ErrorValor("El valor del fabicante tiene que ser una cadena")
        self._fabricante = fabricante

        if not isinstance(so, str):
            raise ErrorValor("El valor del SO tiene que ser una cadena")
        self._so = so

    # MÉTODO GET
    def get_cpu(self):
        return self._cpu
    def get_ram(self):
        return self._ram
    def get_grafica(self):
        return self._grafica
    def get_n_puertos(self):
        return self._n_puertos
    def get_fabricante(self):
        return self._fabricante
    def get_so(self):
        return self._so
    
    # MÉTODO SET
    def set_cpu(self, cpu):
        if not isinstance(cpu, str):
            raise ErrorValor("El valor CPU tiene que ser una cadena")
        self._cpu = cpu
    def set_ram(self, ram):
        if not isinstance(ram, int):
            raise ErrorValor("El valor RAM tiene que ser un entero")
        self._ram = ram
    def set_grafica(self, grafica):
        if not isinstance(grafica, int):
            raise ErrorValor("El valor targeta gráfica tiene que ser un entero")
        self._grafica = grafica
    def set_n_puertos(self, n_puertos):
        if not isinstance(n_puertos, int) or (n_puertos < 0):
            raise ErrorValor("El valor del número de puertos tiene que ser un entero")
        self._n_puertos = n_puertos
    def set_fabricante(self, fabricante):
        if not isinstance(fabricante, str):
            raise ErrorValor("El valor del fabicante tiene que ser una cadena")
        self._fabricante = fabricante
    def set_so(self, so):
        if not isinstance(so, str):
            raise ErrorValor("El valor del SO tiene que ser una cadena")
        self._so = so
    
    # MÉTODO STR
    def __str__(self):
        return (f"CPU: {self._cpu}\n" 
                f"RAM: {self._ram} \n" 
                f"Targeta gráfica: {self._grafica}\n"
                f"Número de puertos: {self._n_puertos} \n"
                f"Fabricante: {self._fabricante} \n" 
                f"Sistema operativo: {self._so}")
     
    # MÉTODOD GT PARA SABER SI UN EQUIPO ES MEJOR QUE OTRO
    def __gt__(self, equipo2):
        count1 = 0  #Equipo 1
        count2 = 0  #Equipo 2
        if self._ram > equipo2._ram:
            count1 += 1
        else:
            count2 += 1
        if self._grafica > equipo2._grafica:
            count1 += 1
        else:
            count2 += 1
        if self._n_puertos > equipo2._n_puertos:
            count1 += 1
        else:
            count2 += 1
        if count1 > count2:
            return True
        else:
            return False
    
    # MÉTODOD LT PARA SABER SI UN EQUIPO ES PEOR QUE OTRO
    def __lt__(self, equipo2):
        count1 = 0  #Equipo 1
        count2 = 0  #Equipo 2
        if self._ram < equipo2._ram:
            count1 += 1
        else:
            count2 += 1
        if self._grafica < equipo2._grafica:
            count1 += 1
        else:
            count2 += 1
        if self._n_puertos < equipo2._n_puertos:
            count1 += 1
        else:
            count2 += 1
        if count1 > count2:
            return True
        else:
            return False
    
    # MÉTODOD EQ PARA SABER SI UN EQUIPO ES IGUAL QUE OTRO
    def __eq__(self, equipo2):
        return (
        self._cpu == equipo2._cpu and
        self._ram == equipo2._ram and
        self._grafica == equipo2._grafica and
        self._n_puertos == equipo2._n_puertos and
        self._fabricante == equipo2._fabricante and
        self._so == equipo2._so
    )

  
if __name__ == "__main__":
    equipo1 = Equipo_informatico("Intel i5", 16, 3060, 4, "Dell", "Windows 10")
    equipo2 = Equipo_informatico("AMD Ryzen 5", 4, 4060, 6, "Asus", "Linux")
    
    print(equipo2)
    print(equipo1.get_cpu())
    print(equipo1 == equipo2)
    print(equipo1 > equipo2)
    print(equipo1 < equipo2)
    equipo2.set_ram(8)
    print(equipo2.get_ram())
    #equipo1.set_cpu(4), esto da error, ya que CPU no puede ser un entero


        
