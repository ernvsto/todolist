# todo.py

def mostrar_menu():
    print("\n--- Mi Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Elegiste: Agregar tarea")
    elif opcion == "2":
        print("Elegiste: Ver tareas")
    elif opcion == "3":
        print("Elegiste: Eliminar tarea")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")