class ALumnoCID:
    def __init__(self, nombre, dni, curso, asignaturas):
        self.__nombre = nombre
        self.__dni = dni
        self.__curso = curso
        self.__asignaturas = asignaturas
    
    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_curso(self):
        return self.__curso

    def get_asignaturas(self):
        return self.__asignaturas
    
    def set_dni(self, dni):
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_asignaturas(self, asignaturas):
        self.__asignaturas = asignaturas
    
    def set_curso(self, curso):
        self.__curso = curso

    def __iter__(self):
        for j in range(len(self.__asignaturas)):
            yield self.__asignaturas[j]   
            
    def __str__(self):
        return (f"El nombre del alumno es: {self.__nombre}\n"
                f"El dni es: {self.__dni}\n"
                f"El curso es: {self.__curso}\n"
                f"Las asignaturas son: {', '.join(self.__asignaturas)}\n")
    
if __name__ == "__main__":
    alumno = ALumnoCID("Juan Pérez", "12345678A", 1, ["Matemáticas", "Programación", "Estadística"])
    print("Alumno creado:")
    print(alumno)
    print()

    alumno.set_asignaturas(["Computadores", "Programación", "Estadística", "Cálculo"])
    print(alumno)

    print("Iterando sobre las asignaturas:")
    for asignatura in alumno:
        print(asignatura)
    print()

    alumno.set_nombre("Ana García")
    alumno.set_dni("87654321B")
    alumno.set_curso(2)
    print("Datos modificados:")
    print(alumno)

    print(alumno.get_asignaturas())
    print(alumno.get_nombre())
    print(alumno.get_curso())
    print(alumno.get_dni())