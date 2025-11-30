from lib.array_queue import ArrayQueue

Q = ArrayQueue()
Q.enqueue("Pepe")
Q.enqueue("Emma")
Q.enqueue("Adrián")
Q.enqueue("Felipe")

while len(Q) > 1:
    texto = input("Dame un texto: ")
    if texto == "p":
        print(f"Jugador {Q.dequeue()} eliminado")
    c = Q.dequeue()
    Q.enqueue(c)

print(f"El jugador {Q.dequeue()} ha ganado ")

     