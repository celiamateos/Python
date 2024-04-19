# importar el modulo time
import time


# definicion de una funcion
def i_am_fuction():
	# Definir variable name de tipo string
	name = str(input("Introduce tu nombre: "))

	# Printear cadena de caracteres "Encantada de conocerte" + variable nombre
	print("Encantada de conocerte", name)

	# Esperar 1 antes de continuar
	time.sleep(1)
	
	# Condicion: Si nombre es menor que 5 caracteres, entonces printear nombre + "tu nombre es corto"
	if len(name) < 6:
		print(f"{name}, tu nombre es corto")
	# Condicion opuesta, si no se cumple la condicion anterior, entonces printear nombre + "tu nombre es largo"
	else:
		print(f"{name}, tu nombre es largo")
	
	time.sleep(1)

	# Inicia un bucle infinito
	while True:
		# Declaracion variable llamada orden, su contenido se obtendrá por la respuesta que escribamos a la pregunta ¿Qué quieres hacer?
		orden = str(input("¿Qué quieres hacer? "))
		# Condición si nuestra respuesta es salir, break: rompemos el bucle
		if orden == "salir":
			break ;
		# Si no, nos dirá que no sabe lo que es la orden que le hemos dado
		else:
			print(f"no se lo que es {orden}")



# Declaracion de funcion principal, funcion main
def main():
	# Declaración de variable tipo int, número entero
	number = 42;
	
	# Declaracion de variable tipo string, cadena de caracteres
	sentence = "Bienvenido/a a"

	# Funcion printear variable string + variable int + string "Madrid"
	print(sentence, number, "Madrid")

	# Esperar 1 antes de continuar
	time.sleep(1)

	# Llamar a la funcion i_am_fuction
	i_am_fuction()


# Protección 
if __name__ == "__main__":
    main()