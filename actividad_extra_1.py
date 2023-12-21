
#iMenuWidth = 50
#strMenuUpperFrame = [b'\xdc'.decode('cp437') for i in range(iMenuWidth)]
#print("".join(strMenuUpperFrame))

print("============================")
print("Ingrese el nombre del alumno")
print("============================")
strStudentName = input()
FinalScore = 0


arrScoreWeight = [0.2, 0.3, 0.5]
for i in range(1, 4):
    print("Ingrese la calificación de la nota ", i)
    Score = int(input())
    if Score > 10 or Score < 0:
        print("Error, la nota debe ser menor que 10 y mayor que 0. Intente nuevamente")
        exit()
    FinalScore = FinalScore + Score * arrScoreWeight[i - 1]

print("La nota final de", strStudentName, "es:", FinalScore)