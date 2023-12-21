#Desafío de listas

Lista1 = [1, 2, 3]
Lista2 = [10, 20, 30]

Lista1.append(456789)
Lista1.append("Hola Mundo")

Lista2.append("Hola y Adios")
Lista2.append(5555)

Lista3 = Lista1[0:-1]
Lista4 = Lista2[1:-1]
Lista5 = Lista4 + Lista3

print("Lista1:", Lista1)
print("Lista2:", Lista2)
print("Lista3:", Lista3)
print("Lista4:", Lista4)
print("Lista5:", Lista5)