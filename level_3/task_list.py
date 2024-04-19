# Función para mostrar la lista de tareas.
def mostrar_tareas(tareas):
    if not tareas:  # Verifica si la lista de tareas está vacía.
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        # Itera sobre las tareas enumerándolas y las muestra en formato: [i]. [prioridad] tarea.
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. [{tarea[1]}] {tarea[0]}")

# Función para agregar una tarea a la lista.
def agregar_tarea(tareas):
    tarea = input("Ingrese la nueva tarea: ")  # Solicita la nueva tarea al usuario.
    prioridad = input("Ingrese la prioridad de la tarea (alta, media, baja): ").lower()  # Solicita la prioridad de la tarea.
    tareas.append((tarea, prioridad))  # Agrega la tarea y su prioridad a la lista de tareas.
    print("Tarea agregada correctamente.")

# Función para eliminar una tarea de la lista.
def eliminar_tarea(tareas):
    mostrar_tareas(tareas)  # Muestra la lista de tareas actual.
    if tareas:  # Verifica si hay tareas en la lista.
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1  # Solicita el índice de la tarea a eliminar.
        if 0 <= indice < len(tareas):  # Verifica si el índice es válido.
            tarea_eliminada = tareas.pop(indice)  # Elimina la tarea seleccionada y la guarda en la variable 'tarea_eliminada'.
            print(f"Tarea eliminada: {tarea_eliminada[0]}")  # Muestra la tarea eliminada.
        else:
            print("Índice inválido.")
    else:
        print("No hay tareas para eliminar.")

# Función para marcar una tarea como completada.
def completar_tarea(tareas):
    mostrar_tareas(tareas)  # Muestra la lista de tareas actual.
    if tareas:  # Verifica si hay tareas en la lista.
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1  # Solicita el índice de la tarea a completar.
        if 0 <= indice < len(tareas):  # Verifica si el índice es válido.
            tarea_completada = tareas.pop(indice)  # Completa la tarea seleccionada y la guarda en la variable 'tarea_completada'.
            print(f"Tarea completada: {tarea_completada[0]}")  # Muestra la tarea completada.
        else:
            print("Índice inválido.")
    else:
        print("No hay tareas para marcar como completadas.")

# Función principal que ejecuta el organizador de listas de tareas.
def main():
    print("¡Bienvenido al organizador de listas de tareas!")
    tareas = []  # Inicializa la lista de tareas.

    while True:
        print("\n1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")  # Solicita al usuario que elija una opción.

        if opcion == "1":
            mostrar_tareas(tareas)  # Muestra la lista de tareas.
        elif opcion == "2":
            agregar_tarea(tareas)  # Agrega una nueva tarea.
        elif opcion == "3":
            eliminar_tarea(tareas)  # Elimina una tarea existente.
        elif opcion == "4":
            completar_tarea(tareas)  # Marca una tarea como completada.
        elif opcion == "5":
            print("¡Hasta luego!")  # Mensaje de despedida.
            break  # Sale del bucle y termina la ejecución del programa.
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")  # Manejo de opción inválida.

if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa.
