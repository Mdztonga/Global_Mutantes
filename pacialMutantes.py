letras_validas = ['A', 'T', 'C', 'G']
matriz = [[' ' for _ in range(6)] for _ in range(6)]

for fila in range(6):
    for columna in range(6):
        letra = input(f"Ingrese letra para la posición ({fila + 1}, {columna + 1}): ").upper()
        while letra not in letras_validas:
            print("La letra ingresada no corresponde a ninguna válida (A, T, C o G).")
            letra = input(f"Ingrese letra para la posición ({fila + 1}, {columna + 1}): ").upper()
        matriz[fila][columna] = letra
print()
print("Este es su ADN en forma de matriz")
print()
# Aca le mostramos la matriz al usuario
for i in matriz:
    print(' '.join(i))

def isMutant(matriz):
    secuencia = 0
    # La forma horizontal
    for fila in matriz:
        contador = 1
        for i in range(1, len(fila)):
            if fila[i] == fila[i - 1]:
                contador += 1
            else:
                contador = 1
            if contador == 4:
                secuencia += 1
    # La forma vertical
    columna = 0
    while columna < len(matriz[0]):
        contador = 1
        for i in range(1, len(matriz)):
            if matriz[i][columna] == matriz[i - 1][columna]:
                contador += 1
            else:
                contador = 1
            if contador >= 4:
                secuencia += 1
        columna += 1
    # La forma oblicua
    for fila in range(len(matriz) - 3):
        for columna in range(len(matriz[0]) - 3):
            if matriz[fila][columna] == matriz[fila + 1][columna + 1] == matriz[fila + 2][columna + 2] == matriz[fila + 3][columna + 3]:
                secuencia += 1
            if matriz[fila][columna + 3] == matriz[fila + 1][columna + 2] == matriz[fila + 2][columna + 1] == matriz[fila + 3][columna]:
                secuencia += 1
    return secuencia > 1, secuencia

# Verificar si es mutante
es_mutante, cantidad_secuencias = isMutant(matriz)
print()
if es_mutante:
    print(f"Es mutante y se encontraron {cantidad_secuencias} secuencias.")
else:
    print("No es un mutante")
