"""
TTAD Fraccion
DESCIPCIÓN: Permite realizar operaciones basicas con fracciones
VALORES: numerador (numero), denominador (numero)
OPERACIONES:
    Constructor(numerador, denominador) -> Fraccion
        Crea una instancia del TAD Fraccion
    Cadena(frac1) -> Cadena
        Crea una cadena de un objeto
    Suma(frac1) -> Fraccion
        Suma dos fracciones
    Resta(frac1) -> Fraccion
        Resta dos fracciones
    Multiplicacion(frac1) -> Fraccion
        Multiplica dos fracciones
    Division(frac1) -> Fraccion
        Divide dos fracciones
    Igualdad(frac1) -> Bool
        Devuelve True si las dos fracciones son iguales
    Mayor_que(frac1) -> Bool
        Devuelve True si la fraccion es mayor 
    Menor_que(frac1) -> Bool
        Devuelve True si la fraccion es menor a 
    Mayor_igual_que(frac1) -> Bool
        Devuelve True si la fraccion es mayor o igual 
    Menor_igual_que(frac1) -> Bool
        Devuelve True si la fraccion es menor o igual
    Desifualdad(frac1) -> Bool
        Devuelve True si la fraccion es diferente
""" 


class Fraccion:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    def __str__(self):
        return f"Fracción: {self.__numerador}/{self.__denominador}"

    def __add__(self, frac1):
        if self.__denominador == frac1.__denominador:
            return Fraccion(self.__numerador + frac1.__numerador, self.__denominador)
        else:
            denominador_sum = frac1.__denominador * self.__denominador
            return Fraccion((self.__denominador * frac1.__numerador) + (frac1.__denominador * self.__numerador), denominador_sum)
        
    def __sub__(self, frac1):
        if self.__denominador == frac1.__denominador:
            return Fraccion(self.__numerador - frac1.__numerador, self.__denominador)
        else:       
            denominador_res = frac1.__denominador * self.__denominador
            return Fraccion((self.__denominador * frac1.__numerador) - (frac1.__denominador * self.__numerador), denominador_res)
    
    def __mul__(self, frac1):
        return Fraccion(self.__numerador * frac1.__numerador, self.__denominador * frac1.__denominador)
    
    def __truediv__(self, frac1):
        return Fraccion(self.__numerador * frac1.__denominador, self.__denominador * frac1.__numerador)
    
    def __eq__(self, frac1):
        return (self.__numerador * frac1.__denominador) == (frac1.__numerador * self.__denominador)
    
    def __gt__(self, frac1):
        return (self.__numerador * frac1.__denominador) > (frac1.__numerador * self.__denominador)
    
    def __ge__(self, frac1):
        return (self.__numerador * frac1.__denominador) >= (frac1.__numerador * self.__denominador)
    
    def __lt__(self, frac1):
        return (self.__numerador * frac1.__denominador) < (frac1.__numerador * self.__denominador)
    
    def __le__(self, frac1):
        return (self.__numerador * frac1.__denominador) <= (frac1.__numerador * self.__denominador)
    
    def __ne__(self, frac1):
        return (self.__numerador * frac1.__denominador) != (frac1.__numerador * self.__denominador)
    
if __name__ == "__main__":
    fraccion1 = Fraccion(4, 5)
    fraccion2 = Fraccion(2, 6)
    print(fraccion1 + fraccion2)

    fraccion3 = Fraccion(1, 2)
    fraccion4 = Fraccion(5, 4)
    print((fraccion3 * fraccion3)-fraccion4)


    