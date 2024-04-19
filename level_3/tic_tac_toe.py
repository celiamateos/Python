# modulo os para limpiar pantalla
import os

# Definir los códigos de color ANSI como variables globales
COLOR_RESET = "\033[0m"
COLOR_NEGRO = "\033[30m"
COLOR_ROJO = "\033[31m"
COLOR_VERDE = "\033[32m"
COLOR_AMARILLO = "\033[33m"
COLOR_AZUL = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"
COLOR_BLANCO = "\033[37m"
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"

# Función para limpiar la pantalla de la terminal
def limpiar_pantalla():
	os.system('cls' if os.name == 'nt' else 'clear')


# Función para verificar si hay un ganador
def hay_ganador(tablero, jugador):
	# Verifica si hay 3 en línea en filas y columnas
	for i in range(3):
		if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
			return True

	# Verifica si hay 3 en línea en diagonales
	if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
		return True

	return False


# Función para determinar si el juego ha terminado, ya sea porque hay un ganador o porque hay empate
def fin_del_juego(jugador1, jugador2, tablero):
	if hay_ganador(tablero, "X"): # Verifica si el jugador 1 (X) ha ganado
		imprimir_tablero(tablero)
		print(COLOR_MAGENTA + f"¡Enhorabuena {jugador1}, has ganado la partida!" + COLOR_RESET)
		return True

	elif hay_ganador(tablero, "O"): # Verifica si el jugador 2 (X) ha ganado
		imprimir_tablero(tablero)
		print(COLOR_CYAN + f"¡Enhorabuena {jugador2}, has ganado la partida!" + COLOR_RESET)
		return True

	if all(tablero[i][j] != " " for i in range(3) for j in range(3)): # Verifica si hay un empate
		imprimir_tablero(tablero)
		print("¡Empate!")
		return True

	return False


# Función para imprimir el tablero con colores
def imprimir_tablero(tablero):
	limpiar_pantalla()
	print("    1   2   3")
	print(NEGRITA + COLOR_VERDE + "   --- --- ---" + COLOR_RESET)
	for i, fila in enumerate(tablero):
		print(f"{i+1} | {' | '.join([NEGRITA + COLOR_MAGENTA + c + COLOR_RESET if c == 'X' else (COLOR_CYAN + c + COLOR_RESET if c == 'O' else c) for c in fila])} |")
		print(NEGRITA + COLOR_VERDE + "   --- --- ---" + COLOR_RESET)


# Función para establecer el nombre del jugador
def nombre_del_jugador(number):
	jugador = input(f"Jugador {number}, por favor ingresa tu nombre: ")
	while not jugador:
		print("El nombre del jugador no puede estar vacío.")
		jugador = input(f"Jugador {number}, por favor ingresa tu nombre: ")

	return (jugador)


# Función principal
def main():
	print("¡Bienvenido al juego de 3 en raya!")

	jugador1 = nombre_del_jugador(1) # Solicita y establece el nombre del jugador 1
	jugador2 = nombre_del_jugador(2) # Solicita y establece el nombre del jugador 2
	tablero = [[" " for _ in range(3)] for _ in range(3)] # Inicializa el tablero
	jugadores = [jugador1, jugador2] # Lista de nombre de los jugadores
	turno = 0 # Inicializa el turno del juego

	while True:
		imprimir_tablero(tablero) # Imprime el estado actual del tablero
		jugador_actual = jugadores[turno % 2] # Determina el jugador actual en función de si el turno es par o impar
		print(COLOR_AZUL + f"Turno de {jugador_actual}" + COLOR_RESET) # Indica de quién es el turno

		try: # Protección contra errores si se introduce algo distinto a un número 
			print(f"Ronda: {turno}") # Imprime el número de la ronda
			fila = int(input("Ingrese el número de fila (1-3): ")) - 1 # Solicita la fila donde colocar la ficha
			columna = int(input("Ingrese el número de columna (1-3): ")) - 1 # Solicita la columna donde colocar la ficha

			if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ": # Verifica si la casilla donde colocar la ficha está vacía 
				tablero[fila][columna] = "X" if jugador_actual == jugador1 else "O" # Coloca la ficha del jugador correspondiente
				if (fin_del_juego(jugador1, jugador2, tablero)): # Verifica si el juego ha terminado
					break ;
				turno += 1 # Avanza al siguiente turno
			else:
				print("Movimiento inválido. Por favor, intentelo de nuevo.")
		except ValueError:
			print("Por favor, ingrese solo números del 1 al 3.") # Manejo de error si se ingresa un valor no numérico

if __name__ == "__main__":
	main() # Llama a la función principal para iniciar el juego
