salario_presidente = int(input("Introduce salario presidente: "))

print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director: "))

print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce salario jefe de area: "))

print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario administrativo: "))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")
