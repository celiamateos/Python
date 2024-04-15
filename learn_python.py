# definicion de una funcion
def i_am_fuction():
	name = str(input("Introduce tu nombre: "))
	print("Encantada de conocerte", name)

def main():
	number = 42;
	sentence = "Bienvenido/a a"
	print(sentence, number, "Madrid")
	i_am_fuction()

if __name__ == "__main__":
    main()