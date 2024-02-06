# For usando lista
print("For usando lista")
lista = [1, 2, 3, 4, 5]

for numeros in lista:
    print(numeros)

# For usando tupla
print("For usando tupla")
tupla = (1, 2, 3, 4, 5)

for numeros in tupla:
    print(numeros)

# range(): intevalo numérico 

print("\n Usando range()")

for numero in range(5):
    print("Numero:", numero)

print("\n Usando range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Numero:", indice)

# enumerate()
    lista_enumerate = ["a","b","c","d"]
    for indice, valor in enumerate(lista_enumerate):
        print(f"{indice}: {valor}")