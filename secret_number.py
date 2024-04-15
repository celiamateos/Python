import random #importa el modulo random q permite generar numeros aleatorios

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


#     __name__: Es una variable especial en Python que almacena el nombre del módulo actual. 
#     Cuando un script es ejecutado directamente, el valor de __name__ es establecido como "__main__". 
#     Cuando un script es importado como un módulo en otro script, el valor de __name__ es establecido como el nombre del módulo.

#     "__main__": Es el nombre especial dado al módulo principal en Python cuando es ejecutado directamente.

# Por lo tanto, la línea 18 verifica si el script actual está siendo ejecutado directamente (es decir, como el programa principal). 
# Si es así, se ejecuta el código que sigue a esta línea. 
# Esto es útil cuando se tiene código en un script que se desea ejecutar solo cuando el script es ejecutado directamente, 
# y no cuando es importado como un módulo en otro script.