#Desafío slicing
#Obtener nombre_alumno, nota y materia desde la cadena original
#Mostrar en pantalla "NOMBRE APELLIDO ha sacado un NOTA en MATERIA"

cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_formateada = cadena[::-1]

nombre_alumno   = cadena_formateada[0:12]
nota            = cadena_formateada[14:17]
materia         = cadena_formateada[19::]

print(nombre_alumno)
print(nota)
print(materia)