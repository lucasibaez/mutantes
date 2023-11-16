# mutantes
programacion1global
Nombre y Apellido: Lucas Ibañez
Legajo:50625
DNI:37617408
Email:lucasibaez8@gmail.com
DESCRIPCION DEL PROYECTO:
Este código en Python realiza la verificación de si un conjunto de ADN es mutante o humano según ciertos criterios.

RESUMEN DEL FUNCIONAMIENTO DEL CODIGO:
Principales funcionalidades y estructura del código:

Funciones Definidas:

mostrar_matriz(dna): Muestra en consola la matriz de ADN.
vectores(dna): Evalúa si hay más de una secuencia de cuatro letras iguales en una cadena de ADN. Devuelve True si cumple con el criterio y False en caso contrario.
ingresar_dna(opcion): Permite al usuario seleccionar entre tres opciones para ingresar conjuntos de ADN: dos predefinidos y uno generado aleatoriamente.
Matriz de ADN:

El código utiliza una matriz de 6x6 para representar el ADN.

Forma de uso del codigo:
Menú de Opciones: presenta un menú que permite al usuario seleccionar entre diferentes conjuntos de ADN para evaluar.
 
la opcion 1 automaticamente se ingresa un ADN mutante para su revision.
la opcion 2 automaticamente se ingresa un ADN humano para su revision.
La opción 3 permite generar un conjunto de ADN aleatorio.
La opción 4 permite al usuario ingresar manualmente las letras de la cadena de ADN.

Verificación de Mutante:

Se realizan diversas verificaciones en las diagonales, filas y columnas de la matriz para determinar si el ADN es mutante.
Contador de Verificaciones Exitosas:

Un contador (contadorVerdades) se incrementa cada vez que se encuentra una secuencia de cuatro letras iguales en alguna dirección.
Resultado Final:

Al final, se imprime en consola si el ADN es mutante o humano según la cantidad de verificaciones exitosas que deben ser mas de una.
Este código proporciona una implementación para determinar si un conjunto de ADN tiene características de mutante basándose en las secuencias de cuatro letras 
iguales en diversas direcciones.
 
