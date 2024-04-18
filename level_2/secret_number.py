import random # Importa el modulo random que permite generar numeros aleatorios

def juego_adivinanza():
    numero_secreto = random.randint(1, 100) 
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        try:
            intento = int(input("Introduce tu número: "))
        except ValueError:
            print("Por favor, introduce solo números.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("El número es mayor. ¡Sigue intentándolo!")
        elif intento > numero_secreto:
            print("El número es menor. ¡Sigue intentándolo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

if __name__ == "__main__":
    juego_adivinanza()
