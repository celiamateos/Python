

#importa todas las funciones y clases del modulo turtle lo que permite usarlas sin tener q escribir turtle antes de cada funcion o clase
from turtle import * 
import colorsys #importa el modulo colorsys q proporciona funciones para convertir entre diferentes representaciones de color

speed (99) #establece la velocidad del dibujo
bgcolor("black") #color de fondo del lienzo
h = 0 #inizializa la variable h q se utiliza para controlar el cambio de color atraves del espacio de color HSV
for i in range(15): #inicia un bucle q se ejecutara 16 veces
    for j in range(18): #inicia otro bucle dentro del bucle externo
        c = colorsys.hsv_to_rgb(h, 1, 1) #utiliza la funcion hsv_to_rgb del modulo colorsys para convertir el valor actual de h en un color RGB. los parametros 1,1 especifican saturacion y el valor respectivo en el q se mantienen las constantes para obtener coores brillantes
        color(c) #establece el color de dibujo de la tortuga al color RGB calculado
        h += 0.005 #incrementa el valor de h para cambiar gradualmente el color en el espacio de color HSV
        rt(90) #gira la tortuga 90 grados a la derecha
        circle(150 - j * 6, 90) #dibuja un arco de circulo con un radio q disminuye a medida q aumenta j y un angulo de 90 grados. esto forma una parte de la esprial
        lt(90) #gira la tortuga 90 grados a la izquierda
        circle(150 - j * 6, 90) #dibuja otro arco de dirculo similar al anterior pero en sentido contrario
        rt(180) #gira la tortuga 180 grados lo q la coloca en posicion para dibujar la siguiente serie de arcos
    circle(40, 24) #despues de completar los bucles anidados, dibuja un pequeño circulo en el centro del patron
done()
#indica q el dibujo ha terminado y q la ventana puede cerrarse
