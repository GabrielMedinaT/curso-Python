midiccionario = {"Alemania": "Berlin", "Francia": "Paris",
                 "Reino Unido": "Londres", "España": "Madrid"}

print(midiccionario["Francia"])
print(midiccionario["España"])
print(midiccionario)
print(midiccionario.keys())


mitupla = ["España", "Francia", "Reino Unido", "Alemania"]
midiccionario = {mitupla[0]: "Madrid", mitupla[1]                 : "Paris", mitupla[2]: "Londres", mitupla[3]: "Berlin"}
print(midiccionario["Alemania"])


midiccionario = {23: "Jordan", "Nombre": "Michael",
                 "Equipo": "Chicago", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario["anillos"])
