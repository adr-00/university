

terminar = False
traductor = {}
traduccion = str(input("Dame la traducción: "))
frase_separada = traduccion.split(",")   
print(frase_separada)
for palabra in frase_separada:
    palabras = palabra.split(":")
    traductor[palabras[0]] = palabras[1]

for i in traductor.items():
    print(i)

frase = (input("Dame una frase: "))
frase_separadada = frase.split( )
frase_output = ""
for i in frase_separadada:
    if i in traductor.keys():            
        frase_output = frase_output + " " + traductor[i]
    else:
        frase_output = frase_output + " " + i    
print(frase_output)



    

