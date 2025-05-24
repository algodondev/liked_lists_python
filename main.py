
import os
from ClassLinkedList import LinkedList

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')

lista = LinkedList()

while True:
    
    clear_console()
    opcion = input("Menu de Linked Lists\n" \
    "a. Mostrar lista\n" \
    "b. Insertar al final\n" \
    "c. Insertar al inicio\n" \
    "d. Insertar en una posicion especifica\n" \
    "e. Eliminar al final\n" \
    "f. Eliminar al inicio\n" \
    "g. Eliminar de una posicion especifica\n" \
    "h. Eliminar por valor\n" \
    "i. Buscar\n" \
    "j. SALIR\n")

    match opcion:
        case "a":
            clear_console()
            if(lista.length() > 0):
                lista.show()
            else:
                print("La lista esta vacia")

            input("\nPresiona cualquier tecla para continuar... ")
        case "b":
            clear_console()
            valor = int(input("Valor a insertar: "))
            lista.add(valor)
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "c":
            clear_console()
            valor = int(input("Valor a insertar: "))
            lista.add_to_start(valor)
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "d":
            clear_console()
            valor = int(input("Valor a insertar: "))
            pos = int(input("Posicion donde insertar: "))
            lista.insert_at(valor, pos)
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "e":
            clear_console()
            lista.delete_last()
            print("Ultimo valor eliminado")
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "f":
            clear_console()
            lista.delete_first()
            print("Primer valor eliminado")
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")
        case "g":
            clear_console()
            pos = int(input("Posicion a eliminar: "))
            lista.delete_at(pos)
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "h":
            clear_console()
            valor = int(input("Valor a eliminar: "))
            lista.delete_by(valor)
            print("\nNuevos valores de lista: \n")
            lista.show()
            input("\nPresiona cualquier tecla para continuar...")

        case "i":
            clear_console()
            op = int(input("Seleccione una opcion\n" \
            "\n1. Buscar por valor\n" \
            "2. Buscar por posicion\n"))

            match op:
                case 1:
                    val = int(input("Inserte el valor a buscar: "))
                    print(f"El valor se encuentra en la posicion {lista.find(val)}")
                case 2:
                    ind = int(input("Inserte la posicion a buscar: "))
                    if ind >= lista.length(): 
                        print("Posicion no valida")
                    else:
                        print(f"La posicion {ind} contiene el valor {lista.find_at(ind).get_data()}")
                case _:
                    input("Opcion no disponible, presiona cualquier tecla para volver al menu principal...")
            input("Presiona cualquier tecla para volver al menu principal... ")

        case "j":
            break
        case _:
            print("Opcion no disponible")
    