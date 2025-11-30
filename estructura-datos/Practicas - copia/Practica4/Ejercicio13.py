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
                f"Las asignaturas son: {self.__asignaturas}\n")
    
p = ALumnoCID("PEPE", "23455G", 1, ["Programacion", "Mates"])
for i in p:
    print(i)
