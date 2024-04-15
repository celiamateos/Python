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
	# Verificar filas y columnas
	for i in range(3):
		if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
			return True

	# Verificar diagonales
	if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
		return True

	return False


# Función para determinar si hay un ganador o si hay empate
def fin_del_juego(jugador1, jugador2, tablero):
	if hay_ganador(tablero, "X"):
		imprimir_tablero(tablero)
		print(COLOR_MAGENTA + f"¡Enhorabuena {jugador1}, has ganado la partida!" + COLOR_RESET)
		return True

	elif hay_ganador(tablero, "O"):
		imprimir_tablero(tablero)
		print(COLOR_CYAN + f"¡Enhorabuena {jugador2}, has ganado la partida!" + COLOR_RESET)
		return True

	if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
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

	jugador1 = nombre_del_jugador(1)
	jugador2 = nombre_del_jugador(2)
	tablero = [[" " for _ in range(3)] for _ in range(3)]
	jugadores = [jugador1, jugador2]
	turno = 0

	while True:
		imprimir_tablero(tablero)
		jugador_actual = jugadores[turno % 2]
		print(COLOR_AZUL + f"Turno de {jugador_actual}" + COLOR_RESET)

		# Protección contra errores si se introduce algo distinto a un número
		try:
			print(f"Ronda: {turno}") 
			fila = int(input("Ingrese el número de fila (1-3): ")) - 1
			columna = int(input("Ingrese el número de columna (1-3): ")) - 1

			if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
				tablero[fila][columna] = "X" if jugador_actual == jugador1 else "O"
				if (fin_del_juego(jugador1, jugador2, tablero)):
					break ;
				turno += 1
			else:
				print("Movimiento inválido. Por favor, intentelo de nuevo.")
		except ValueError:
			print("Por favor, ingrese solo números del 1 al 3.")

if __name__ == "__main__":
	main()
