# Función para mostrar la lista de tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. [{tarea[1]}] {tarea[0]}")

# Función para agregar una tarea a la lista
def agregar_tarea(tareas):
    tarea = input("Ingrese la nueva tarea: ")
    prioridad = input("Ingrese la prioridad de la tarea (alta, media, baja): ").lower()
    tareas.append((tarea, prioridad))
    print("Tarea agregada correctamente.")

# Función para eliminar una tarea de la lista
def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if tareas:
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea eliminada: {tarea_eliminada[0]}")
        else:
            print("Índice inválido.")
    else:
        print("No hay tareas para eliminar.")

# Función para marcar una tarea como completada
def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if tareas:
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_completada = tareas.pop(indice)
            print(f"Tarea completada: {tarea_completada[0]}")
        else:
            print("Índice inválido.")
    else:
        print("No hay tareas para marcar como completadas.")

# Función principal
def main():
    print("¡Bienvenido al organizador de listas de tareas!")
    tareas = []

    while True:
        print("\n1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            completar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
