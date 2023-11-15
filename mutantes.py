def mostrar_matriz(dna):
    for i in range(6):
        for j in range(6):
            print(dna[i][j], end="\t")
        print("")

def vectores(dna):
    suma = 0
    conTTa, conTTc, conTTg, conTTt = 0, 0, 0, 0
    conTa, conTc, conTg, conTt = 1, 1, 1, 1

    for i in range(len(dna)):
        

        if dna[i] == "a":
            if i < len(dna) - 1:
                if dna[i] == dna[i + 1]:
                    conTa += 1

        if dna[i] == "c":
            if i < len(dna) - 1:
                if dna[i] == dna[i + 1]:
                    conTc += 1

        if dna[i] == "g":
            if i < len(dna) - 1:
                if dna[i] == dna[i + 1]:
                    conTg += 1

        if dna[i] == "t":
            if i < len(dna) - 1:
                if dna[i] == dna[i + 1]:
                    conTt += 1

     
    if conTa >= 4:
        conTTa += 1
    
    if conTc >= 4:
        conTTc += 1
     
    if conTg >= 4:
        conTTg += 1
     
    if conTt >= 4:
        conTTt += 1

    suma = conTTa + conTTc + conTTg + conTTt
    

    return suma == 1
import random


contadorVerdades=0
dna = [["" for _ in range(6)] for _ in range(6)]
import random

def ingresar_dna(opcion):
    if opcion == 1:
        cadena=["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "CCCCTG"]
        matriz_minusculas = [[letra.lower() for letra in fila] for fila in cadena]
        return  matriz_minusculas
    elif opcion == 2:
        cadena=["ATGCAA", "CTGTGC", "TTGTGT", "AGAAGG", "CCACTA", "CCACTG"]
        matriz_minusculas = [[letra.lower() for letra in fila] for fila in cadena]
        return  matriz_minusculas
    elif opcion == 3:
        dna = [["" for _ in range(6)] for _ in range(6)]
        for i in range(6):
            for j in range(6):
                print(f"Ingrese el valor para la fila {i + 1}, columna {j + 1}: ", end="")
                menu = ["a", "a", "g", "t"]

                indice_aleatorio = random.randint(0, len(menu) - 1)

                letra_seleccionada = menu[indice_aleatorio]

                print(f"Letra seleccionada: {letra_seleccionada}")
                dna[i][j] = letra_seleccionada
        return dna
    elif opcion == 4:
        dna = [["" for _ in range(6)] for _ in range(6)]
        for i in range(6):
            for j in range(6):
                letra = input(f"Ingrese el valor para la fila {i + 1}, columna {j + 1} (a/c/g/t): ").lower()
                if letra in ["a", "c", "g", "t"]:
                    dna[i][j] = letra
                else:
                    print("¡Letra no válida! Debe ser 'a', 'c', 'g' o 't'.")
                    j -= 1  # Decrementamos j para volver a solicitar la misma posición
        return dna
    else:
        print("Opción no válida. Selecciona 1, 2 , 3 o 4")

# Menú
print("Selecciona una opción:")
print("1. Ingresar primer conjunto de ADN que dara como resultado MUTANTE (mas de una convinacion repetida de cuatro letras iguales): ")
print("ADN MUTANTE:  [ATGCGA, CAGTGC, TTATGT, AGAAGG, CCCCTA, CCCCTG] ")
print("2. Ingresar segundo conjunto de ADN que dara como resultado HUMANO (una o menos convinaciones de cuatro letras iguales): ")
print("ADN HUMANO: [ATGCAA, CTGTGC, TTGTGT, AGAAGG, CCACTA, CCACTG]")
print("3. Generar conjunto de ADN aleatorio  llenando aleatoriamente con A,C,G y T")
print("4. Ingrear manualmente el codigo de ADN con las siguientes letras:  A,C,G y T")
opcion_elegida = int(input("Ingresa el número de la opción: "))

dna = ingresar_dna(opcion_elegida)



mostrar_matriz(dna)
valor, cont = 0, 0
#print("diagonales secundarias:")
while cont < 3:
    valor = 6 - cont
    diagonales_secundaria = [dna[i][valor - 1 - i] for i in range(valor)]
    # print(vectores(diagonales_secundaria))
    if vectores(diagonales_secundaria):
     contadorVerdades += 1

    cont += 1
#print("diagonales secundarias de abajo:")
cont = 0
while cont < 2:
    valor = 5 - cont
    diagonalesSecundariaA = [dna[i + cont + 1][5 - i] for i in range(valor)]
    # print(vectores(diagonales_secundaria))
    if vectores(diagonalesSecundariaA):
        contadorVerdades += 1
    cont += 1
# print("diagonal principal")
diagonalesPrincipal = [dna[i][i] for i in range(6)]
# print(vectores(diagonalesPrincipal))
if vectores(diagonalesPrincipal):
    contadorVerdades += 1
#print("diagonales principales de arriba")
cont = 0
while cont < 2:
    valor = 5 - cont
    diagonalesPrincipalesB = [dna[i][i + 1 + cont] for i in range(valor)]
    # print(vectores(diagonalesPrincipalesB))
    if vectores(diagonalesPrincipalesB):
        contadorVerdades += 1
    cont += 1
#print("diagonales principales de abajo")
cont = 0
while cont < 2:
    valor = 5 - cont
    diagonalesPrincipalesA = [dna[i + 1 + cont][i] for i in range(valor)]
    # print(vectores(diagonalesPrincipalesA))
    if vectores(diagonalesPrincipalesA):
        contadorVerdades += 1
    cont += 1
#print("columnas")
for j in range(6):
    col = [dna[i][j] for i in range(6)]
    # print(vectores(col))
    if vectores(col):
        contadorVerdades += 1
#print("filas")
for j in range(6):
    fil = [dna[i][j] for i in range(6)]
    # print(vectores(fil))
    if vectores(fil):
        contadorVerdades += 1
 

if contadorVerdades > 1:
       print("ES MUTANTE")
else:
       print("ES HUMANO")

