print("Asignaturas optativas año 2017")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asi_opt = input("Escribe la asignatura escogida: ")
asignatura = asi_opt.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asi_opt)
else:
    print("La asignatura escogida no está contemplada")
