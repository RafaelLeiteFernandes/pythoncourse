# Declaração
minha_lista = [1, 2, 3, 4, 5, "aula", False, True]
minha_lista_numeros = [10, 20, 12, 0, 13]
# Exibindo lista
print ("Minha Lista", minha_lista)

# Exibição dos elementos
minha_lista[0] = "python"

print ("Minha Lista", minha_lista)


print("minha_lista[0]", minha_lista[0])
print("minha_lista[5]", minha_lista[5])
print("minha_lista[1:7]",minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append("Steam")
print("Após o adicionar um elemento ao final da lista:", minha_lista)

# Método index(): Retorna o primeiro elemento do index solicitado
indice = minha_lista.index("Steam")
print("Busca do indice proposto acima:", indice)

# Método insert(): Insere um elemento no index especificado
minha_lista.insert(2, 10)
print("Substituição do valor no index escolhido:", minha_lista)

# Método pop(): Remove e retorna um item de um index específico
elemento_removido = minha_lista.pop(3)
print("Após o pop(3) :", minha_lista)

# Método remove(): Remove o elemento especificado 
minha_lista.remove("python")
print("Após a remoção do elemento:", minha_lista)

# Método sort(): Faz a organização da lista quando a mesma for somente de números
minha_lista_numeros.sort()
print("Após o sort:", minha_lista_numeros)