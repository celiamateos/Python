import random

# Listas de elementos para las historias
personajes = ["un valiente caballero", "una astuta princesa", "un malvado dragón", "un mago poderoso", "un noble rey", "una encantadora hada"]
lugares = ["un oscuro castillo", "un misterioso bosque", "una bulliciosa ciudad", "una remota montaña", "una isla desierta", "un antiguo templo"]
eventos = ["en busca de un tesoro perdido", "luchando contra fuerzas oscuras", "rescatando a un ser querido", "enfrentándose a un desafío imposible", "descubriendo un secreto milenario", "ayudando a un pueblo en peligro"]



# Función para generar una historia aleatoria
def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)

    # Imprimir la historia generada
    print("Había una vez", personaje, "que se encontraba", lugar, evento + ".")

# Función principal
def main():
    print("¡Bienvenido al generador de historias!")
    print("Aquí tienes una historia aleatoria:")
    generar_historia()

if __name__ == "__main__":
    main()
