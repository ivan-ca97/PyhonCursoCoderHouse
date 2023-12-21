#Desafío números
#20 partidos
#Partido ganado -> 3 puntos | Partido empatado -> 1 punto | Partido perdido -> 0 puntos
#Calcular promedio de puntos

TotalMatchesNum = 20

print("============================")
print("Ingrese el nombre del equipo")
print("============================")

TeamName = input()
FinalScore = 0

print("Ingrese la cantidad de partidos ganados")
WonMatchesNum = int(input())
print("Ingrese la cantidad de partidos empatados")
TiedMatchesNum = int(input())
print("Ingrese la cantidad de partidos perdidos")
LostMatchesNum = int(input())

if(WonMatchesNum + TiedMatchesNum + LostMatchesNum != TotalMatchesNum):
    print("Error: Se disputaron 20 partidos")
    exit()

print("El promedio de puntos es", (WonMatchesNum * 3 + TiedMatchesNum * 1 + LostMatchesNum * 0) / TotalMatchesNum)