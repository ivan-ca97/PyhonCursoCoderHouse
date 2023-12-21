#==================================================
#Actividad 2 - Parte 5

matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4]
]

for i in range(0, 4):
    matriz[i].append(sum(matriz[i]))

print(matriz)