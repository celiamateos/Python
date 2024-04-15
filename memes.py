# to install PIL cmd: pip install pillow

from PIL import Image, ImageDraw, ImageFont
import os

# Función para agregar texto superior e inferior a una imagen
def generar_meme(imagen_path, texto_superior, texto_inferior, output_path):
    try:
        # Cargar la imagen
        imagen = Image.open(imagen_path)
        draw = ImageDraw.Draw(imagen)
        width, height = imagen.size

        # Definir la fuente y el tamaño del texto
        font_path = "arial.ttf"  # Cambia esto a la ruta de tu fuente
        font_size = int(height / 15)
        font = ImageFont.truetype(font_path, font_size)

        # Calcular el tamaño del texto
        text_width, text_height = draw.textsize(texto_superior, font=font)

        # Calcular la posición del texto superior
        x = (width - text_width) / 2
        y = 0

        # Dibujar el texto superior
        draw.text((x, y), texto_superior, fill="white", font=font)

        # Calcular la posición del texto inferior
        text_width, text_height = draw.textsize(texto_inferior, font=font)
        x = (width - text_width) / 2
        y = height - text_height - 10

        # Dibujar el texto inferior
        draw.text((x, y), texto_inferior, fill="white", font=font)

        # Guardar el meme generado
        imagen.save(output_path)
        print("Meme generado exitosamente en:", output_path)

    except Exception as e:
        print("Error al generar el meme:", e)

# Función principal
def main():
    print("¡Bienvenido al generador de memes!")

    # Solicitar la ruta de la imagen
    imagen_path = input("Por favor, introduce la ruta de la imagen: ")

    # Verificar si la imagen existe
    if not os.path.exists(imagen_path):
        print("La imagen no existe.")
        return

    # Solicitar texto superior e inferior
    texto_superior = input("Introduce el texto superior del meme: ")
    texto_inferior = input("Introduce el texto inferior del meme: ")

    # Solicitar la ruta de salida para el meme generado
    output_path = input("Por favor, introduce la ruta de salida para el meme generado (con extensión .jpg): ")

    # Generar el meme
    generar_meme(imagen_path, texto_superior, texto_inferior, output_path)

if __name__ == "__main__":
    main()
