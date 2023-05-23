milista = ["Juan", "Pepe", "Luis", "Ana"]

milista.append("Gabriel")  # Agrega un elemento al final de la lista
milista.insert(2, "Sandra")  # Agrega un elemento en la posición indicada
# Agrega varios elementos al final de la lista
milista.extend(["Manolo", "Andres", "Dua"])
milista.pop()  # Elimina el último elemento de la lista

print(milista[:])  # Imprime toda la lista
milista.remove("Ana")  # Elimina el elemento indicado
milista.sort()  # Ordena la lista
milista.reverse()  # Invierte el orden de la lista
print(milista[:])  # Imprime toda la lista
