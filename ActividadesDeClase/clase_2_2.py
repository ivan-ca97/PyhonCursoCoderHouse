#Desafío de tuplas

#A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

#1. El último ítem de tupla
#2. El número de ítems de tupla
#3. La posición donde se encuentra el ítem 87 de tupla
#4. Una lista con los últimos tres ítems de tupla
#5. Un ítem que haya en la posición 8 de tupla
#6. El número de veces que el ítem 7 aparece en tupla

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355, 7, 7)

print(tupla[-1])
print(len(tupla))
print(tupla.index(87))
print(list(tupla[-3::]))
print(tupla[8])
print(tupla.count(7))