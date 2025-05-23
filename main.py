
from ClassLinkedList import LinkedList

lista = LinkedList()

lista.add(10)
lista.add(1)
lista.add(14)
lista.add_to_start(4)

lista.show()

index = int(input("Ingrese el indice: "))
valor = lista.find_at(index)

print(f"En la posicion {index} esta {valor}")