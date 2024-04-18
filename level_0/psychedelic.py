from turtle import *  # Importa todo desde el módulo turtle para usar sus funciones de dibujo.
import colorsys  # Importa el módulo colorsys para manipular colores en el espacio de color HSV.
bgcolor('black')  # Establece el color de fondo del lienzo de dibujo en negro.
tracer(900)  # Acelera el dibujo, haciendo que las actualizaciones sean más rápidas

def draw():  # Define una función llamada draw para dibujar un patrón
    h = 0  # Inicializa la variable h para almacenar el componente de matiz del color en 0
    for i in range(100):  # Bucle para iterar sobre un rango de valores
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Convierte el valor de matiz (h) a un color RGB
        h += 0.5  # Incrementa el valor de matiz para cambiar el color
        # h += 0.42
        up()  # Levanta el lápiz del lienzo para moverse sin dibujar
        goto(0, 0)  # Mueve la tortuga a la posición (0, 0) sin dibujar
        down()  # Baja el lápiz del lienzo para empezar a dibujar
        color('black')  # Establece el color de la línea en negro
        fillcolor(c)  # Establece el color de relleno en el color calculado
        begin_fill()  # Comienza a llenar la figura con el color de relleno
        rt(98)  # Gira a la derecha 98 grados
        circle(i, 12)  # Dibuja un círculo con radio i y un ángulo de 12 grados
        fd(290)  # Avanza hacia adelante 290 unidades
        fd(i)  # Avanza hacia adelante la distancia i
        lt(29)  # Gira a la izquierda 29 grados
        for j in range(129):  # Bucle para iterar sobre un rango de valores
            fd(i)  # Avanza hacia adelante la distancia i
            circle(j, 299, steps=3)  # Dibuja un círculo con radio j y 3 lados
        end_fill()  # Finaliza el relleno de la figura
draw()  # Llama a la función draw para dibujar el patrón
done()  # Termina el programa de dibujo
