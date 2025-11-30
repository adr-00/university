empleados = []
clientes = []
while len(empleados) < 10:
    nombre = input("Dame un nombre de empleado")
    empleados.append(nombre)

while len(clientes) < 5:
    nombre = input("Dame un nombre de clientes")
    clientes.append(nombre)
empleados = set(empleados)
clientes = set(clientes)
print(empleados)
print(clientes)

#Repetidos en los dos
print(empleados&clientes)

#Empleados que no aparecen en clientes
print(empleados-clientes)
