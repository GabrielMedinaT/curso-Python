print("Control de acceso")

edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("No puedes pasar")
elif edad > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("El programa ha finalizado")


print("Notas de alumnos")

nota = int(input("Introduce la nota: "))

if nota < 4:
    print("Insuficiente")
elif nota < 5:
    print("Suficiente")
elif nota < 6:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
