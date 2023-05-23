print("Ejemplo de condicionales")

nota_alumno = int(input("Introduce la nota: "))


def notas(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


notas(nota_alumno)
print(notas(nota_alumno))
